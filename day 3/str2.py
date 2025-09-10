def count():
    s="123hello#world"
    dig=0
    alpha=0
    spl=0
    for char in s:
        if char.isdigit():
            dig+=1
        elif char.isalpha():
            alpha+=1
        else:
            spl+=1
    print("num of digits:",dig)
    print("num of alphabets:",alpha)
    print("num of spl chars:",spl)
count()