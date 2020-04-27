
# Encryption I have worked on in my early career in cybersecurity

This is a folder for the beginner encryption i have worked on.

# 01_Transposition
Transposition Cipher will take a message as split it up into a grid and take the columns in a certain order (key) and print it out in that order. to decrypt it takes the key and sets the encrypted in a similar grid used to encrypt. and will take the column with key value 1 and put that as the first new decrypted grid and then so on with key value 2 and so on


- encrypter.py
> this file has a function called **encryptMessage()** which takes a string to encrypt and a key that it will use to encrypt the message.

- decrypter.py
> this file has a function called **decryptMessage()** which takes a encrypted string to decrypt and a key that it will use to decrypt the message.

- modified_tranposition.py
> this file puts the encrypter and decrypter files together and takes a file (specifically mystery.txt) and has a key allredy assignd. it will then decrypt the .txt file and produce a decrypt file called mystery.dec.txt


# 02_Caesar_Cipher
- caesar_cipher.py
> this program will take a key, a mode "encrypt" or "decrypt" and the message as a string and will output the encrypted or decrypted message with the given key using the Caesar cipher
 - stronger_caesar_cipher.py
 > similar to the first but:
 > 1.  The first letter of the message is shifted according to the chosen key, exactly as before (i.e.a key of ‘3’ shifts the first letter up by 3 for encryption).
 >  2. All remaining letters are shifted according to the previous letter of the message. So, if the message is simply the word “gold”, the ‘g’ is enciphered as per the Caesar Cipher, but the ‘o’ is shifted up 6 positions, since the letter ‘g’ corresponds to the number 6. The ‘l’ is then shifted up 14 positions, and the ‘d’ is shifted up 11 positions. If the initial key is ‘3’, this gives a ciphertext of “juzo”.
- caesar_cipher_2.py
> this time instead of a number the key can be a word.
> the key will work in the following ways:
> 1. Let’s call the length of the keyword n (so if the keyword is “cdgd”, n is 4). The first n letters of the message are shifted according to the nth letter of the keyword. So, if the keyword is “cdgd”, the first letter of the message would be shifted by 2 (since ‘c’ corresponds to 2), the second would be shifted by 3, the third by 6, and the fourth by 3.
> 2. If there are more than n letters is the message, then the mth letter, where m > n, is shifted according to the (m − n)th letter of the plaintext message itself. So, if the message is “helloworld” and the keyword is, again, “cdgd”, the ‘o’, being the fifth letter, is shifted according to letter (5 − 4) = 1 of the message, which is ‘h’, which gives a shift of 7, so the ‘o’ is enciphered as ‘v’. The sixth letter, ‘w’, is enciphered using the next letter in the plaintext, which is ‘e’, so the ‘w’ is enciphered as ‘a’. This process ultimately gives a ciphertext of “JHROVAZCZZ”.





