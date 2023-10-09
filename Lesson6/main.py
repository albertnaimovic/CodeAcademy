# 1. Create a list of different types of python objects, and print all the types. The one who gets the the most unique types wins respect points:

# my_list = ["a", 1, 1.543, [1, 3, 4], (1, 2, 3), {"name": "Albert"}, {1, 2, 3}, True]
# for item in my_list:
#     print(type(item))

# 2. print all the items separated with "|"

# my_list = ["a", 1, 1.543, [1, 3, 4], (1, 2, 3), {"name": "Albert"}, {1, 2, 3}, True]
# print(*my_list, sep = "|")

# 3. create a list of floats with 3 decimal points, create another list with all the values rounded to 2 decimals.

# my_list = [1.123, 6.432, 4.499]
# rounded_list = []

# for item in my_list:
#     rounded_list.append(round(item, 2))
# print(rounded_list)

# 4. Create a list with student names and sort them, print the result to the terminal.

# my_list = ["Petras", "Jonas", "Tomas", "Giedrius", "Andrius"]
# my_list = sorted(my_list)
# print(my_list)

# 5. write a program that allows user to write in any float number and then round it.

# any_float = input("Enter any float: ")
# float_check = any_float.isdecimal()
# if float_check == True:
#     print("Decimal")
# else:
#     print("Not decimal")

# if any_float == float_check:
#     print("Not float")
# else:
#     print("Float")



# We've got a very long string, containing a bunch of User IDs. This string is a listing, which seperates each user ID with a comma and a whitespace ("' "). 
# Sometimes there are more than only one whitespace. Keep this in mind! Futhermore, some user Ids are written only in lowercase,
# others are mixed lowercase and uppercase characters. Each user ID starts with the same 3 letter "uid", e.g. "uid345edj".
# But that's not all! Some stupid student edited the string and added some hashtags (#). User IDs containing hashtags are invalid, so these hashtags should be removed!

# Task
# 1.Remove all hashtags
# 2.Remove the leading "uid" from each user ID
# 3.Return an array of strings --> split the string
# 4.Each user ID should be written in only lowercase characters
# 5.Remove leading and trailing whitespaces

import re

income_list = "uidMultipleuid"

prefix = "uid"
list_without_uid = []

cleared = re.sub("[#]","", income_list)
split = cleared.split(",")

for item in split:
    delete_uid = item.index(prefix) + len(prefix)
    list_without_uid.append(item[delete_uid:].strip().lower())
    
print(list_without_uid)


# test.assert_equals(get_users_ids("uid12345"), ["12345"])
# test.assert_equals(get_users_ids("   uidabc  "), ["abc"])
# test.assert_equals(get_users_ids("#uidswagger"), ["swagger"])
# test.assert_equals(get_users_ids("uidone, uidtwo"), ["one", "two"])
# test.assert_equals(get_users_ids("uidCAPSLOCK"), ["capslock"])

# test.describe("Advanced tests")
# test.assert_equals(get_users_ids("uid##doublehashtag"), ["doublehashtag"])
# test.assert_equals(get_users_ids("  uidin name whitespace"), ["in name whitespace"])
# test.assert_equals(get_users_ids("uidMultipleuid"), ["multipleuid"])
# test.assert_equals(get_users_ids("uid12 ab, uid#, uidMiXeDcHaRs"), ["12 ab", "", "mixedchars"])
# test.assert_equals(get_users_ids(" uidT#e#S#t# "), ["test"])
