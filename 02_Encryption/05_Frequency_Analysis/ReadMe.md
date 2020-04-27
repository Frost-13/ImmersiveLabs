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
