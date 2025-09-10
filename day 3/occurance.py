def occurance():
    s="bhavana"
    ch='a'
    occurance=[]
    for i in range(len(s)):
        if s[i]==ch:
            occurance.append(i)
    print("occurance of a", ch,"is",occurance)
occurance()