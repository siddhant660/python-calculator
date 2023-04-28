# A calculator program that can perform basic arithmetic operations

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: division by zero"
    else:
        return num1 / num2

print("Welcome to the calculator program!")
print("Please select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter your choice (1/2/3/4): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operation == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operation == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid operation")