# Transposition Cipher Decryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import math, pyperclip

def main():
    myMessage = 'XOV EK HLYR NUCO HEEEWADCRETL CEEOACT KD'
    myKey =  [2,4,6,8,10,1,3,5,7,9]
    plaintext = decryptMessage(myKey, myMessage)

    # Print with a | ("pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfRows = int(math.ceil(len(message) / float(len(key))))
    #print(numOfRows)
    # The number of "rows" in our grid will need:
    numOfColumns= len(key)
    plaintext = [['' for x in range(numOfColumns)] for y in range(numOfRows)]
    #print(plaintext)
    counter = 0

    #this loop reads through the encripted string and takes sections that are as
    #long as the number of columns. using the key it will put it in
    #its proper place in a list
    for i in key:
        end = counter+numOfRows
        temp_ltrs = message[counter:end]

        for j in range(numOfRows):
            #print(len(temp_ltrs))
            #print(j)
            plaintext[j][i-1] = temp_ltrs[j]
        #print(plaintext)

        counter += numOfRows

    final = ''
    for i in plaintext:
        for j in i:
            final += j
    return final



# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
