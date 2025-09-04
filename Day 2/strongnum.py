def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
def strong_num(n):
    for i in range(1,n+1):
        total=0
        for d in str(i):
            total+=fact(int(d))
            if total==i:
                print(i,end=" ")
strong_num(1000)
