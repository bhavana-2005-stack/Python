def countevenodd():
    l=[1,9,8,6,4,55,89]
    counte=0
    counto=0
    for i in l:
        if i%2==0:
            counte=counte+1
        else:
            counto=counto+1
    print("even num",counte)
    print("odd num",counto)
countevenodd()