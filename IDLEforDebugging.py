# Program 3: Using IDLE for Debugging

# This program has an intentional error (division by zero) for debugging practice.
def divide_numbers(a, b):
    return a / b

# Main code
num1 = 10
num2 = 0  # This will cause a division by zero error

# Call the function and print the result
result = divide_numbers(num1, num2)
print("Result:", result)
