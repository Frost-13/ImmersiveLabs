def decrypt(mapping, ciphertext):
    plain = ''
    for i in ciphertext:
        if i == ' ':
            plain += ' '
        else:
            try:
                plain += mapping[i]
            except:
                pass
    return plain
