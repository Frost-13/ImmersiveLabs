def leet_that(word):
	    leet = (
	                (('are', 'Are'), 'r'),
	                (('ate', 'Ate'), '8'),
	                (('that', 'That'), 'tht'),
	        (('you', 'You'), 'j00'),
	        (('o', 'O'), '0'),
	        (('i', 'I'), '1'),
	        (('e', 'E'), '3'),
	        (('s', 'S'), '5'),
	        (('a', 'A'), '4'),
	        (('t', 'T'), '7'),
	        )
	    for symbols, replaceStr in leet:
	        for symbol in symbols:
	            word = word.replace(symbol, replaceStr)
	    return word

words = open('words.txt','r')
leeted = open('leeted.txt', 'w')

for line in words:
    for word in line.split():
        leeted.write(leet_that(word) + "\n")
