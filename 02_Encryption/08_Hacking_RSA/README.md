# 08_Hacking_RSA
- hackRSA.py
> The security of the RSA cipher depends on there being an infinitely many prime numbers:
generating large prime numbers is, as far as we know, far easier than factoring the products of
these primes, meaning that, no matter how fast computers become, we will always be able to
find products of larger prime numbers than potential cryptanalysts can factor. Therefore we can make a function “finitePrimeHack” that can generate prime numbers and bruteforce a solution. This function will take 3 parameters, in this order: a threshold [t], and n and e, which together form a public RSA key. The function will assume that there are no prime numbers larger than t. It will then discover the values of p and q, compute the value of d
(the inverse of e modulo (p − 1) × (q − 1)) and returns a list containing p, q, and d in that order.
Note: p ≤ q (that is, the smaller of the two primes should
come first; this constraint is simply to fix the ordering of primes in found solutions).
