import operator
import string
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
	return letter

#-------------------------------------------------------------------------------
#open the file
filename = 'modciph2'
f= open(filename, 'r')

#-------------------------------------------------------------------------------
#this chunck just saves bytes into a list named byte_list
#save all numbers/letters into one big string
big_string = ''
for line in f:
	big_string= big_string + line

#remove \n
big_string = big_string.replace('\n', '')

byte_list = []
for i in range(0, len(big_string)-1, 2):
	if i == len(big_string)-1:
		pass
	temp = big_string[i] +big_string[i+1]
	byte_list.append(temp)


#-------------------------------------------------------------------------------
#Getting key length
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
print(feqlist,"\n")

key_len = int(input("What do you think the key length is based on the given list?: "))
key_len = 40

#-------------------------------------------------------------------------------

possibility= open("possibility.txt","w")

first_four = []
for i in range(0,4):
	first_four.append(byte_list[i])


# finding every single possiblity of decrypted form of the first four
i = 0

for first in range(32, 127):
	first_ch = first_four[0][0]
	first_cl = first_four[0][1]
	first_kh = str(hex(first)[2])
	first_kl = str(hex(first)[3])
	first_decrypted = decryption(first_ch, first_cl, first_kh, first_kl)
	if first_decrypted.isprintable():
		for second in range(32,127):
			second_ch = first_four[1][0]
			second_cl = first_four[1][1]
			second_kh = str(hex(second)[2])
			second_kl = str(hex(second)[3])
			second_decrypted = decryption(second_ch, second_cl, second_kh, second_kl)
			if second_decrypted.isprintable():
				for third in range(32,127):
					third_ch = first_four[2][0]
					third_cl = first_four[2][1]
					third_kh = str(hex(third)[2])
					third_kl = str(hex(third)[3])
					third_decrypted = decryption(third_ch, third_cl, third_kh, third_kl)
					if third_decrypted.isprintable():
						for fourth in range(32, 127):
							fourth_ch = first_four[3][0]
							fourth_cl = first_four[3][1]
							fourth_kh = str(hex(fourth)[2])
							fourth_kl = str(hex(fourth)[3])
							fourth_decrypted = decryption(fourth_ch, fourth_cl, fourth_kh, fourth_kl)
							if fourth_decrypted.isprintable():
								# print(i)
								i+=1
								possibility.write("%s %s %s %s | %s %s %s %s\n" % (first_decrypted, second_decrypted, third_decrypted, fourth_decrypted,first, second, third, fourth))

# file signature possibility
# 50 4b 03 04 = zip 91 57 53 119
# [95w
#
# ef bb bf = UTF-8 encoded unicode byte order mark, commonly seen in text file 99 50 122
# c2z
#
# FF FB = MPEG-1 Layer 3 file without an ID3 tag or with an ID3V1 tag 102 62
# f>
#
# 4e 45 53 1a = Nintendo Entertainment System ROM file 49 73 59 102
# 1I;B
#
# 1f 8b = GZIP compressed file 100 53
# d5
#
# 43 57 53 = flash .swf 33 115 59
# !s;

#--------------------------------------------------------------------------------
#50 4b 03 04 = zip 91 57 53 119
#[95w

#finding the frequency for the first 4 ch of the key
findx = []
sindx = []
tindx = []
foindx = []

f = 0
s = 1
t = 2
fo = 3
while f <= len(byte_list):
	findx.append(byte_list[f])
	f+=key_len

while s <= len(byte_list):
	sindx.append(byte_list[s])
	s+=key_len

while t <= len(byte_list):
	tindx.append(byte_list[t])
	t+=key_len

while fo <= len(byte_list):
	foindx.append(byte_list[fo])
	fo+=key_len

ffreq = {}
decimal = 91
for i in findx:
	ch = i[0]
	cl = i[1]
	kh = str(hex(decimal)[2])
	kl = str(hex(decimal)[3])
	a = decryption(ch,cl,kh,kl)
	if a not in ffreq:
		ffreq[a] = 1
	else:
		ffreq[a]+=1

ffreq = sorted(ffreq.items(), key=operator.itemgetter(1), reverse = True)
fhighest= ffreq[0][0]

decimal = 57
sfreq = {}
for i in sindx:
	ch = i[0]
	cl = i[1]
	kh = str(hex(decimal)[2])
	kl = str(hex(decimal)[3])
	a = decryption(ch,cl,kh,kl)
	if a not in sfreq:
		sfreq[a] = 1
	else:
		sfreq[a]+=1

