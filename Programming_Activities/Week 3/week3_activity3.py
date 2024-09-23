"""
Programming Activity 3

Write a program that gets a user's score in this class, as a percentage i.e. 90 or 95. 
Write an if statement that checks to see if their score is equal to or greater than 93.  
If so, print "Congratulations you got an A" else print "Congratulations, you still learned a ton!!!!"
"""
score = int(input("What grade did you get in the class?\n"))
if score >= 93:
    print("Congratulations you got an A")
else:
    print("Congratulations, you still learned a ton!!!!")
    
    