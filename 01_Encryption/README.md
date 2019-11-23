# Encryption I have worked on in my early career in cybersecurity

This is a folder for the beginner encryption i have worked on. most of it is very basic but we all had to start somewhere.

# 01_Transposition
Transposition Cipher will take a message as split it up into a grid and take the columns in a certain order (key) and print it out in that order. to decrypt it takes the key and sets the encrypted in a similar grid used to encrypt. and will take the column with key value 1 and put that as the first new decrypted grid and then so on with key value 2 and so on


- encrypter.py
> this file has a function called **encryptMessage()** which takes a string to encrypt and a key that it will use to encrypt the message.

- decrypter.py
> this file has a function called **decryptMessage()** which takes a encrypted string to decrypt and a key that it will use to decrypt the message.

- modified_tranposition.py
> this file puts the encrypter and decrypter files together and takes a file (specifically mystery.txt) and has a key allredy assignd. it will then decrypt the .txt file and produce a decrypt file called mystery.dec.txt


# 02_
