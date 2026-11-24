# 12. Check whether a number is prime
# A prime number is greater than 1 and has exactly two positive factors: 1 and itself.
n = int(input("Enter a number: "))
prime = True

if n < 2:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

if prime:
    print("Prime")
else:
    print("Not prime")