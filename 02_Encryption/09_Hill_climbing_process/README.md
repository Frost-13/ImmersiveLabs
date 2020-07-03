# 09_Hill_Climbing_Process

- ngramsFreqsFromFile.py
> this program contains a function called ngramsFreqsFromFile(textFile, n), which takes as input a path to a text file, and the n-gram variable n. It returns a dictionary in which each key is a character n-gram, represented as a single string, and the value of a key is the relative frequency of that n-gram in that text file (the number of times that n-gram occurs, divided by the total number of character n-grams in the given file).

- ngramsFreqsFromText.py
> For mapping I used a Python dictionary which maps the set of 27 characters to itself bijectively (so the mapping is exactly one-to-one, with 27 unique keys and 27 unique values), with the constraint that ‘space’ is always mapped to itself. Given a mapping, a ciphertext, and an n-gram frequency dictionary, the n-gram score of the key will then be computed as follows:
• 1. Decipher the ciphertext using the mapping, by mapping each ciphertext character to the
value it has in that key.
• 2. For a given n-gram b, let c(b) be the number of times it occurs in the decipherment, and
let f (b) be its relative frequency in the given dictionary.
• 3. Letting B be the set of all n-grams which occur in the decipherment, the score of the provided mapping is:  ∑ c(b) · f (b)
•the function keyScore( mapping, ciphertext, frequencies, n ),  returns the n-gram score, as a floating-point number, computed given that mapping, ciphertext (given as a string), an n-gram frequency dictionary(such as is returned by the ngramsFreqsFromFile function), and the n-gram parameter n.

- bestSuccessor.py
>In this program the function called bestSuccessor(mapping, ciphertext, frequencies, n ), which computes the n-gram score of each possible successor of the given mapping, given the ciphertext (as a string), an n-gram frequency dictionary, and the value of n. If any such successor has a higher score than the given mapping, the function will return the successor with the highest such score. Otherwise, it will return the original mapping.

> • Given a mapping m, we can create a new mapping, call it m0 , by choosing two keys in the dictionary that is m, and exchanging their values. For example, if m maps ‘A’ to ‘X’ and ‘B’ to ‘Y’, one such “swap” would have m0 be identical to m, except that m0 maps ‘A’ to ‘Y’ and ‘B’ to ‘X’. Since a mapping has 26 keys which are not fixed (recall that any mapping must map space to itself), the total number of swaps is equal to 325 (there are 25 characters to swap ‘A’ with, 24 for ‘B’, and so on). For a mapping m, let Sm be the set of all mappings which can be created by swapping two values in m in this way. We will call these mappings the successors of m. Of course, some successor of m might have a higher score than m itself – that is, in terms of n-gram frequencies, it might be a better mapping.

- breakSub.py
>This program contains a function called breakSub( ciphertext, textFile, n ). Initially, this function will create a mapping based on frequency analysis (so, the ith most frequent cipher character is mapped to the ith most frequent English character). It will then repeatedly apply the previously made bestSuccessor function, with the given ciphertext, an n-gram frequency dictionary derived
from the given text file, and n-gram size n, halting when that function simply returns the same mapping it was given (that is, when a better mapping cannot be found through any swap). Once this happens, the function will return a string containing the decipherment produced using that mapping.

> • This strategy of repeatedly replacing the current solution with the best of a set of successor solutions until no further improvement is possible is a strategy called hill climbing.
