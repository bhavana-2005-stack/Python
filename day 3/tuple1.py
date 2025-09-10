def studetails():
    allmarks=[]
    for i in range(0,2):
        name=str(input("enter name of stu"))
        rno=int(input("enter roll no"))
        marks=int(input("enter marks:"))
        studentdetails=(name,rno,marks)
        allmarks.append(marks)
        if marks>75:
            print(studentdetails)
    print("all marks:",max(allmarks))
studetails()