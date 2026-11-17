# 9. Sum of squares of the first N natural numbers
# For \(n=3\): \(1^2+2^2+3^2=14\).
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i ** 2

print("Sum of squares:", total)