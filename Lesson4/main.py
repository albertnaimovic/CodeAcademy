# weight_lower_limit: float = 60.0
# weight_higher_limit: float = 100.0

# my_weight = float(input("Enter your weight: "))

# if my_weight > weight_higher_limit:
#     if my_weight > 125.5:
#         print("Too much.....")
#     print("Mindaugas is too fat")
# elif my_weight < weight_lower_limit:
#     print("Mindaugas is too skinny")
# else:
#     print("Mindaugas is cool")


# if my_weight > weight_higher_limit:
#     print("Mindaugas is too fat")
# print("Lalala")

# a = 50
# b = int(input("Enter b: "))
# if b >= a:
#     print(b)
# else:
#     print(a)

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# d = int(input("Enter d: "))

# if a < b and b < c:
#     print(f"First condition met: {b}")
# elif a > c:
#     print(f"Second condition met: {a}")
# else:
#     print(f"Last condition met: {a, b, c, d}")

# 1. Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.

# user_name = input("Enter your name: ")
# user_surname = input("Enter your surname: ")
# user_age = int(input("Enter your age: "))

# if user_age > 20:
#     print(f"{user_name} {user_surname} is allowed to enter casino.")
# else:
#     print(f"{user_name} {user_surname} is NOT allowed to enter casino.")


# 2. Create a database (List of privileged users) print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"

# privileged_users = ["Tom", "Albert", "Stephen"]
# user_name = input("Enter your name: ")

# if user_name in privileged_users:
#     print(f"Welcome, {user_name}!")
# else:
#     print("Welcome otherwise")


# 3. allow user to enter two numbers, print out which one is higher than the other, or are they equal?

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > b:
#     print(f"{a} is higher than {b}")
# elif a < b:
#     print(f"{b} is higher than {a}")
# else:
#     print("They are equal.")


# 4. Write a small calculator application, that allows user to enter two numbers and a symbol, given and then do the operation and print an answer.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# symbol = input("Enter symbol: ")

# if symbol == "+":
#     print(f"Sum: {a + b}")
# elif symbol == "-":
#     print(f"Difference: {a - b}")
# elif symbol == "*":
#     print(f"Multiplication: {a * b}")
# elif symbol == "/":
#     print(f"Division: {a / b}")
# else:
#     print("There is no such symbol in my calculator :(")


# 5. create a number guessing game from 1-10, with random library. (IDEA FOR LATER MAYBE)


import random
#from random import randint

random_number = random.randint(1, 10)
#random_number = randint(1, 10)
guess_number = int(input("Guess the number from 1 to 10: "))

if guess_number == random_number:
    print(f"You've guessed it! It is {random_number}")
else:
    print(f"You haven't guessed, the right answer is {random_number}")
