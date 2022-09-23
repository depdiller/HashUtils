from parameters import Encoding
from parameters import HashFunctions
import argparse

parser = argparse.ArgumentParser(description='Crack passwords')
parser.add_argument('file', type=str, metavar='file',
    help='Text file with passwords-condidates')
parser.add_argument('-e', '--encoding', type=Encoding,
    help='Choose encoding', default=Encoding.utf8)
parser.add_argument('-f', '--function', type=HashFunctions,
    help='Choose which hash functions to use',
    default=HashFunctions.sha256)

args = parser.parse_args()
input_file_path = args.file
encoding = args.encoding.value
hash_function_name = args.function


