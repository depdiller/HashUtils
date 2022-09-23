import re
from this import d
from parameters import Encoding
from parameters import HashFunctions
import argparse
import multiprocessing

parser = argparse.ArgumentParser(description='Crack passwords')
parser.add_argument('hashlist', type=str, metavar='file',
    help='List of hashes')
parser.add_argument('dictionary', type=str, metavar='file',
    help='List of word - password candidates')
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
    hash_object = hash_function_name.get_hash_object()
    hash_object.update(line.encode(encoding=encoding))
    return hash_object.hexdigest()

result_dictionary = None

def worker(hash, word_list):
    matches = [word for word in word_list if compute_hash(word) == hash]
    result_dictionary[hash] = matches
    
word_list = None

def worker_wrapper(hash):
    return worker(word_list, hash)

def worker_init(dictionary):
    global word_list
    global result_dictionary
    word_list = dictionary
    result_dictionary = dict()

with open(hashlist_path, 'r') as hashlist, open(dictionary_path, 'r') as dictionary:
    init_dict = dictionary.readlines()
    pool = multiprocessing.Pool(proccesses=4, initializer=worker_init, initargs=(init_dict))
    init_hashes = hashlist.readlines()
    pool.map(worker_wrapper, init_hashes)
    pool.close()
    pool.join()
    pool.terminate()
    

print(result_dictionary)