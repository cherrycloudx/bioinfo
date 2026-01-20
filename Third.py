# Operators in Python
a = 10
b = 3
# Arithmetic Operators
print("Addition:", a + b)          # 13
print("Subtraction:", a - b)       # 7
print("Multiplication:", a * b)    # 30
print("Division:", a / b)          # 3.3333...
print("Floor Division:", a // b)   # 3, Floor division discards the decimal part 
print("Modulus:", a % b)           # 1 # Remainder of the division
print("Exponentiation:", a ** b)   # 1000  # a raised to the power of b

# Comparison Operators
print("Equal:", a == b)            # False
print("Not Equal:", a != b)        # True
print("Greater Than:", a > b)      # True
print("Less Than:", a < b)         # False
print("Greater Than or Equal To:", a >= b)  # True
print("Less Than or Equal To:", a <= b)     # False

# Logical Operators
print("Logical AND:", (a > 5) and (b < 5)) # True # Both conditions are true # AND operator returns True only if both operands are true 
print("Logical OR:", (a > 5) or (b > 5)) # True  # At least one condition is true # OR operator returns True if at least one operand is true
print("Logical NOT:", not(a > 5)) # False # NOT operator inverts the boolean value 
print("Logical NOT:", not(b > 5)) # True # Inverts the boolean value 

# Assignment Operators
 
a += b
print("a after += b:", a)          # 13
a -= b
print("a after -= b:", a)        # 10 # Subtract b from a # a is 13 right now
a *= b
print("a after *= b:", a)          # 30
a /= b
print("a after /= b:", a)          # 10.0
a //= b
print("a after //= b:", a)         # 3.0
a %= b
print("a after %= b:", a)          # 0.0
a **= b
print("a after **= b:", a)         # 0.0


# Bitwise Operators: 
# Demonstrating bitwise operations on integers
a = 10  # 1010 in binary
b = 3   # 0011 in binary    
# Bitwise Operations
# AND, OR, XOR, NOT, Left Shift, Right Shift
# Expected Results:
# Bitwise AND: 2 (0010 in binary)
# Bitwise OR: 11 (1011 in binary)
# Bitwise XOR: 9 (1001 in binary)
# Bitwise NOT: -11 (inverts bits and adds 1 in two's complement )
# print("Bitwise AND:", a & b)       # 2

print("Bitwise AND:", a & b)       # 2
print("Bitwise OR:", a | b)        # 11
print("Bitwise XOR:", a ^ b)       # 9
print("Bitwise NOT:", ~a)          # -11
print("Left Shift:", a << 1)       # 20
print("Right Shift:", a >> 1)      # 5

# Difference between Logical and Bitwise Operators:
x = 5  # 0101 in binary
y = 3  # 0011 in binary
# Logical AND
print("Logical AND:", (x > 2) and (y < 5)) # True
# Bitwise AND
print("Bitwise AND:", x & y)           # 1 (0001 in binary) # Bitwise AND of 0101 and 0011 is 0001 # Both bits must be 1 to result in 1
# Logical OR
print("Logical OR:", (x > 2) or (y > 5)) # True
# Bitwise OR
print("Bitwise OR:", x | y)                # 7 (0111 in binary) # Bitwise OR of 0101 and 0011 is 0111 # At least one bit must be 1 to result in 1
# Logical NOT
print("Logical NOT:", not(x > 2))          # False
# Bitwise NOT
print("Bitwise NOT:", ~x)                   # -6 # Inverts bits and adds 1 in two's complement # 0101 becomes 1010 which is -6 in two's complement
# Note: Logical operators work with boolean values, while bitwise operators work with the binary representation of integers.
print("Bitwise AND:", a & b)       # 2
print("Bitwise OR:", a | b)        # 11
print("Bitwise XOR:", a ^ b)       # 9 # 1001 in binary 
print("Bitwise NOT:", ~a)          # -11   # Inverts bits and adds 1 in two's complement      
print("Left Shift:", a << 1)       # 20 # 10100 in binary 
print("Right Shift:", a >> 1)      # 5 # 0101 in binary

