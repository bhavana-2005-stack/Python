#check if a number is divisible by 5 and 11 or not
def divisibility(a):
    if a%5==0 and a%11==0:
        print(a, "is divisible by both 5 and 11")
    else:
        print(a, " is not divisible by either 5 or 11")
divisibility(55)
divisibility(22)