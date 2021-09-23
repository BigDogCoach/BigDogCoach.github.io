calculator = False

start = input("Do you want to use the calculator? [Y/N] ")

if start.lower() == "y":
    calculator = True
elif start.lower() == "n":
    calculator = False

while calculator:
    num1 = float(input("Enter your first number here: "))
    operator = input("Enter one of these operators- +,-,/,*,%,**: ")
    num2 = float(input("Enter your second number here: "))

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "*":
        print(num1 * num2)

    elif operator == "%":
        print(num1 % num2)
    elif operator == "**":
        print(num1 ** num2)
    else:
        print("You have either entered an invalid operator or didnt enter a number.")

    answer = input("Do you want to use the calculator again? [Y/N] ")
    if answer.lower() == "y":
        calculator = True
    elif answer.lower() == "n":
        calculator = False
    else:
        calculator = False