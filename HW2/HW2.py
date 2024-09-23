# Homework Week 2 
# Landon Bell

# 2.3
# Basic IF statements and variable printing
print("Problem 2.3:\n") # Print for better formatting and easier reading in output
grade = int(input("What Grade did you earn for this course? \n"))
if grade >= 91:
    print(f"Congratulations! Your grade of {grade}% has earns you an A in this course!")
else:
    print(f"Unfortunately, your grade of {grade}% DOES NOT earn you an A in this course.")



# 2.4
# Basic arithmetics operations
print("Problem 2.4:\n") # Print for better formatting and easier reading in output
left = 27.5
right = 2
add = left + right
subtract = left - right 
multiply = left * right
divide = left / right
floor = left // right
power = left ** right
print(f"Addition: {add}\nSubtraction: {subtract}\nMultiplication: {multiply}\nDivision: {divide}\nFloor: {floor}\nPowers: {power}")




# 2.5
# Circles: Area, Circumferenc, Diameter
print("Problem 2.5:\n") # Print for better formatting and easier reading in output
radius = 2
pi = 3.14159
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius ** 2
print(f"Diameter: {diameter}\nCircumference: {circumference}\nArea: {area}")





# 2.6
# Remainder Operations: Odd/Even
print("Problem 2.6:\n") # Print for better formatting and easier reading in output
x = int(input(f"Input number and check if it is even:\n"))
if x % 2 == 0:
    print(f"{x} IS an even number")
else:
    print(f"{x} IS NOT an even number")
    
    
    

# 2.7
# More remainder operations: Checking for multiples
print("Problem 2.7:\n") # Print for better formatting and easier reading in output
a = 1024
b = 10
if a % 4 == 0:
    print(f"{a} IS divisible by 4")
else:
    print(f"{a} IS NOT divisible by 4")

if b % 2 == 0:
    print(f"{b} IS divisible by 2")
else:
    print(f"{b} IS NOT divisible by 2")




# 2.8
# Detailed math operations with iteration to print a formatted output
print("Problem 2.8:\n") # Print for better formatting and easier reading in output
print("Number\tSquare\tCube")
for num in range(0,6):
    print(f"{num}\t{num**2}\t{num**3}")
    
    