def perform_operation(num1, num2, operation):
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed."
    else:
        return "Invalid operation choice."

print("Simple Calculator")
print("Available Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = int(input("Enter the operation choice (1/2/3/4): "))

result = perform_operation(num1, num2, operation)

print("Result:", result)





# Task Done
