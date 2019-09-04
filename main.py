import db
import hashing

import os

db.create_table()


hashpath = input("Enter Path of the file, you want to observe (e.g. Host-File in C:\Windows\System32\drivers\etc): ")
filename = input("Enter the name of the File: ")
hashpath_joined = os.path.join(hashpath)

try:
    os.chdir(hashpath_joined)
    hash_value = hashing.hash_calculation(filename)
    print(hash_value)
except IOError:
    print("Typo in file-path or file does not exist")
