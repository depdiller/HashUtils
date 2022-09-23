import argparse
from ast import arg, parse
from dataclasses import dataclass
from enum import Enum
import hashlib

class Encoding(Enum):
    utf8 = 'UTF-8'
    ascii = 'ASCII'
    utf16be = 'UTF-16-BE'
    utf16le = 'UTF-16-LE'
    
    def __str__(self) -> str:
        return self.value
    
class HashFunctions(Enum):
    md4 = 'md4'
    md5 = 'md5'
    sha256 = 'sha256'
    sha1 = 'sha1'
    sha512 = 'sha512'

    def __str__(self) -> str:
        return self.value
    
    def get_function(self):
        fun = getattr(hashlib, self.value)
        return fun


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
number_of_generated_values = args.n

with open(input_file_path, 'r', encoding=encoding) as input_file, open(output_file_path, 'w', encoding=encoding) as output_file:
    for i, line in enumerate(input_file):
        hash_function = args.function.get_function()
        hash_function().update(line.encode(encoding=encoding))
        hashed_line = hash_function().hexdigest()
        output_file.write(hashed_line)