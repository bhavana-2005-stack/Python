def perfect_num(n):
    for i in range(1,n+1):
        total=0
        i=1
        while i<num:
            if num%i==0:
                total+=i
            i+=1
        if total==num:
            print(i,end=" ")
perfect_num(20000)
    