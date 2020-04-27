
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
# 03_Pseudorandom_numbers
- PRNG.py
>this program is a pseudorandom number generators (PRNGs). this produces a  sequence of pseudorandom numbers, which appear random, but which, with some extra (typically hidden) information, can be predicted. it uses a  linear congruential generator (LCG)  Algorithm. this is a recurrence relation similar to the affine cipher’s encryption function to generate its pseudorandom numbers
>LCG uses the formua: 
>Ri+1 = (aRi + b) (mod m) where    i ≥ 0
>this program contains a function that will take a,b,m and r and calculate using the formula above and outputs a corresponding list of the ri values
- crack_PRNG.py
>this program contains a function “crack lcg(m, r1, r2, r3)”, where m is a positive integer, and r1, r2, and r3 are integers between 0 and m − 1, inclusive. This function
returns a list [a, b], where a and b are the keys for an LCG, with modulus m, which outputs r1, r2, and r3 as its first three random numbers (i.e. r1 = R1 , r2 = R2 , and r3 = R3 ).  some cases, there may not be a solution. In that case, the program will
output the list [0, 0]
# 04_Substitution_Cipher
- nomenclator.py
> this program contains two functions called ‘encryptMessage’ and ‘decryptMessage’, which implement encryption and decryption respectively with a nomenclator. These functions each take 3 parameters: ‘subKey’, which contains a key to the simple substitution cipher (which is simply a permutation of the alphabet), ‘codeBook’, a dictionary matching some dictionary words to non-letter symbols (for example, a key could be ‘uncomfortable’, and its value could be ‘*’). Given a message to encrypt, it will consider each word one at a time: If the word is in the codebook, it will replace it with its corresponding symbol. If the word is not in the codebook, it will encipher it using the simple substitution cipher.
- modified_simple_sub_hacker.py
> this program is an improved version of a substitution cipher hacker which will decrypt the message without the key. however it leaves blanks in some words. i modified it so that it will go over the message again and fill in the blanks using regular expressions
# 05_Frequency_Analysis
- file_freq_analysis.py
> this program has 2 functions:
> 1. The “freqDict” function takes as input the name of a file. It then performs frequency analysis on the entire text, using the frequency statistics from the textbook, and returns a dictionary, whose keys are the cipher characters, with the value for each key being the plaintext character it is assigned to
using frequency analysis.
>2. The “freqDecrypt” function takes two arguments, the first, f 1, being the name of a file containing a ciphertext as for the “freqDict” function, and the second, f 2, being the name of file to be produced by the “freqDecrypt” function. it then performs frequency analysis on f 1, the ciphertext file, decipher it using the
resulting mapping
- sub_eval.py
> this program contains a function named “evalFile”, which takes as input two files, f 1 and f 2. The first argument, f 1, should be a file containing a plaintext, which is assumed to have been enciphered with a simple substitution cipher, and
then deciphered by some method (such as frequency analysis). The second argument, f 2 should be a file containing this decipherment. the program will compare the two files, and return a two-element list containing the key accuracy and decipherment accuracy of the decipherment in f 2, in that order, comparing to the plaintext in f 1.
# 06_ Vigenere_Cipher
- preproc.py
> this program has a function called “antiKasiski”, which does the following pre-processing on a plain text:
• Takes two parameters: a key, and a plaintext, in that order.
• Removes all non-letter characters from the plaintext.
• Obtains the ciphertext from the Vigenere cipher with the given key.
• Repeats the following in a loop until there are no repeated sequences of length at least in the ciphertext:
Find the beginning of the the first repeated ciphertext sequence of length at least 3,
which could be useful to Kasiski examination.
Insert a random letter into the corresponding position in the plaintext.
• Returns a string containing the final ciphertext.
-  vigenereIC.py
> the function “stringIC”, which takes a string as input, and returns the IC of that string. 
> the function  “subseqIC”,  takes a string as input, containing a Vigenere ciphertext, and a key length, in that order, and returns the average IC of the subsequences of the ciphertext induced by that key length.
> the function  “keylengthIC”,  takes as input a ciphertext, and which returns a list containing the top five most likely key lengths, in order from most to least likely, according to the above heuristic (that is, it returns the five key lengths which give the highest average IC, over the subsequences they induce). the function then
tries all key lengths between 1 and 20. 






