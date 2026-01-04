# Variable in Python
# variable is memory location in computer stores the values (container)
"""Rules of variables :
1. Only Digits, Alphabets and underscores are permitted. 
2. Variable name should start with underscore and alphabets only.
3. No white space between variable name.
4. No special character is permitted to use.
"""

# Below Example : "name" is a variable that stores a String (str)
name = input("What's your Name? ")  # Takes input from the User
print(name)                         # Prints Name of the user

# Some special functions for improving the user input :
#  strip() = It removes and extra white space present between user input characters.
#  title() = It Capatilised the string first letter of each word.

Name = input("What is your name? ").strip().title()
print("Hello,", Name)  


