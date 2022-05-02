# Encryption Demo
Project used for showcasing basic encryption techniques. This implementation builds off of a ceasar
cypher by using a key instead of a number of letters. 

Obviously, this is for educational purposes and should not be used as an actual encryption tool.

## More detail on how it works...
* The user is prompted to either encrypt or decrypt a specified file
* Then, the user enters a key to use for encryption/decryption
* The program will make sure the specified file is not encrypted/decrypted twice (for example,
  decrypted files cannot be further decrypted)
* The program will shift each character in the file using the characters in the key. Characters
  outside of range are wrapped around.
* The encrypted/decrypted file is saved.
* If encrypting, the key is saved in a seperate file in hashed form for password checking.
* If decrypting, the key file is deleted.

## License
This project is licensed under the Unlicense which can be read [here](LICENSE).