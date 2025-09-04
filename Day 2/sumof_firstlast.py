def sumof_firstlastdigits(n):
    n_str=str(n)
    first=n_str[0]
    last=n_str[-1]
    num1=int(first)
    num2=int(last)
    c=num1+num2
    print(c)
sumof_firstlastdigits(1234)