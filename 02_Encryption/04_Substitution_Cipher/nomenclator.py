# Simple Substitution Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip, sys, random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    plaintext = 'Lj jia ! py Lmfacjl, # jlka bmlwa sx Oawanfac lxo Lbcsm ypc jia Ylmm lxo $ jacnr.'
    #plaintext = 'At the University of Alberta, examinations take place in December and April for the Fall and Winter terms.'
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'decrypt' # Set to either 'encrypt' or 'decrypt'.
    codebook = {'university':'!', 'examination':'@', 'examinations':'#', 'WINTER':'$'}

    if not keyIsValid(myKey):
        sys.exit('There is an error in the key or symbol set.')
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, plaintext, codebook)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, plaintext, codebook)
    print('Using key %s' % (myKey))
    print('The %sed message is:' % (myMode))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('This message has been copied to the clipboard.')


def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    return keyList == lettersList


def encryptMessage(key, message, codebook):
    return translateMessage(key, message, 'encrypt', codebook)


def decryptMessage(key, message, codebook):
    return translateMessage(key, message, 'decrypt', codebook)


def translateMessage(key, message, mode, codebook):
    translated = ''
    charsA = LETTERS
    charsB = key
    #this adds the symbols from the code book for encryption purpouses
    if mode == 'encrypt':
        temp = message.split(' ')
        for i in range(len(temp)):
            for key in codebook:
                if temp[i].lower() == key.lower():
                    temp[i] = codebook[key]
                    print(temp[i])
        message = ' '.join(temp)

    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # Loop through each symbol in message:
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Symbol is not in LETTERS; just add it
            translated += symbol

    #symbols were skipped earlier so now we fill in those code book values
    if mode == 'decrypt':
        temp = translated.split(' ')
        for i in range(len(temp)):
            for key in codebook:
                if temp[i] == codebook[key]:
                    temp[i] = key
        translated = ' '.join(temp)

    return translated


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
