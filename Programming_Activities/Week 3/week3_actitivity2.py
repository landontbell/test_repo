"""
Programming Activity 2

Write a program that asks the user how old they are, and what age they would like to live to. Calculate how long they have left to live (approximately), and then print a friendly message telling the user how long they have to 
live.
"""
age = int(input("How old are you?\n"))
death = int(input("What age would you like to live too?\n"))
life_left = death - age
print(f"You have {life_left} years left to live, nice!")