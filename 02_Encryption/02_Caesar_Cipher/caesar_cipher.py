# Caesar Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip
import sys

def caesarCipher(message, key, mode):
    # Every possible symbol that can be encrypted:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Stores the encrypted/decrypted form of the message:
    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

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
            translated = translated + symbol
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
