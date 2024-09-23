"""
1. Find all the prime numbers within a given range using a for loop
"""

start = int(input("Input the start for the range\n"))
end = int(input("Input the end for the range\n"))
print(f"Prime numbers within the range {start}-{end} are:")
end = end + 1 # Add one to the end so it can check if the end is prime also
for num in range(start, end):
    if num > 1: #Prime numbers are greater than 1
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            print(num)
        
