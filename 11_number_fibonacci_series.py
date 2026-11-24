# 11. Fibonacci series
# The series starts with 0 and 1. Each new number is the sum of the previous two.
n = int(input("How many terms? "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Iteration	a (printed)	b	New a	New b
# 1	        0	        1	    1	1
# 2	        1	        1	    1	2
# 3     	1	        2	    2	3
# 4     	2	        3	    3	5
# 5     	3	        5	    5	8