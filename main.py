import os
import hashlib

MIN_CHARACTER = 0x0 # 0
MAX_CHARACTER = 0x110000 # 1,114,112

def hash_key(key):
    return hashlib.sha256(key.encode("ascii")).hexdigest()

print("""Select one of the following options...
1. Encrypt a file
2. Decrypt a file""")

is_encrypting = None
while is_encrypting is None:
    selection = input("Enter the selection number: ")
    if selection == "1":
        is_encrypting = True
    elif selection == "2":
        is_encrypting = False
    else:
        print("Invalid selection! Please try again.")

file_name = input("Enter the file name: ")
key = input("Enter the key: ")

file_contents = None

if os.path.exists(file_name + ".key"):
    if is_encrypting:
        print("File was already encrypted")
        quit()
    else:
        with open(file_name + ".key", "r", encoding = "utf-8") as f:
            if hash_key(key) != f.read():
                print("Wrong key")
                quit()   
        os.remove(file_name + ".key")    
else:
    if is_encrypting:
        with open(file_name + ".key", "w", encoding = "utf-8") as f:
            f.write(hash_key(key))
    else:
        print("File is not encrypted")
        quit()
    
# Reading in the file contents
with open(file_name, "r", encoding = "utf-8") as f:
    file_contents = f.read()

# Encryption of the file contents
encrypted_contents = ""

for i in range(len(file_contents)):
    file_character_code = ord(file_contents[i])
    key_character_code = ord(key[i % len(key)]) 

    if is_encrypting:
        encrypted_contents += chr((file_character_code + key_character_code) % MAX_CHARACTER)
    else:
        encrypted_contents += chr((file_character_code - key_character_code) % MAX_CHARACTER)

with open(file_name, "w", encoding = "utf-8") as f:
    f.write(encrypted_contents)