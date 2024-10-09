# Function to calculate area of a triangle
def triangle_area(base, height):
    area = 0.5 * base * height
    return format(area, ".2f")

# Input base and height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate and print the area
print("The area of the triangle is:", triangle_area(base, height))

# IN C++ THIS IS HOW YOU DO IT:
#        cout << "The area of the triangle is: " << fixed << setprecision(2) << area << endl;

#In C++, fixed is a manipulator used to control the formatting of floating-point numbers when printing them to the console (or writing to a stream). 
#When combined with setprecision(n), it ensures that the output will display exactly n digits after the decimal point, regardless of the size of the number.

#Without fixed: setprecision(3) affects the total number of significant digits, so it truncates the number to just 3 digits (i.e., 123).
