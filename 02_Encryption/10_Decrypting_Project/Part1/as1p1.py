import operator
map = [[0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0 ],[0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8 ],[0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3 ],[0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb ],[0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa ],[0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5 ],[0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf ],[0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd ],[0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc ],[0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4 ],[0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe ],[0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7 ],[0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6 ],[0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2 ],[0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9 ],[0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1 ]]
#0------------------------------------------------------------------------------
def decryption(ch,cl,kh,kl):
	table = [["8", "9", "b", "a", "e", "f", "d", "c", "4", "5", "7", "6", "2", "3", "1", "0"],
			 ["9", "b", "a", "e", "f", "d", "c", "4", "5", "7", "6", "2", "3", "1", "0", "8"],
			 ["1", "0", "8", "9", "b", "a", "e", "f", "d", "c", "4", "5", "7", "6", "2", "3"],
			 ["a", "e", "f", "d", "c", "4", "5", "7", "6", "2", "3", "1", "0", "8", "9", "b"],
			 ["e", "f", "d", "c", "4", "5", "7", "6", "2", "3", "1", "0", "8", "9", "b", "a"],
			 ["7", "6", "2", "3", "1", "0", "8", "9", "b", "a", "e", "f", "d", "c", "4", "5"],
			 ["d", "c", "4", "5", "7", "6", "2", "3", "1", "0", "8", "9", "b", "a", "e", "f"],
			 ["c", "4", "5", "7", "6", "2", "3", "1", "0", "8", "9", "b", "a", "e", "f", "d"],
			 ["4", "5", "7", "6", "2", "3", "1", "0", "8", "9", "b", "a", "e", "f", "d", "c"],
			 ["5", "7", "6", "2", "3", "1", "0", "8", "9", "b", "a", "e", "f", "d", "c", "4"],
			 ["f", "d", "c", "4", "5", "7", "6", "2", "3", "1", "0", "8", "9", "b", "a", "e"],
			 ["6", "2", "3", "1", "0", "8", "9", "b", "a", "e", "f", "d", "c", "4", "5", "7"],
			 ["2", "3", "1", "0", "8", "9", "b", "a", "e", "f", "d", "c", "4", "5", "7", "6"],
			 ["3", "1", "0", "8", "9", "b", "a", "e", "f", "d", "c", "4", "5", "7", "6", "2"],
			 ["b", "a", "e", "f", "d", "c", "4", "5", "7", "6", "2", "3", "1", "0", "8", "9"],
			 ["0", "8", "9", "b", "a", "e", "f", "d", "c", "4", "5", "7", "6", "2", "3", "1"]]

	for x in range(0, len(table)):
		if ch == table[x][int(kl,16)]:
			ph = x
	for x in range(0, len(table)):
		if cl == table[x][int(kh,16)]:
			pl = x
	letter = str(hex(ph).split('x')[1])+str(hex(pl).split('x')[1])
	if int(letter, 16) == 10:
		return str(chr(int(letter,16)))
	elif int(letter,16)>=32 and int(letter,16) <=126:
		return str(chr(int(letter,16)))

#-------------------------------------------------------------------------------
#open the file
filename = 'modciph1'
f= open(filename, 'r')
#-------------------------------------------------------------------------------
#this chunck just saves bytes into a list named byte_list

#save all numbers/letters into one big string
big_string = ''
for line in f:
	big_string= big_string + line

#remove \n
big_string = big_string.replace('\n', '')
#print(big_string)

#save all of them into a list in groups of 2's
byte_list = []
for i in range(0, len(big_string)-1, 2):
	if i == len(big_string)-1:
		pass
	temp = big_string[i] +big_string[i+1]
	byte_list.append(temp)

#print(len(byte_list))
#print(byte_list)
#-------------------------------------------------------------------------------
#this chunk will find the key length....sortta
feqlist = []
for i in range(1, 100):
	temp = 0
	for j in range(len(byte_list)-1):
		try:
			if byte_list[j] == byte_list[j+i]:
				temp +=1
		except:
			pass
	feqlist.append(temp)
print(feqlist)
key_len = int(input("what do you think the key length is based on the given list?: ")) #can we make this automatic??

#-------------------------------------------------------------------------------
# this chunck tries to find printable ascii in the key length

#for i in range(len(byte_list)):
key = []
for length in range(key_len):
	specific_array = []
	i = length
	while i <= len(byte_list):
		try:
			specific_array.append(byte_list[i])
		except:
			bs = 0
		i+=key_len

	#print('\n\n\n')
	#print(specific_array)
	pair_list = []
	#print(len(specific_array))
	for decimal in range(32, 127):
		for i in specific_array:

			ch = i[0]
			cl = i[1]
			kh = str(hex(decimal)[2])
			kl = str(hex(decimal)[3])
			a = decryption(ch,cl,kh,kl)
			if a != None:
				#print(decimal,a)
				pair_list.append(decimal)
			else:
				break

		#print('#_________________________')
		#print(pair_list)
	#my key guess in dec not hex: 95 76 105 116 70 117 84 95

	#-------------------------------------
	#freqency analysis on pair_list
	freq = {}
	for i in pair_list:
		if i not in freq:
			freq[i] = 1
		else:
			freq[i]+=1
	#print("\n\n\n\n")
	sorted_x = sorted(freq.items(), key=operator.itemgetter(1)) #https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
	temp_hex = hex(sorted_x[-1][0])
	temp_hex = str(temp_hex[2])+str(temp_hex[3])
	temp_hex = temp_hex.upper()
	key.append(temp_hex)
	print('this is hex: ', temp_hex)
#key = ['5F', '4C', '69', '74', '46', '75', '54', '5F']
i = 0
counter = 0
while i < len(byte_list):
	ch = byte_list[i][0]
	cl = byte_list[i][1]
	kh = key[counter][0]
	kl = key[counter][1]
	char = decryption(ch,cl,kh,kl)
	print(char, end ='')
	counter+=1
	i+=1
	if counter >= key_len:
		counter = 0
