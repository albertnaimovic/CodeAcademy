my_list = []
list_less_than_50 = []
my_tuple = []

for num in range(10):
    my_list.append(int(input(f"Enter number {num+1}: ")))

for number in my_list:
    if number < 50:
        list_less_than_50.append(number)
    else:
        my_tuple.append(number)

my_difference = max(list_less_than_50) - min(list_less_than_50)
print(f"Difference between the highest and lowest number in list: {my_difference}")

tuple(my_tuple)
my_sum = sum(my_tuple)
print(f"Sum of numbers from tuple: {my_sum}")
