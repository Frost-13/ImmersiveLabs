def evalFile(f1, f2):
    plaintext_file = open(f1, 'r')
    encrypted_file = open(f2, 'r')

    plain_lines = plaintext_file.readlines()
    encrypted_lines = encrypted_file.readlines()

    plain_letters =[]
    for line in plain_lines:
        for char in line:
            if char.isalpha():
                plain_letters.append(char)

    encrypted_letters = []
    for line in encrypted_lines:
        for char in line:
            if char.isalpha():
                encrypted_letters.append(char.lower())
    # print(len(plain_letters))
    # print(len(encrypted_letters))
    keeper_list = []
    total = []
    counter = 0
    counter2 =0
    for i in range(len(plain_letters)-1):
        if plain_letters[i] not in total:
            total.append(plain_letters[i])

        if plain_letters[i] == encrypted_letters[i]:
            counter +=1
            if plain_letters[i] not in keeper_list:
                keeper_list.append(plain_letters[i])
                counter2 +=1

    return [counter2/ len(total), counter/len(plain_letters)]
