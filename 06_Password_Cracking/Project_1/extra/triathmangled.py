import re
filename = 'triathlete_dict.txt'
fp= open(filename, "r")
filename2 = 'trimangle.txt'
fp2= open(filename2, "w")
lines = fp.readlines()

#(l,l)
#(l,u)
#(l,f)
#(u,l)
#(u,u)
#(u,f)
#(f,l)
#(f,u)
#(f,f)

for line in lines:
    #erasing space at the end of the line
    line = line[:-1]
    #split the last name and first name
    name = re.split(" ", line)
    
    #all letter lower
    firstnamelow= name[0].lower()
    secondnamelow= name[1].lower()
    
    #all letter upper
    firstnameup= name[0].upper()
    secondnameup= name[1].upper()
  
    #(l,l)
    #mangling with $
    fp2.write(firstnamelow)
    fp2.write("$")
    fp2.write(secondnamelow)
    fp2.write("\n")
    #mangling with %
    fp2.write(firstnamelow)
    fp2.write("%")
    fp2.write(secondnamelow)
    fp2.write("\n")
    #mangling with *
    fp2.write(firstnamelow)
    fp2.write("*")
    fp2.write(secondnamelow)
    fp2.write("\n")
    #mangling with _
    fp2.write(firstnamelow)
    fp2.write("_")
    fp2.write(secondnamelow)
    fp2.write("\n")
    
    #(l,u)
    #mangling with $
    fp2.write(firstnamelow)
    fp2.write("$")
    fp2.write(secondnameup)
    fp2.write("\n")
    #mangling with %
    fp2.write(firstnamelow)
    fp2.write("%")
    fp2.write(secondnameup)
    fp2.write("\n")
    #mangling with *
    fp2.write(firstnamelow)
    fp2.write("*")
    fp2.write(secondnameup)
    fp2.write("\n")
    #mangling with _
    fp2.write(firstnamelow)
    fp2.write("_")
    fp2.write(secondnameup)
    fp2.write("\n")
    
    #(l,f)
    #mangling with $
    fp2.write(firstnamelow)
    fp2.write("$")
    fp2.write(name[1])
    fp2.write("\n")
    #mangling with %
    fp2.write(firstnamelow)
    fp2.write("%")
    fp2.write(name[1])
    fp2.write("\n")
    #mangling with *
    fp2.write(firstnamelow)
    fp2.write("*")
    fp2.write(name[1])
    fp2.write("\n")
    #mangling with _
    fp2.write(firstnamelow)
    fp2.write("_")
    fp2.write(name[1])
    fp2.write("\n")

    #(u,l)
    #mangling with $
    fp2.write(firstnameup)
    fp2.write("$")
    fp2.write(secondnamelow)
    fp2.write("\n")
    #mangling with %
    fp2.write(firstnameup)
    fp2.write("%")
    fp2.write(secondnamelow)
    fp2.write("\n")
    #mangling with *
    fp2.write(firstnameup)
    fp2.write("*")
    fp2.write(secondnamelow)
    fp2.write("\n")
    #mangling with _
    fp2.write(firstnameup)
    fp2.write("_")
    fp2.write(secondnamelow)
    fp2.write("\n")

    #(u,u)
    #mangling with $
    fp2.write(firstnameup)
    fp2.write("$")
    fp2.write(secondnameup)
    fp2.write("\n")
    #mangling with %
    fp2.write(firstnameup)
    fp2.write("%")
    fp2.write(secondnameup)
    fp2.write("\n")
    #mangling with *
    fp2.write(firstnameup)
    fp2.write("*")
    fp2.write(secondnameup)
    fp2.write("\n")
    #mangling with _
    fp2.write(firstnameup)
    fp2.write("_")
    fp2.write(secondnameup)
    fp2.write("\n")

    #(u,f)
    #mangling with $
    fp2.write(firstnameup)
    fp2.write("$")
    fp2.write(name[1])
    fp2.write("\n")
    #mangling with %
    fp2.write(firstnameup)
    fp2.write("%")
    fp2.write(name[1])
    fp2.write("\n")
    #mangling with *
    fp2.write(firstnameup)
    fp2.write("*")
    fp2.write(name[1])
    fp2.write("\n")
    #mangling with _
    fp2.write(firstnameup)
    fp2.write("_")
    fp2.write(name[1])
    fp2.write("\n")

    #(f,l)
    #mangling with $
    fp2.write(name[0])
    fp2.write("$")
    fp2.write(secondnamelow)
    fp2.write("\n")
    #mangling with %
    fp2.write(name[0])
    fp2.write("%")
    fp2.write(secondnamelow)
    fp2.write("\n")
    #mangling with *
    fp2.write(name[0])
    fp2.write("*")
    fp2.write(secondnamelow)
    fp2.write("\n")
    #mangling with _
    fp2.write(name[0])
    fp2.write("_")
    fp2.write(secondnamelow)
    fp2.write("\n")

    #(f,u)
    #mangling with $
    fp2.write(name[0])
    fp2.write("$")
    fp2.write(secondnameup)
    fp2.write("\n")
    #mangling with %
    fp2.write(name[0])
    fp2.write("%")
    fp2.write(secondnameup)
    fp2.write("\n")
    #mangling with *
    fp2.write(name[0])
    fp2.write("*")
    fp2.write(secondnameup)
    fp2.write("\n")
    #mangling with _
    fp2.write(name[0])
    fp2.write("_")
    fp2.write(secondnameup)
    fp2.write("\n")

    #(f,f)
    #mangling with $
    fp2.write(name[0])
    fp2.write("$")
    fp2.write(name[1])
    fp2.write("\n")
    #mangling with %
    fp2.write(name[0])
    fp2.write("%")
    fp2.write(name[1])
    fp2.write("\n")
    #mangling with *
    fp2.write(name[0])
    fp2.write("*")
    fp2.write(name[1])
    fp2.write("\n")
    #mangling with _
    fp2.write(name[0])
    fp2.write("_")
    fp2.write(name[1])
    fp2.write("\n")


fp.close()
fp2.close()