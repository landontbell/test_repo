"""
Write a Python function that takes input from the user for three numbers, compares them using dynamic typing, 
and outputs the smallest and largest numbers. Then, if the largest number is divisible by 2, print the range 
between the smallest and largest numbers. If the largest number is not divisible by 2, print whether the 
smallest number is within the range of 0 to 10.
"""

def compare():
    num1 = input("Please enter the first number:\n")
    num2 = input("Please enter the second number:\n")
    num3 = input("Please enter the third number:\n")
    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)
    sml = min(num1, num2, num3)
    lrg = max(num1, num2, num3)
    print(f"The smallest number is {sml}")
    print(f"The largest number is {lrg}")
    if lrg % 2 == 0:
        print(f"The range between the largest and smallest number is: {lrg - sml}")
    else:
        if sml in range(0,10):
            print(f"{sml} is within the range of 0-10")
        else:
            print(f"{lrg} is not divisible by 2 and {sml} is not within the range of 0-10")
            
if __name__ == "__main__":
    compare()