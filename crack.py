from multiprocessing.dummy import Pool
from parameters import Encoding
from parameters import HashFunctions
import argparse
import multiprocessing
import time

THREADS = multiprocessing.cpu_count()

parser = argparse.ArgumentParser(description='Crack passwords')
parser.add_argument('dictionary', type=str, metavar='dict_file',
    help='List of word - password candidates')
parser.add_argument('hashlist', type=str, metavar='hash_file',
    help='List of hashes')
parser.add_argument('-e', '--encoding', type=Encoding,
    help='Choose encoding', default=Encoding.utf8)
parser.add_argument('-f', '--function', type=HashFunctions,
    help='Choose which hash functions to use', default=HashFunctions.sha256)

args = parser.parse_args()
hashlist_path = args.hashlist
dictionary_path = args.dictionary
encoding = args.encoding.value
hash_function_name = args.function

def compute_hash(line):
    line = line.rstrip('\n')
    hash_object = hash_function_name.get_hash_object()
    hash_object.update(line.encode(encoding=encoding))
    hash = hash_object.hexdigest()
    return hash

def worker(hashed_passwords, chunk_of_dict):
    local_dict = dict()
    for word in chunk_of_dict:
        hashed_word = compute_hash(word)
        matches = [hash for hash in hashed_passwords if hashed_word == hash]
        if (len(matches) != 0):
            local_dict[word] = matches
    return local_dict
    
hashed_passwords = None

def worker_wrapper(chunk_of_dict):
    return worker(hashed_passwords, chunk_of_dict)

def worker_init(hashes):
    global hashed_passwords
    hashed_passwords = hashes
    
def main():
    answer = []
    with open(hashlist_path, 'r') as hashlist, open(dictionary_path, 'r') as dictionary:
        dict = dictionary.readlines()
        dict = [el.rstrip('\n') for el in dict]
        init_hashes = hashlist.readlines()
        init_hashes = [hash.rstrip('\n') for hash in init_hashes]
        chunksize = int(len(init_hashes) / THREADS)
        chunksize = chunksize if chunksize > 0 else chunksize + 1
        chunks = [dict[i: i + chunksize]
            for i in range(0, len(dict), chunksize)]
        pool = multiprocessing.Pool(THREADS, initializer=worker_init, initargs=(init_hashes,))
        start_time = time.perf_counter()
        for chunk in chunks:
            result_dict = pool.apply_async(worker_wrapper, (chunk,))
            answer.append(result_dict)
        pool.close()
        pool.join()
    for async_res in answer:
        dict = async_res.get()
        if dict:
            print(dict)
    print(f"Completed Execution in {time.perf_counter() - start_time} seconds")

if __name__ == '__main__':
    main()
