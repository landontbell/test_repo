"""
Programming Activity 1

 1. make a variable called apple_price (set it to whatever you want)
 2. make a variable called number_purchased (set it to whatever you want)
 3. make a variable called tax and set it equal to 1.07
 4. make a variable, total_bill and calculate it by: total_bill = apple_price * number_purchased * tax
 5. print clearly and cleanly how many apples were purchased and the total_bill
 6. add a check before the final print statement to see if total_bill is equal to 0.  If so, print a message to the user to check their inputs.
"""

apple_price = 3.12
number_purchased = int(input("How many apples did you buy?\n"))
tax = 1.07
total_bill = round(apple_price * number_purchased * tax, 2)
if total_bill == 0:
    print("Please check your inputs")
else:
    print(f"You bought {number_purchased} apples at a price of {apple_price}. For a total cost of ${total_bill}")