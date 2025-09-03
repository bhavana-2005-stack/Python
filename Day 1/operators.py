#operations
def operations(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y 
    e=x%y 
    f=x//y 
    g=x**y
    return a,b,c,d,e,f,g;
x=10
y=5
z=operations(x,y)
print("result of operations" , z)