import argparse
from random import randint
from parameters import Encoding
from parameters import HashFunctions

parser = argparse.ArgumentParser(description='Hash generator')
parser.add_argument('file', type=str, metavar='file',
    help='Text file with passwords')
parser.add_argument('-e', '--encoding', type=Encoding,
    help='Choose encoding', default=Encoding.utf8)
parser.add_argument('-f', '--function', type=HashFunctions,
    help='Choose which hash functions to use',
    default=HashFunctions.sha256)
parser.add_argument('n', help='How many hash codes should be generated')
parser.add_argument('-o', '--output', type=str, 
    help='Output file to store hash codes', default='./output.txt')

args = parser.parse_args()
input_file_path = args.file
encoding = args.encoding.value
output_file_path = args.output
number_of_generated_values = int(args.n)
hash_function_name = args.function

def hash(line):
    hash_object = hash_function_name.get_hash_object()
    hash_object.update(line.encode(encoding=encoding))
    return hash_object.hexdigest()

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    i = 0
    line = input_file.readline()
    while i < number_of_generated_values and len(line) != 0:
        hashed_line = hash(line.rstrip('\n'))
        output_file.write(hashed_line + '\n')
        i += 1
        line = input_file.readline()
    
    while i < number_of_generated_values:
        random_number = str(randint(1, 1_000_000_000))
        hashed_line = hash(random_number)
        output_file.write(hashed_line + '\n')
        i += 1
        