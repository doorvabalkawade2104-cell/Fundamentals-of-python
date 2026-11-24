#14. Check whether a number is an Armstrong number
#A number is an Armstrong number if the sum of its digits raised to the number of digits equals the original number.

#Example: \(153 = 1^3 + 5^3 + 3^3 = 153\).
n = int(input("Enter a number: "))
temp = n
digits = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == n:
    print("Armstrong number")
else:
    print("Not Armstrong")