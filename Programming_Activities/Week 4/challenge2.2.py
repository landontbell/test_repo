"""
2. Write a Python program to reverse a given three or more digit integer WITHOUT using lists (hint, use // and % to isolate numbers)
"""
base_number = int(input("Please input a 3 digit or more number:\n"))
reversed_number = 0
number = base_number
while number > 0:
    digit = number % 10 # Pulls the last number by getting the remainder of 10
    number = number // 10 # Removes the last number by doing floor division
    reversed_number = reversed_number * 10 + digit # Multiplies by 10 to add a digit to the number then add the reversed number back to it
print(f"{base_number} reversed is {reversed_number}")