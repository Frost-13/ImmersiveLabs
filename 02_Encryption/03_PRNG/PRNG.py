def lcg(a,b,m,r):
    #save list of nums in this list
    final = []
    for i in range(10):
        #formula given
        #Ri+1 = (aRi + b) (mod m)
        r = ((a*r)+b)%m

        final.append(r)
    return final
