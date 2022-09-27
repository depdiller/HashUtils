## Лабораторная работа №1

### Описание утилит:
- Gen
```
usage: gen.py [-h] [-e ENCODING] [-f FUNCTION] [-o OUTPUT] file n

Hash generator

positional arguments:
  file                  Text file with passwords
  n                     How many hash codes should be generated

optional arguments:
  -h, --help            show this help message and exit
  -e ENCODING, --encoding ENCODING
                        Choose encoding
  -f FUNCTION, --function FUNCTION
                        Choose which hash functions to use
  -o OUTPUT, --output OUTPUT
                        Output file to store hash codes
```

- Crack
```
usage: crack.py [-h] [-e ENCODING] [-f FUNCTION] dict_file hash_file

Crack passwords

positional arguments:
  dict_file             List of word - password candidates
  hash_file             List of hashes

optional arguments:
  -h, --help            show this help message and exit
  -e ENCODING, --encoding ENCODING
                        Choose encoding
  -f FUNCTION, --function FUNCTION
                        Choose which hash functions to use
```

##### Поддерживаемые кодировки и хэш-функции:
###### Кодировки:
- utf-8
- ascii
- utf-16-be
- utf-16-le
###### Хэш-функции
- md4
- md5
- sha256
- sha1
- sha512

Стандартные параметры: кодировка - utf-8, хэш-функция - sha256, выходной файл с хэшами в утилите `gen` - output.txt

### Benchmark

Параметры среды: 
- Процессор: *Apple M1 8 ядер*
- Размер словаря кондидатов в пароли: *492_086 слов*
- Размер словаря хэшей: *50_000 слов*

Время работы утилиты `crack` - 249 секунд, что составляет около *1_976 кандидатов/секунду*
