def uniqueelements():
    list=[1,1,4,12,89,7,6,3,4,12]
    unique_list=[]
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)
uniqueelements()
