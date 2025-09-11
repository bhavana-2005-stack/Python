class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("roll no:",self.rollno)
        print("Marks:",self.marks)
s1=Student("Lucky",9,79)
s2=Student("mary",12,68)
s1.display()
s2.display()

