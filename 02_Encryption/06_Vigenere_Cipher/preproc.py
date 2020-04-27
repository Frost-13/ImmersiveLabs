import vigenereCipher, vigenereHacker, random
# this function takes a given string and strips it of all non letter chars
# also coverts all lower case letters to upper case
def alpha_only(plaintext):
    final = ''
    for char in plaintext:
        if char.isalpha() == True:
            final += char.upper()
    return final

#this function insert was retrived from:
#https://stackoverflow.com/questions/4022827/insert-some-string-into-given-string-at-given-index-in-python
#by Sim Mak
# this function inserts a sting in the middle of another given sting at a
# certian position
def insert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

def antiKasiski(key, plaintext):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = alpha_only(plaintext)
    encrypted = vigenereCipher.encryptMessage(key, plaintext)

    # get the repeating sequnces
    a = vigenereHacker.findRepeatSequencesSpacings(encrypted)

    #saving this string for later to be used in insert function
    final = encrypted

#this loop goes through the repeated sequnces and for every time in the string it
# appers that isnt the first time it will insert a random letter between it
    for key in a:
        length = len(encrypted) - len(key)
        x = len(key)
        count =0
        for i in range(0, length):
            cluster = encrypted[i:i+x]
            if cluster == key:
                if count == 0:
                    count +=1
                else:
                    # puts rand letter into the string
                    int = random.randint(0, 25)
                    letter = alphabet[int]

                    final = insert(final, letter, i)
    return final

#print(antiKasiski('WICK', 'THOSEPOLICEOFFICERSOFFEREDHERARIDEHOMETHEYTELLTHEMAJOKETHOSEBARBERSLENTHERALOTOFMONEY'))
