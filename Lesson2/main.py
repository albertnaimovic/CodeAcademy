# print('hello')
# my_name = 'Albis'
# my_age = 15
# print(my_name +str(my_age))

# num_one = 5
# num_two = 7
# print('Sum:', num_one + num_two, '\nMinus:', num_one - num_two, '\nMultiplication:', num_one * num_two, '\nDivision:', num_one / num_two, '\nExponentiation:', num_one ** num_two)

# my_name = input('Enter my name: ')
# print('My name is:', my_name)

# name = "Code Academy"
# print(name.replace('Co','Ka'))

# print(type(float("das")))

# 1
# my_name = input("Enter my name: ")
# my_age = int(input("Enter my age: "))
# age_calculation = 2023 - my_age
# print(my_name, "was born in", age_calculation)

# 2
# my_sentence = input("Enter sentence: ")
# print(my_sentence[::-1])
# print(my_sentence[::2])

# 3
# num_one = int(input("Enter num one: "))
# num_two = int(input("Enter num two: "))
# print("Multiplication =", num_one * num_two)

# 4
my_text = input("Enter text: ")
mytable = str.maketrans("abcdefghijklmnoprstuvwxyz", "@8(D3F9H|JKLMN06R$TV^W*Y5")
print(my_text.casefold().translate(mytable))
