"""
Programming Activity 3

Write a program which determines whether a child can sit in the front seat  of a car, using the following logic:
- if a child is 12 years old or older, they can sit in the front, regardless of weight.
- if a child is 11 years old, and over 90 pounds, they can sit in the front seat.
- if a child is under 11 years old, and over 100 pounds, they can sit in the front seat
- if a child does meet the criteria above they cannot sit in the front seat.
Your program will ask the user for a child's age and weight. Use Boolean variables to store the results of the criteria above. 
Use if statements and the Boolean variables created above to print a message to the user whether or not the child may sit in the front seat.
"""

age = int(input("What is your childs age?\n"))
weight = int(input("What is your childs weight?\n"))
front = False
if age == 12:
    front = True
elif age == 11 and weight > 90:
    front = True
elif age < 11 and weight > 100:
    front = True
else:
    front = False

print(f"Can my child sit in the front seat? {front}")