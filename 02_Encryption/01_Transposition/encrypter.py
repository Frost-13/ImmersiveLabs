# Transposition Cipher Encryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip

def main():
    myMessage = 'CIPHERS ARE FUN'
    myKey = [2,4,1,5,3]

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message.
    print(ciphertext + '|')

    # Copy the encrypted string in ciphertext to the clipboard.
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):


    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * len(key)
    #print(ciphertext)

    # Loop through each column in ciphertext.
    for column in range(len(key)):
        #print(column)
        currentIndex = column

        # Keep looping until currentIndex goes past the message length.
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list.
            ciphertext[column] += message[currentIndex]

            # move currentIndex over
            currentIndex += len(key)

    # use the key to put the columns in jumbled order
    final_cipher_text = []
    for i in key:
        final_cipher_text += ciphertext[i-1]

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(final_cipher_text)


# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
