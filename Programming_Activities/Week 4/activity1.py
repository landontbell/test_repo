"""
Programming Activity 1

Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to 
based on the following rules/years:
 - Zoomer 1997
 - Millennial 1981
 - Gen X 1965
 - Baby Boomer 1946
"""
year = int(input("What year where you born?\n"))
if year >= 1997:
    gen = "Zoomer"
elif year >= 1981:
    gen = "Millennial"
elif year >= 1965:
    gen = "Gen X"
else:
    gen = "Baby Boomer"

print(f"Based on your birth year you are a {gen}!")