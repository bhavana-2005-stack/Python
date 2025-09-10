def strlen():
    count1=0
    count2=0
    s1="hi"
    s2="hi"
    for char in s1:
        count1+=1
    print(count1)
    for char in s2:
        count2+=1
    print(count2)
    if s1==s2:
        print("equal")
    else:
        print("not equal")
    print(s1+s2)
strlen()