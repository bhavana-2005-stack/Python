def palindrome(n):
    for i in range(1,n+1):
        n_str=str(i)
        rev_str=n_str[::-1]
        if (n_str==rev_str):
            print(n_str,end =" ")
palindrome(1000)