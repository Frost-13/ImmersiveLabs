# 07_Vigenere_Hacker
- vigenereIMC.py
>IMC(t) =∑  t(i) · e(i)
> this program containins a function named vigenereKeySolver, that takes two arguments: ciphertext, which is a string containing a ciphertext created using the Vigenere cipher, and keylength, which is an integer giving the length of the key used to do so. vigenereKeySolver function will return an iterator
that yields string guesses of the key used to encipher the ciphertext. These guesses should be
iterated be in the order of their likelihood of being correct. The returned iterator will terminate when it has yielded all possible keys.
- vigenereHacker.py
>using several tools created earlier to aid in the hacking of the Vigenere cipher, we can now attempt to hack a vigenere message. it will try to guess different keys and decrypt it with these best guess keys and use a detect English on it, the one with the highest result is used.
