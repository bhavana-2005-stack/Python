def removeduplicates():
    l=[1,7,89,4,23,12,12,7,1]
    unique_list=[]
    for i in l:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)
removeduplicates()
