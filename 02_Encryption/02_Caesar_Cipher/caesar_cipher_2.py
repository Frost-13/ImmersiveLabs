# Caesar Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip
import sys

def caesarCipher(message, key, mode):
    # Every possible symbol that can be encrypted:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Stores the encrypted/decrypted form of the message:
    translated = ''

    for i in range(len(message)):
        messageIndex = SYMBOLS.find(message[i])
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if message[i] in SYMBOLS:
            if i >= len(key):
                if mode == 'encrypt':
                    temp = i - len(key)
                    symbolIndex = SYMBOLS.find(message[temp])
                if mode == 'decrypt':
                    symbolIndex = SYMBOLS.find(translated[i-len(key)])
            else:
                symbolIndex = SYMBOLS.find(key[i])


            # Perform encryption/decryption:
            if mode == 'encrypt':
                total = messageIndex+ symbolIndex
                if total>= len(SYMBOLS):
                    total -= len(SYMBOLS)
                translated += SYMBOLS[total]

            elif mode == 'decrypt':
                total = messageIndex- symbolIndex
                if total< 0:
                    total += len(SYMBOLS)
                translated += SYMBOLS[total]

        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + message[i]




    return translated




# The string to be encrypted/decrypted:
message = sys.argv[3]
message = message.upper()
# The encryption/decryption key:
key = sys.argv[1]
key = key.strip(''':;"'!@#$%^&*(),.? <>/|{[_-+=`~]}1234567890''')
key = key.upper()

# Whether the program encrypts or decrypts:
mode = sys.argv[2]
if (mode != 'encrypt') and (mode!= 'decrypt'):
    print("INVALID MODE: please use 'encrypt' or 'decrypt'")


else:
    # Output the translated string:
    translated = caesarCipher(message, key, mode)
    print(translated)
