import re

filename = "can_writers.txt"
fp= open(filename, "r")
filename2 = 'nospacecanno.txt'
fp2= open(filename2, "w")
lines = fp.readlines()


for line in lines:
    line = re.sub(r"\s+", '', line)
    fp2.write(line)
    fp2.write("\n")
fp.close()
fp2.close()