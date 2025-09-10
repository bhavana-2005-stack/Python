def countduplicates():
    l=[1,22,3,45,68,1,2,22,12,12]
    dupl=[]
    for i in l:
        if l.count(i)>1:
            if i not in dupl:
                dupl.append(i)
    print(dupl)
    print(len(dupl))
countduplicates()
