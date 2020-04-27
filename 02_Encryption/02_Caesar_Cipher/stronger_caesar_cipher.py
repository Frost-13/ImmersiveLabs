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
        if i == 0:
            # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
            if message[i] in SYMBOLS:
                symbolIndex = SYMBOLS.find(message[i])

                # Perform encryption/decryption:
                if mode == 'encrypt':
                    translatedIndex = symbolIndex + key
                elif mode == 'decrypt':
                    translatedIndex = symbolIndex - key

                # Handle wrap-around, if needed:
                if translatedIndex >= len(SYMBOLS):
                    translatedIndex = translatedIndex - len(SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + message[i]

        else:
            if mode == 'encrypt':
                #transpose symbol
                if message[i] in SYMBOLS:
                    symbolIndex_ofCurrent = SYMBOLS.find(message[i])
                    symbolIndex_ofPrev = SYMBOLS.find(message[i-1])
                    total = symbolIndex_ofPrev+symbolIndex_ofCurrent

                    if total >=26:
                        total = total - 26
                    #add symbol to translated
                    translated = translated + SYMBOLS[total]

                else:
                    # Append the symbol without encrypting/decrypting:
                    translated = translated + message[i]

            if mode == 'decrypt':
                if message[i] in SYMBOLS:
                    symbolIndex_ofPrev = SYMBOLS.find(translated[i-1])
                    symbolIndex_ofCurrent = SYMBOLS.find(message[i])
                    total = symbolIndex_ofCurrent - symbolIndex_ofPrev

                    if total <0:
                        total = total + 26
                    #add symbol to translated
                    translated = translated + SYMBOLS[total]

                else:
                    # Append the symbol without encrypting/decrypting:
                    translated = translated + message[i]


    return translated




# The string to be encrypted/decrypted:
message = sys.argv[3]
message = message.upper()
# The encryption/decryption key:
key = int(sys.argv[1])

# Whether the program encrypts or decrypts:
mode = sys.argv[2]
if (mode != 'encrypt') and (mode!= 'decrypt'):
    print("INVALID MODE: please use 'encrypt' or 'decrypt'")


else:
    # Output the translated string:
    translated = caesarCipher(message, key, mode)
    print(translated)