sfreq = sorted(sfreq.items(), key=operator.itemgetter(1), reverse= True)
shighest= sfreq[0][0]

decimal = 53
tfreq = {}
for i in tindx:
	ch = i[0]
	cl = i[1]
	kh = str(hex(decimal)[2])
	kl = str(hex(decimal)[3])
	a = decryption(ch,cl,kh,kl)
	if a not in tfreq:
		tfreq[a] = 1
	else:
		tfreq[a]+=1

tfreq = sorted(tfreq.items(), key=operator.itemgetter(1), reverse= True)
thighest= tfreq[0][0]


decimal = 119
fofreq = {}
for i in foindx:
	ch = i[0]
	cl = i[1]
	kh = str(hex(decimal)[2])
	kl = str(hex(decimal)[3])
	a = decryption(ch,cl,kh,kl)
	if a not in fofreq:
		fofreq[a] = 1
	else:
		fofreq[a]+=1

fofreq = sorted(fofreq.items(), key=operator.itemgetter(1), reverse= True)
fohighest= fofreq[0][0]


#-------------------------------------------------------------------------------
#finding the key ch for the rest of the key

possible_ch= {0:["91"], 1:["57"], 2:["53"], 3:["119"]}

for length in range(4,key_len):
	chindx= length
	specific_array = []
	i = length
	while i < len(byte_list):
		specific_array.append(byte_list[i])
		i+=key_len
	value_counter = 0
	for decimal in range(32, 127):
		freq = {}
		for i in specific_array:
			ch = i[0]
			cl = i[1]
			kh = str(hex(decimal)[2])
			kl = str(hex(decimal)[3])
			a = decryption(ch,cl,kh,kl)
			if a not in freq:
				freq[a] = 1
			else:
				freq[a]+=1

		freq = sorted(freq.items(), key=operator.itemgetter(1), reverse= True)

		if freq[0][0] == fhighest or freq[0][0] == shighest or freq[0][0] == thighest or freq[0][0] == fhighest:
			possible_ch.setdefault(length,[]).append(decimal)

print(possible_ch,"\n")

decrypted_file = open("decrypted_file.zip", "wb")

key = ["91", "57", "53", "119" ]

ch_indx = 4
choice = input("Press 1 to change couple key characters\nPress 2 to change all key charactes\n")

while choice != '1' and choice  != '2':
	choice = input("Need to choose 1 or 2:")

while choice == '1':
	while ch_indx < len(possible_ch):
		print(ch_indx)
		key.insert(ch_indx,possible_ch.get(ch_indx)[0])
		ch_indx+=1

	print("All the other key characters will use the key characters with 20 as the highest frequency")
	keep_going = 'Y'
	while keep_going == 'Y':

		print(key)
		cindx = input("Choose which key index you would like to change; (4-39):")
		print("Possible keys in decimal: ", possible_ch[int(cindx)])
		key_chosen = input("Choose a key ch in decimal: ")
		key[int(cindx)] = key_chosen
		keep_going = input("Y to switch more key characters or N to stop: ")
	if keep_going == 'N':
		break
if choice== '2':
	while ch_indx < len(possible_ch):

		print("key: ",key,"\n")
		if len(possible_ch.get(ch_indx)) != 1:
			print(possible_ch.get(ch_indx))
			choice = input("choose a ch from the list: ")
			key.insert(ch_indx, choice)
			print("\n")
		else:
			print("Only one choice", possible_ch.get(ch_indx)[0])
			key.insert(ch_indx,possible_ch.get(ch_indx)[0])
			print("\n")
		ch_indx+=1


print("\n",key,"\n")

#correct key
#key = ["91", "57", "53", "119", "74", "76", "52", "80", "105", "69",
		# "41", "55", "117", "94", "80", "45", "81", "40", "37" , "94",
		# "45", "95", "50", "53", "52", "100", "104", "49", "70","64" ,
		# "64","110", "110", "69", "49", "50", "56", "101", "82", "111" ]

decrypted_file = open("decrypted_file.zip", "wb")
i = 0
counter = 0
while i < len(byte_list):
	ch = byte_list[i][0]
	cl = byte_list[i][1]
	key_value = hex(int(key[counter]))
	kh = key_value[2]
	kl = key_value[3]
	char = decryption(ch,cl,kh,kl)
	x= bytes.fromhex(char)
	decrypted_file.write(x)
	counter+=1
	i+=1
	if counter >= key_len:
		counter = 0
