#calculate total average marks of student and print all student details
sno=int(input("Enter Student number"))
sname=str(input("enter student name"))
sub1,sub2,sub3=map(int,input("Enter 3 sub marks").split())
total=(sub1+sub2+sub3)
avg=total/3
if avg>=40:
    print("pass")
    if avg<50:
        print("C grade") 
    elif 51<avg<70:
        print("B grade")
    elif 71<avg<80:
        print("A grade")
    elif avg>80:
        print("distinction")
else:
    print("fail")  

print("student number", sno)
print("student name" , sname)
print("total marks" ,total)
print("average marks" ,round(avg,2))