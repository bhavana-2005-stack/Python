def exception_handling():
    n=int(input("Enter numerator:"))
    d=int(input("Enter denominator:"))
    try:
        res=n/d
        print(res)
    except ZeroDivisionError:
        print("denominator must not be zero")
exception_handling()

