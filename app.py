import argparse
from enum import Enum
from hashlib import sha256
from tokenize import String

class Encoding(Enum):
    utf8 = 'UTF-8'
    ascii = 'ASCII'
    utf16be = 'UTF-16_BE'
    utf16le = 'UTF-16_LE'
    
    def __str__(self) -> str:
        return self.value
    
class HashFunctions(Enum):
    md4 = 'MD4'
    md5 = 'MD5'
    sha256 = 'SHA-256'
    sha1 = 'SHA-1'
    sha512 = 'SHA-512'

    def __str__(self) -> str:
        return self.value

parser = argparse.ArgumentParser(description='Hash generator')
parser.add_argument('-f', '--file', type=String,
    help='Text file with passwords', required=True)
parser.add_argument('-e', '--encoding', type=Encoding,
    help='Choose encoding')
parser.add_argument('')