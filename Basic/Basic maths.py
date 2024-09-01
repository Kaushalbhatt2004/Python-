import math

x = 4.5
y = 2

print(math.ceil(x))      # Rounds x up to the nearest integer, output: 5
print(math.floor(x))     # Rounds x down to the nearest integer, output: 4
print(math.fabs(x))      # Returns the absolute value of x, output: 4.5

# factorial should be applied to an integer, so let's use y instead of x
print(math.factorial(y)) # Returns the factorial of y, output: 2

print(math.fmod(x, y))   # Returns the remainder when x is divided by y, output: 0.5

print(math.log2(x))      # Returns the base-2 logarithm of x

print(math.log10(x))

print(pow(x,y))          # Returns x raised to the power y

print(math.sqrt(x))

print(math.trunc(x))     # Returns the truncated integer 

print(math.pi)       

print(math.tau)

print(math.e)            # Returns Euler's number

print("Positive infinity-",math.inf)

print("Negative infinity-",-math.inf)