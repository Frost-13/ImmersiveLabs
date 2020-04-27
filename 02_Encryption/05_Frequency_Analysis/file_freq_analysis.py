import operator
def freqDict(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    dict = {}
    for line in lines:
        for char in line:
            if char.isalpha():
                if char in dict:
                    dict[char] += 1
                else:
                    dict[char] = 1
    #https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
    #print(sorted_dict)
    j = 0
    for i in range(len(sorted_dict)-1, 0, -1):
        encrypted_letter = sorted_dict[i][0]
        decrypted_letter = ETAOIN[j]

        dict[encrypted_letter] = decrypted_letter
        j+=1
    #print(dict)
    return dict


    '''The “freqDecrypt” function should take two arguments, the first, f 1, being the name of a
file containing a ciphertext as for the “freqDict” function, and the second, f 2, being the name
of file to be produced by the “freqDecrypt” function (that is, it is a file your code will create).
Your code should perform frequency analysis on f 1, the ciphertext file, decipher it using the
resulting mapping (i.e. mapping all instances of the most frequent cipher character to ‘E’, and
so on; you should call your “freqDict” function to get the mapping), and print the resulting
decipherment to f 2, the specified output file-name.'''
def freqDecrypt(f1, f2):
    encrypted_file = open(f1, 'r')
    decrypted_file = open(f2, 'w')
    lines = encrypted_file.readlines()
    frequency_dict = freqDict(f1)
    text = ' '
    for line in lines:
        for char in line:
            if char in frequency_dict:
                text = text + str(frequency_dict[char])
            else:
                text = text+ char
    text = text + '\n'

    decrypted_file.write(text)
