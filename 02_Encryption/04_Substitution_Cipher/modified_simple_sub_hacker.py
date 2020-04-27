# Simple Substitution Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import re, copy, pyperclip, simpleSubCipher, wordPatterns, makeWordPatterns





LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')

def main():
    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'

    # Determine the possible valid ciphertext translations:
    print('Hacking...')
    letterMapping = hackSimpleSub(message)

    # Display the results to the user:
    print('Mapping:')
    print(letterMapping)
    print()
    print('Original ciphertext:')
    print(message)
    print()
    print('Copying hacked message to clipboard:')
    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
    hackedMessage = secondRun(hackedMessage, message)
    pyperclip.copy(hackedMessage)
    print(hackedMessage)


def getBlankCipherletterMapping():
    # Returns a dictionary value that is a blank cipherletter mapping.
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


def addLettersToMapping(letterMapping, cipherword, candidate):
    # The `letterMapping` parameter is a "cipherletter mapping" dictionary
    # value that the return value of this function starts as a copy of.
    # The `cipherword` parameter is a string value of the ciphertext word.
    # The `candidate` parameter is a possible English word that the
    # cipherword could decrypt to.

    # This function adds the letters of the candidate as potential
    # decryption letters for the cipherletters in the cipherletter
    # mapping.


    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])



def intersectMappings(mapA, mapB):
    # To intersect two maps, create a blank map, and then add only the
    # potential decryption letters if they exist in BOTH maps.
    intersectedMapping = getBlankCipherletterMapping()
    for letter in LETTERS:

        # An empty list means "any letter is possible". In this case
        # copy the other map entirely.
        if mapA[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])
        else:
            # If a letter in mapA[letter] exists in mapB[letter], add
            # that letter to intersectedMapping[letter].
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)

    return intersectedMapping


def removeSolvedLettersFromMapping(letterMapping):
    # Cipherletters in the mapping that map to only one letter are
    # "solved" and can be removed from the other letters.
    # For example, if 'A' maps to potential letters ['M', 'N'], and 'B'
    # maps to ['N'], then we know that 'B' must map to 'N', so we can
    # remove 'N' from the list of what 'A' could map to. So 'A' then maps
    # to ['M']. Note that now that 'A' maps to only one letter, we can
    # remove 'M' from the list of letters for every other
    # letter. (This is why there is a loop that keeps reducing the map.)

    loopAgain = True
    while loopAgain:
        # First assume that we will not loop again:
        loopAgain = False

        # `solvedLetters` will be a list of uppercase letters that have one
        # and only one possible mapping in `letterMapping`:
        solvedLetters = []
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])

        # If a letter is solved, than it cannot possibly be a potential
        # decryption letter for a different ciphertext letter, so we
        # should remove it from those other lists:
        for cipherletter in LETTERS:
            for s in solvedLetters:
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1:
                        # A new letter is now solved, so loop again.
                        loopAgain = True
    return letterMapping


def hackSimpleSub(message):
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
    for cipherword in cipherwordList:
        # Get a new cipherletter mapping for each ciphertext word:
        candidateMap = getBlankCipherletterMapping()

        wordPattern = makeWordPatterns.getWordPattern(cipherword)
        if wordPattern not in wordPatterns.allPatterns:
            continue # This word was not in our dictionary, so continue.

        # Add the letters of each candidate to the mapping:
        for candidate in wordPatterns.allPatterns[wordPattern]:
            addLettersToMapping(candidateMap, cipherword, candidate)

        # Intersect the new mapping with the existing intersected mapping:
        intersectedMap = intersectMappings(intersectedMap, candidateMap)

    # Remove any solved letters from the other lists:
    return removeSolvedLettersFromMapping(intersectedMap)


def decryptWithCipherletterMapping(ciphertext, letterMapping):
    # Return a string of the ciphertext decrypted with the letter mapping,
    # with any ambiguous decrypted letters replaced with an _ underscore.

    # First create a simple sub key from the letterMapping mapping:
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # If there's only one letter, add it to the key.
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    # With the key we've created, decrypt the ciphertext:
    return simpleSubCipher.decryptMessage(key, ciphertext)


#-------------------------------------------------------------------------------
#this function looks at all the words in the encrypted
#message and fills in any blanks
#returns full text
def secondRun(message, encrypted):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #open File
    file = open('dictionary.txt', 'r')
    lines = file.readlines()
    #remove newlines
    for i in range(len(lines)-1):
        lines[i] = lines[i].strip('\n')

    #go through the message and find which charactars are no being used
    #this just edits alphabet to leave unused letters for regex later
    temp = message.upper()
    for letter in temp:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, '')

    #make a dictionary to store undecreypted letters
    dict = {}
    for i in range(len(message)):
        if message[i] == '_':
            dict[encrypted[i].lower()] = ''

    #make a reg expression starting point
    reg = '['
    for char in alphabet:
        reg = reg+char
    reg = reg+']'
    lines_string = ' '.join(lines)

    #go through each word check to see if its incomplete yet. if it is incomplete
    # use regex to fix it.
    search_message = message.split(' ')
    compare = encrypted.split(' ')

    for word in search_message:
        if '_' in word:
            old_word = word
            for letter in '''!,.?-:;@#$%^&*"'()''':
                word = word.replace(letter, '')


            # come up with an expression to up in re.findall()
            expression = ''
            for i in range(len(word)):
                if word[i] == '_':
                    store_i = i
                    expression = expression+reg
                elif word[i] != '_':
                    expression = expression+word[i].upper()

            #use re.findall() to find the word
            possible_list = re.findall(expression, lines_string)
            #store the index of ddecrypted message
            the_index = search_message.index(old_word)
            #save the replaced letter
            try:
                decrypted_letter = possible_list[0][store_i]
                encrypted_letter = compare[the_index][store_i]
                if dict[encrypted_letter] == '':
                    dict[encrypted_letter] = decrypted_letter
            except:
                pass

    #put together the translated message using the dictionary
    # that was made earlier
    translated = []
    for i in message:
        translated.append(i)
    for key in dict:
        for i in range(len(encrypted)):
            if encrypted[i].lower() == key and message[i] == '_':
                translated[i] = dict[key].lower()


    translated = ''.join(translated)


    return translated
if __name__ == '__main__':
    main()
