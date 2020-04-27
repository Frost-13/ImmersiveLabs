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






