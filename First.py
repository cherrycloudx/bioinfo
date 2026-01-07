# Variable in Python
# variable is memory location in computer stores the values (container)

"""Rules of variables :
1. A variable name must only contain alphanumeric characters and underscores (A-z, 0-9, and _ )
2. A variable name must start with a letter or the underscore character
3. A variable name cannot start with a number
4. No white space between variable name.
5. No special character is permitted to use.
6. Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
7. Do not use Python keywords as variable names.

"""
#Python developers use snake case(snake_case) variable naming convention.
#We use underscore character after each word for a variable containing more than one word(eg. first_name, last_name etc) 

First_name = "Cherry"
Last_name = "Blossom"
age = 120 #it is not my actual age so dont worry about it :D
country = "India"
is_married = False
skills = ("C++", "Python", "R", "SQL")
person_info = (
    'Firstname: Cherry',
    'Lastname: Blossom',
    'Age : 120',
    'Country : India')

#use built function print() to print the variables value
# f-string = formatted string used to print multiple variables in a single print state
print(f"First Name: {First_name}", f"Last name: {Last_name}", f"Age: {age}", 
      f"Country name: {country}", f"Married status: {is_married}",
      f"Skills: {skills}", f"Person's Info: {person_info}", sep="\n")

# Getting user input using the input() built-in function.
# Let us assign the data we get from a user into Name and Age variables. Example:
Name = input("what is your name? ")
Age = input("What is your Age? ")

#printing the Variables 
print(f"Your name : {Name}".title().strip(), f"Your Age : {Age}", sep="\n")

#Some special functions for improving the user input :
#  strip() = It removes and extra white space present between user input characters.
#  title() = It Capatilised the string first letter of each word.
#  len() = It counts the number of characters present in the string including spaces.
# Example of len() function: 
print(len(Name)) #12 output
print(len(Age)) #2 output



