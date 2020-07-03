# similar to a9p1 needed this function but as a ciphertext not a file
def ngramsFreqsFromText(ciphertext, n):

    text = preprocess(ciphertext)
    grams_dict = {}
    for i in range(len(text)):
        gram = text[i:i+n]
        if gram not in grams_dict:
            grams_dict[gram] = 1
        else:
            grams_dict[gram] +=1
    denom = len(grams_dict)
    for key in grams_dict:
        numer = grams_dict[key]
        grams_dict[key] = numer/denom
    return grams_dict


def preprocess(text):
    final = ''
    for let in text:
        if let.isalpha():
            final += let.upper()
        elif let == ' ' or let == '\n':
            final += ' '
    return final

def keyScore(mapping, ciphertext, frequencies, n ):
    plaintext = ''
    # decipher the text using the given mapping
    for letter in ciphertext:
        try:
            plaintext += mapping[letter]
        except:
            plaintext += letter
    # get n gram score using similar function from a9p1
    num_dict = ngramsFreqsFromText(ciphertext, n)

    # gets the n_gram score using the given formula
    n_gram_score = 0 # total (incremental) function
    for key in num_dict:
        if key in frequencies:
            n_gram_score += num_dict[key] * frequencies[key]
        else:
            pass
    return n_gram_score
