"""
Programming Activity 4

Write a program that prints all the multiples of 5, from 5 to 95 using a while loop.
"""
i = 5
while i <= 95:
    if i % 5 == 0:
        print(f"{i} is a multiple of 5")
        i += 1
    i += 1