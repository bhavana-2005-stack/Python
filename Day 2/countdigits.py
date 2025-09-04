def numofdigits(n):
    count=0
    while n>=1:
        count+=1
        n=n//10
    print(count)
numofdigits(2222222)
numofdigits(12)