"""
Programming Activity 2

Write a program which can adds up the numbers in the series:
1/2 + 1/4 + 1/8 + 1/16 + 1/32 for 1000 iterations.
create a variable for the denominator
for loop for 1000 iterations
start for loop at 1, go to 1000
variable to track the sum
What number is the result?
"""
total = 0
denom = 0.5
for i in range(1, 1000):
    total += denom
    denom /= 2
print(total)
    