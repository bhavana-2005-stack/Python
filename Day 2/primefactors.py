def prime_factor(n):
    i=2
    while i<=n:
        if n%i==0:
            print(i,end=" ")
            n=n//i
        else:
            i+=1
prime_factor(40)
        