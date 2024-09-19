#A Peterson number is a number that equals the sum of the factorials of its digits. For example, 145 is a Peterson number because:
# 145 = 1!+4!+5! = 1+24+120 = 145

import math

# Use a different variable name instead of 'sum'
factorial_sum = 0
num = int(input("Enter the number: "))
original_num = num  # Store the original number for comparison

while num > 0:
    a = num % 10
    factorial_sum += math.factorial(a)
    num //= 10  # Use integer division to remove the last digit

# Compare the sum of factorials with the original number
if factorial_sum == original_num:
    print(True)
else:
    print(False)
