def amt(a):
    count=0
    if a>=500:
        count+=a//500
        a=a%500
    if a>=200:
        count+=a//200
        a=a%200
    if a>=100:
        count+=a//100
        a=a%100
    if a>=50:
        count+=a//50
        a=a%50
    if a>=20:
        count+=a//20
        a=a%20      
    if a>=10:
        count+=a//10
        a=a%10
    print("total number of notes",count)
a=int(input("enter amt"))
amt(a)

        