# import math
#
# bird = {}
# value = None
# bird.update({
#     'name' : 'parrot',
#     'color' : value,
#     'breed': value,
#     'legs': value,
#     'age': value})
# print(bird)
#
# student = {}
# student.update({
#     'first_name': 'student1',
#     'last_name' : value,
#     'gender' : value,
#     'age' : value,
#     'marital_status' : value,
#     'skills' : ['programming','coding'],
#     'country' : value,
#     'city' : value,
#     'address' : value
# })
#
# len1 = len(student)
#
# print(type(student['skills']))
#
# keys = []
# for key in student.keys():
#     keys.append(key)
# print(keys)
#
# values= []
# for value in student.values():
#     values.append(value)
# print(values)
#
# student_items = list(student.items())
# print(student_items)
#
# student.popitem()
# print(student)
#
# print(bird)
# del bird

######################## Exercises on Functions

#area and perimeter of circle

# def circle(rad):
#     area = 2 * 3.14 * rad
#     peri = 3.14 * rad * rad
#     return (area, peri)
#
# print(circle(3))

# add all nums

# def addall(*args):
#     ad = 0
#     for arg in args:
#         ad += arg
#     return(ad)
# print(addall(1,2,3))

# fahrenheit to celsius conversion
# def convert_celsius_2_fahrenheit(cel):
    # return (cel - 32) * 5/9
# print(convert_celsius_2_fahrenheit(32))
#
# #checking sesason through month
# def check_season(month):
#     month = month.lower()
#     if month in ['december','january','february']:
#         return 'Winter'
#     elif month in ['march','april','may']:
#         return 'Spring'
#     elif month in ['june','july','august']:
#         return 'Summer'
#     elif month in ['september','october','november']:
#         return 'Autumn'
#
# print(check_season('january'))

# calculating slope

# def calculate_slope(x1,y1,x2,y2):
#     if x2 - x1 == 0:
#         print("Line is Vertical")
#     slope = (y2-y1)/(x2-x1)
#     return slope
# print(calculate_slope(1,2,3,4))

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

# import math
#
#
# def solve_quadratic_eqn(a, b, c):
#     if a == 0:
#         return "Not a quadratic equation (a cannot be zero)."
#
#     discriminant = b ** 2 - 4 * a * c
#
#     if discriminant > 0:
#         root1 = (-b + math.sqrt(discriminant)) / (2 * a)
#         root2 = (-b - math.sqrt(discriminant)) / (2 * a)
#         return (root1, root2)  # Two real and distinct roots
#
#     elif discriminant == 0:
#         root = -b / (2 * a)
#         return (root,)  # One real repeated root (note the comma makes it a tuple)
#
#     else:
#         return "No real solutions"

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

# def print_list(lst):
#     lst = list(lst)
#     for i in lst:
#         print(i)
# a = [1,'banana',3,4,5]
# print_list(a)

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

# def reverse_list(arr):
#     reversed_arr = []
#     for i in range(len(arr) - 1, -1, -1):
#         reversed_arr.append(arr[i])
#     return reversed_arr
# print(reverse_list([1, 2, 3]))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

# def capitalize_list_items(list1):
#     capitalized_list = []
#     for item in list1:
#         if isinstance(item, str):
#             capitalized_list.append(item.capitalize())
#         else:
#             capitalized_list.append(item)
#
# print(capitalize_list_items(['apple','banana']))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

# def add_item(list1 , add):
#     list1.append(add)
#     return list1
#
# print(add_item([1,2,3,4,5],'apple'))

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

# def remove_item(list1,item):
#     list1.remove(item)
#     return list1
#
# print(remove_item([1,2,3,4,5],5))

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

# def sum_of_numbers(num):
#     sum = 0
#     for i in range(num+1):
#         sum += i
#     return sum
#
# print(sum_of_numbers(10))

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

# def sum_of_odds(num):
#     sum = 0
#     for i in range(num+1):
#         if i % 2 != 0:
#             sum += i
#     return sum
#
# print(sum_of_odds(10))

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

# def sum_of_even(num):
#     sum = 0
#     for i in range(num+1):
#         if i % 2 == 0:
#             sum+=i
#     return sum
#
# print(sum_of_even(10))

################ level 2 ############

# Declare a function named evens_and_odds. It takes a positive integer as parameter and it counts number of evens and odds in the number.

# def evens_and_odds(num):
#     even_counter = 0
#     odd_counter = 0
#     for i in range(1,num+1):
#         if i % 2 == 0:
#             even_counter += 1
#         elif i % 2 != 0:
#             odd_counter += 1
#     return (even_counter, odd_counter)
#
# print(evens_and_odds(10))

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(4))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not

# def is_empty(arr):
#     if len(arr) == 0:
#         return True
# x=[]
# print(is_empty(x))

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std

# def calculate_mean_median_mode(list1):
#     list1 = list(list1)
#     mean = sum(list1)/len(list1)
#     mode = 0
#     d1 = {}
#     if len(list1) % 2 != 0:
#         median = list1[int(len(list1)/2)]
#     else:
#         median = (list1[int(len(list1)/2-1)] + list1[int(len(list1)/2)]) / 2
#     for i in list1:
#         if i in d1.keys():
#             d1[i] += 1
#         else:
#             d1[i] = 1
#     max_val = max(d1.values())
#     mode = [k for k,v in d1.items() if v == max_val]
#     return (mean,median,mode)
# x = [2,4,6,6,8,10,12]
# print(calculate_mean_median_mode(x))

def calculate_range(data):
    return max(data) - min(data)

def calculate_variance(data):
    n = len(data)
    mean = sum(data) / n
    squared_diffs = [(x - mean) ** 2 for x in data]
    return sum(squared_diffs) / (n - 1)

def calculate_std(data):
    variance = calculate_variance(data)
    return variance ** 0.5

############################### level 3

# def is_prime(n):
#     if n <= 1:
#         return False  # 0 and 1 are not prime
#     if n == 2:
#         return True   # 2 is the only even prime number
#     if n % 2 == 0:
#         return False  # exclude all other even numbers
#
#     # check for factors from 3 to √n (skip even numbers)
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False

# Write a functions which checks if all items are unique in the list.
#
# def all_unique(items):
#     return len(items) == len(set(items))

# WAF which checks if there are different type of data present in list.
# def all_same_type(items):
#     if not items:
#         return True  # empty list → considered uniform
#     first_type = type(items[0])
#     for item in items:
#         if type(item) != first_type:
#             return False
#     return True

#Write a function which check if provided variable is a valid python variable

# import keyword
#
# def is_valid_variable(name):
#     if not isinstance(name, str):
#         return False
#     if not name.isidentifier():
#         return False
#     if keyword.iskeyword(name):
#         return False
#     return True






