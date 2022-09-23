from enum import Enum
import hashlib

class Encoding(Enum):
    utf8 = 'utf-8'
    ascii = 'ascii'
    utf16be = 'utf-16-be'
    utf16le = 'utf-16-le'
    
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
    
    def get_hash_object(self):
        return hashlib.new(self.value)