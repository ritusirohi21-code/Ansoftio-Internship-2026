# Python Developer Internship – Day 12
# Topic: Functions in Python

def area(length, width):
    return length * width

l = int(input("Enter length: "))
w = int(input("Enter width: "))

result = area(l, w)

print("Area of rectangle:", result)