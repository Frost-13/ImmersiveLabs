import operator, a9p1, a9p2, a9p3, decrypt

# gets the char frequencies from the ciphertext
def get_freq(ciphertext):

    ciph_dict = {}
    for let in ciphertext:

        if let.isalpha():
            let = let.upper()
            if let in ciph_dict:
                ciph_dict[let] +=1
            else:
                ciph_dict[let] = 1
    sorted_dict = sorted(ciph_dict.items(), key=operator.itemgetter(1))
    frq = ''
    for i in range(len(sorted_dict)-1, 0, -1):
        frq += sorted_dict[i][0]
    return frq

def  breakSub( ciphertext, textFile, n):
    #get the mapping
    engl_freq = 'ETAOINSRHDLUCMFYWGPBVKXQJZ'
    cipher_freq = get_freq(ciphertext)
    mapping ={}
    for i in range(len(cipher_freq)):
        try:
            mapping[cipher_freq[i]] = engl_freq[i]
        except:
            mapping[cipher_freq[i]] = ''
    # calls on the functions from past questions to decrypt the ciphertext
    # using the hill climbing method
    frequencies = a9p1.ngramsFreqsFromFile(textFile, n)
    ngram_score = a9p2.keyScore(mapping, ciphertext, frequencies, n)
    new_mapping = a9p3.bestSuccessor(mapping, ciphertext, ngram_score, frequencies, n)
    plain = decrypt.decrypt(new_mapping, ciphertext)
    return plain
