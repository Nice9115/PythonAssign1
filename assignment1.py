def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Math Error."
    return x / y


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Enter operation (+,-,*,/) ")


if choice == '+':
    print(f"{num1} {choice} {num2} = ", add(num1, num2))
elif choice == '-':
    print(f"{num1} {choice} {num2} =:", subtract(num1, num2))
elif choice == '*':
    print(f"{num1} {choice} {num2} =", multiply(num1, num2))
elif choice == '/':
    print(f"{num1} {choice} {num2} =", divide(num1, num2))
else:
    print("Invalid input")

