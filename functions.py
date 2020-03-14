def divide(num1 , num2):
    return num1 / num2

def plus(num1 , num2):
    return num1 + num2

def minus(num1 , num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 * num2

def power(num1 , num2):
    return num1 ** num2


operation = input("What operation do you want, +, -, /, *, ** : ")
num1 = input(" Enter your number: ")
num2 = input("Enter another number: ")


if operation == "+":
    num3 = plus(float(num1) , float(num2))
elif operation == "-":
    num3 = minus(float(num1), float(num2))
elif operation == "*":
    num3 = multiply(float(num1), float(num2))
elif operation == "/":
    num3 = divide(float(num1) , float(num2))
elif operation == "**":
    num3 = power(float(num1), float(num2))
else:
    print("Sorry about the unconvienece but we coudn't find your answer due to your operation " + operation)
    num3 = 0

if num3 > 0:
    print("Result: " + str(num3))

