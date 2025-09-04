# Print prime numbers up to N using while loop

n = int(input("Enter the limit: "))
num = 2

print("Prime numbers are:")

while num <= n:
    i = 2
    is_prime = True
    while i * i <= num:  
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, end=" ")
    num += 1
