#  Simple Calculator with Conditionals
# Write a Python program that takes two numbers and an operation (+, -, *, /) from the user.
# Perform the operation and print the result.



# addition
def myCalculator(num1,num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid Operator"


num1 = int(input("Enter the first number: \t"))
num2 = int(input("Enter the second number: \t"))
operator = input("Enter the operation you want to perform: \t")

results = myCalculator(num1,num2, operator)

print('\n Operation \t', f'{num1} {operator} {num2} = {results}')
