import math

# calculates the Euclidean gcd to be used in the modular inverse function
# got this from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

#calculates the modular inverse of a mod m
# got this from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m
# question 1 function given n and e it will return p and q and d
def finitePrimeHack(t,n,e):
	return_list = []
	p,q =0,0
	t = n # i found that it works best when i set t to be the size of n so that it doesnt run out of numbers
	for x in range(2, int(math.sqrt(t) + 1)):
		if t % x == 0:
			pass
		if (n/x).is_integer():
			if x >= n/x:
				p,q = int(n/x), x
			elif x <= n/x:
				q,p = int(n/x), x

	return_list.append(p)
	return_list.append(q)
	temp = (p-1)*(q-1)
	return_list.append(modinv(e,temp))
	return return_list

# a =finitePrimeHack(100,493,5)
# print('test key is:')
# print(a)
#
# a =finitePrimeHack(567607865171,567607865171,829733)
# print('key 2 is:')
# print(a)
# a =finitePrimeHack(392069431823,392069431823,797539)
# print('key 3 is:')
# print(a)
# a =finitePrimeHack(1071440448707,1071440448707,775385)
# print('key 4 is:')
# print(a)
# a =finitePrimeHack(474233311109,474233311109,946273)
# print('key 5 is:')
# print(a)
