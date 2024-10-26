# Program 2: Simple Arithmetic Calculator

# Define addition function
def add(a, b):
    return a + b

# Define subtraction function
def subtract(a, b):
    return a - b

# Define multiplication function
def multiply(a, b):
    return a * b

# Define division function
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# Main program to prompt user for inputs
print("Simple Arithmetic Calculator")
print("Choose an operation: +, -, *, /")
operation = input("Enter operation: ")

# Get numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the chosen operation and display the result
if operation == '+':
    print("Result:", add(num1, num2))
elif operation == '-':
    print("Result:", subtract(num1, num2))
elif operation == '*':
    print("Result:", multiply(num1, num2))
elif operation == '/':
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation!")
