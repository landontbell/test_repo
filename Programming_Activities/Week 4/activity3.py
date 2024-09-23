"""
Programming Activity 3

Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 
"""
for i in range(5,96):
    if i % 5 == 0:
        print(f"{i} is a multiple of 5")
    i += 1