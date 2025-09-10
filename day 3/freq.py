def frequency():
    l=[1,90,8,45,5.3]
    n=len(l)
    l.sort()
    i=0
    while i<n:
        cnt=1
        j=i
        while j<n-1 and l[j]==l[j+1]:
            cnt+=1
            j+=1
        print(l[i],"=",cnt)
        i=j+1
frequency()