import a9p2, decrypt
def bestSuccessor(mapping, ciphertext, ngram_score, frequencies, n):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    m_prime = {}
    # this part is the loop that re aranges the mapping
    for i in range(len(letters)):
        m_prime = mapping
        for j in range(i+1, len(letters)):
            try:
                temp = m_prime[letters[i]]
                m_prime[letters[i]] = mapping[letters[j]]
                m_prime[letters[j]] = temp
            except:
                pass
            # this part checks this new mappings n gram score if it is higer
            # then it is the new mapping. ties are broken by older one will win
            new_ngram_score = a9p2.keyScore(m_prime, ciphertext, frequencies, n)
            if new_ngram_score > ngram_score:
                ngram_score = new_ngram_score
                final_mapping = m_prime

    return final_mapping
