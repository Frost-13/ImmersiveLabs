def crack_lcg(m, r1, r2, r3):
    #error checking
    if m<0:
        return[0,0]
    check_list = [r1,r2,r3]
    for i in check_list:
        if i<0 or i>(m-1):
            return [0,0]

    #do the equation subtraction
    temp1 = r1-r2
    temp2 = r2-r3

    #find the possible int for a that works
    for i in range(m):
        if (((i*temp1)%m)) == temp2:
            a = i
    #find the possible int for b that works
    for i in range(m):
        if (((a*r1)+i)%m) == r2:
            b = i
    return [a,b]
