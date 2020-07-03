import vigenereCipher


# this function calculates the IMC on a given string using the fromula from the
# assignent discriotion
def imc_calc(letters, length, ENG_LETT_FREQ):
	imc = {}
	for let in letters:
		if let not in imc:
			imc[let] = 0
		else:
			imc[let] +=1

	for i in imc:
		total = (imc[i] / length) * ENG_LETT_FREQ[i]
		imc[i] = round(total,3)
	return imc

# this function just simply totals up the IMC value of a given dictionary
def imc_total(cipher_imc):
	total = 0
	for key in cipher_imc:
		total += cipher_imc[key]
	return total

# i wasnt able to get this function to produce the proper key so i am hoping to get
# part marks for the algorithim of the code that i made
def vigenereKeySolver(ciphertext,  keylen):
	ENG_LETT_FREQ = {'E':0.127, 'T': 0.09, 'A': 0.0817, 'O': 0.0751, 'I': 0.0697, 'N': 0.0675, 'S': 0.0633, 'H': 0.0609, 'R': 0.0599, 'D': 0.0425, 'L': 0.0403, 'C': 0.0278, 'U': 0.0276, 'M': 0.0241, 'W': 0.0236, 'F': 0.0223, 'G': 0.0202, 'Y': 0.0197, 'P': 0.0193, 'B': 0.0129, 'V': 0.0098, 'K': 0.0077, 'J': 0.0015, 'X': 0.0015, 'Q': 0.0010, 'Z': 0.0007}

	key = ['']*keylen
	# loop that starts from key val 1 to end of key val
	for num in range(1, keylen+1):
		letters = []
		old_compare_val = -1
		#this loop gets every num th letter from the ciper text. ie every 2nd letter
		for i in range(num-1,len(ciphertext), num):
			letters.append(ciphertext[i])
		#try every possible letter as a key val on that sub string called letters
		for let in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			temp_decrypt = vigenereCipher.decryptMessage(let, letters)
			# make an imc functionthat will return the imc of temp_decrypt
			imc = imc_calc(temp_decrypt, len(temp_decrypt), ENG_LETT_FREQ)

			#now find the largest IMC
			new_compare_val = imc_total(imc)
			# if it is greater than the old saved one save it as the highes and
			# make the let that is being used as the key value at num in key[]
			if new_compare_val > old_compare_val:
				old_compare_val = new_compare_val
				key[num-1] = let
				# save the highest one for that letter of the key
	return key
#ciphertext = "QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCVKVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV"
#a = vigenereKeySolver(ciphertext, 5)
