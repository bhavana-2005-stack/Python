def armstrong_num(n):
    for i in range(1,n+1):
        digits=str(i)
        power=len(digits)
        total=0
        for d in digits:
            total+=int(d)**power
        if total==i:
            print(i,end=" ")
armstrong_num(150)

    
         