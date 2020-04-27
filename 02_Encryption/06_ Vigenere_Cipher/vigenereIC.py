import vigenereHacker, operator
#takes a string and returns the IC value
def stringIC(string):
    # create a dictonary that saves the number of occurances for each number
    # in string
    dict = {}
    for letter in string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1

    total = 0
    # use the given IC formula on the Dictionary
    for i in dict:
        num = dict[i] *(dict[i] - 1)
        total += num

    denom = len(string) * (len(string) - 1)

    return total / denom


def subseqIC(string, key):
    total = 0

    #go through the string n number of times where n is the length of the key
    # this loop takes all letters at the i th index and saves them.
    # it then calculates the IC and saves it to a total
    for i in range(1, key+1):
        letters =  vigenereHacker.getNthSubkeysLetters(i, key, string)

        total += stringIC(letters)

    # average out total
    final = total / key
    return final

def keylengthIC(ciphertext):
    key_dict = {}
    # this loop goes through key lengths 1 -20 and saves it in a dict
    # where the key is the key length
    # and the value is the IC value
    for key in range(1,21):
        avg = subseqIC(ciphertext, key)
        key_dict[key] = avg

    # sort the dict from smallest to largest
    sorted_dict = sorted(key_dict.items(), key=operator.itemgetter(1))
    #print(sorted_dict)

    # save the largest 5
    temp_keys = sorted_dict[-5:]
    #print(temp_keys)
    keys = [0,0,0,0,0]
    index = 4
    # save them in the final list called keys but puting them in backwards
    for item in temp_keys:
        keys[index] = item[0]
        index -=1
    return keys

#print(stringIC('ABCD'))
#print(subseqIC('PPQCAXQVEKGYBNKMAZUHKNHONMFRAZCBELGRKUGDDMA', 5))
#print(keylengthIC('PPQCAXQVEKGYBNKMAZUHKNHONMFRAZCBELGRKUGDDMA'))
