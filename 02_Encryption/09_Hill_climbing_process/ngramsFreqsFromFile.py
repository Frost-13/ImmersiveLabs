def preprocess(text):
    final = ''
    for let in text:
        if let.isalpha():
            final += let.upper()
        elif let == ' ' or let == '\n':
            final += ' '
    return final

def ngramsFreqsFromFile(textFile, n):
    #read the file
    f = open(textFile, 'r')
    temp_text = ''
    # make the lines into one string
    for line in f:
        temp_text +=line
    # call preprocess to remove all char that is not a space or letter
    # also makes letters upper case
    text = preprocess(temp_text)
    grams_dict = {}

    # gets all the n grams based on what n was
    for i in range(len(text)):
        gram = text[i:i+n]
        if gram not in grams_dict:
            grams_dict[gram] = 1
        else:
            grams_dict[gram] +=1

    denom = len(grams_dict)
    # modifiy the values in the dict to match the specification in the discription
    # ' number of times that n-gram occurs, divided by the total number of character n-grams in the given file' 
    for key in grams_dict:
        numer = grams_dict[key]
        grams_dict[key] = numer/denom
    return grams_dict
