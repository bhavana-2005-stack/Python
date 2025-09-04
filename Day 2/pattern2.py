def pattern_2(i,j):
    for x in range(i):
        for y in range(j):
            if x==y:
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()
pattern_2(5,5)