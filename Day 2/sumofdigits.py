def sumofdigits(n):
    sum=0
    while n>=1:
        sum+=n%10
        n=n//10
    print(sum)
sumofdigits(1234)
sumofdigits(22222)