import db
import hashing

import os

db.create_table()


user_input_path = input("Enter Path of the file, you want to observe "
                        "(e.g. Host-File in C:\\Windows\\System32\\drivers\\etc): ")
filename = input("Enter the name of the File: ")
hashpath_joined = os.path.join(user_input_path)

try:
    os.chdir(hashpath_joined)
    hash_value = hashing.hash_calculation(filename)
    hashed_file = hashpath_joined + "\\" + filename
    print("Hashvalue of " + hashed_file + " is " + hash_value)
    db.insert_data(hashed_file, hash_value)
except IOError:
    print("Typo in file-path or file does not exist")


def compare():
    pass
