# Data types in Python :
# Data type defines the type of data a variable can stores

'''
int - stores integers value
str - stores string of character (should be in double qoute)
float - stores decimal value
boolean - stores true or false
complex - stores complex numbers (not commonly used)
'''

#Example of data types: 
a = int(input("Enter the value of a: ")) # value of a stored in the integer data type
b = float(input("enter the value of b: ")) #value of b stored in Decimal data type
c = input("Enter your Name: ") # value of c is in double quote that shows the string
d = bool(input("Enter the Condition to check T/F : ")) # value of d gives True or False 
print(f"The value of a is: {a}", f"The value of b is: {b}", f"The value of c is: {c}".title().strip(), f"The value of d is: {d}", sep="\n")

# You can check the data type of variable by using type() function
print(f"The data type of a is: {type(a)}")
print(f"The data type of b is: {type(b)}")
print(f"The data type of c is: {type(c)}")
print(f"The data type of d is: {type(d)}")

# You can convert one data type to another by using type casting functions:
# int() - converts to integer
# float() - converts to float
# str() - converts to string
# bool() - converts to boolean
x = "123"
y = int(x) # converts string to integer
z = float(x) # converts string to float
w = bool(x) # converts string to boolean
print(f"The value of y is: {y} and its data type is: {type(y)}")
print(f"The value of z is: {z} and its data type is: {type(z)}")
print(f"The value of w is: {w} and its data type is: {type(w)}")
# Note: Converting non-numeric string to int or float will raise an error.  
