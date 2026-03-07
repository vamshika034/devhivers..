#Simple Calculator (Addition, Subtraction, Multiplication, Division)
# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print("Result =", num1 + num2)

elif choice == '2':
    print("Result =", num1 - num2)

elif choice == '3':
    print("Result =", num1 * num2)

elif choice == '4':
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero not allowed")

else:
    print("Invalid choice")




#Number Guessing Game (1–100)
import random

number = random.randint(1, 100)

guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < number:
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.")

    else:
        print("Congratulations! You guessed the correct number.")




