# Create a program, which takes 10 random numbers. The program should produce
# a list of non prime and tuple of prime numbers. After input is done, program should return the the mathematical
# differnce between the highest and lowest number from non primary numbers, and sum of primary numbers from tuple.


# num_one = float(input("Enter number one: "))
# num_two = float(input("Enter number two: "))
# num_three = float(input("Enter number three: "))
# num_four = float(input("Enter number four: "))
# num_five = float(input("Enter number five: "))
# num_six = float(input("Enter number six: "))
# num_seven = float(input("Enter number seven: "))
# num_eight = float(input("Enter number eight: "))
# num_nine = float(input("Enter number nine: "))
# num_ten = float(input("Enter number ten: "))

# num_one = 3
# num_two = 7
# num_three = 15
# num_four = 20
# num_five = 80
# num_six = 14
# num_seven = 3
# num_eight = 10
# num_nine = 1
# num_ten = 9

# my_list = [num_one, num_two, num_three, num_four, num_five, num_six, num_seven, num_eight, num_nine, num_ten]

# non_prime_list = []

# for number in my_list:
#     if (number % number) == 0:
#         non_prime_list.append(number)
# print(non_prime_list)

# Create a program, which takes 10 random numbers as user inputs.
# The program should produce list of input values what are less than 50 and tuple of all other values.
# After input is done, program should return the the mathematical differnce between the highest and lowest number, and sum of numbers from tuple.


num_one = int(input("Enter number one: "))
num_two = int(input("Enter number two: "))
num_three = int(input("Enter number three: "))
num_four = int(input("Enter number four: "))
num_five = int(input("Enter number five: "))
num_six = int(input("Enter number six: "))
num_seven = int(input("Enter number seven: "))
num_eight = int(input("Enter number eight: "))
num_nine = int(input("Enter number nine: "))
num_ten = int(input("Enter number ten: "))

my_list = [num_one, num_two, num_three, num_four, num_five, num_six, num_seven, num_eight, num_nine, num_ten]
list_less_than_50 = []
my_tuple = []
for number in my_list:
    if number < 50:
        list_less_than_50.append(number)
    else:
        my_tuple.append(number)

my_difference = max(list_less_than_50) - min(list_less_than_50)
print(f"Difference between the highest and lowest number in list: {my_difference}")

tuple(my_tuple)
# for number in my_tuple:
#     my_sum += number
# print(f"Sum of numbers from tuple: {my_sum}")
my_sum = sum(my_tuple)
print(f"Sum of numbers from tuple: {my_sum}")

