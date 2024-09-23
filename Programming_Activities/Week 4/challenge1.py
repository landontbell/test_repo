"""
Write in pseudocode and then in Python a program that simulates a guessing game. 
The program should randomly choose a number between 1 and 100. 
The user must guess the number, and the program will tell the user if their guess is too high, too low, or correct. 
The game should continue until the user guesses the correct number or chooses to quit. 
The program should also keep track of how many guesses the user made.
"""

"""
Set the number of guesses to zero
generate a random number between 1-100
prompt the user to guess the number

set up a loop to let it run until they guess the number

check if the guess is higher or lower than the random number.
tell the user if their guess was too high or low
Increment the count for each guess
prompt the user to guess again

continue this logic until they guess the number
once they guess it add one to the count because their most recent guess needs to be accounted for
tell thee user that they guesseed it and in how many guesses
"""


import random
num = random.randint(1,100)
count = 0
guess = int(input(f"What is your guess?\n"))
while guess != num:
    if guess > num:
        print("Too high try again")
        guess = int(input(f"What is your guess?\n"))
        count += 1
        
    elif guess < num:
        print("Too low try again")
        guess = int(input(f"What is your guess?\n"))
        count += 1
count += 1
print(f"Good job you guessed {num} in only {count} tries!")

    