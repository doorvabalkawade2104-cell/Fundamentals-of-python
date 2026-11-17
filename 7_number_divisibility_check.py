#7. Check whether a number is divisible by another number

a = int(input("Enter number: "))
b = int(input("Enter divisor: "))

if b != 0 and a % b == 0:
    print("Divisible")
else:
    print("Not divisible")