#swapping of numbers
a=int(input("enter num1"))
b=int(input("enter num2"))
print("Before swapping")
print("a=",a)
print("b=" ,b)
temp=a
a=b
b=temp
print("after swapping")
print("a=", a)
print("b=" ,b)
print("without using temp")
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)