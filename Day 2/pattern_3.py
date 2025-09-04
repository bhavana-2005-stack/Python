def pattern_3(i,j):
    for x in range(i):
        for y in range(j):
            if (x==y) or (x==j-y-1):
                print("$",end=  " ")
            else:
                print("*",end=" ")
        print()
pattern_3(5,5)       
