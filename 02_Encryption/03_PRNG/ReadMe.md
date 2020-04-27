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
