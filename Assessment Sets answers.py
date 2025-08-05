
# Sum of positive number until user inputs zero

li = []
while True:
    num = input("Enter the number : ")
    if num == '0':
        break
    li.append(num)

for number in li:
    tracker = False
    li = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for c in number:
        if c not in li:
            tracker = True
        break
    if number == "" or tracker:
        continue
    if int(number) < 0:
        continue

    sum += int(number)
print(sum)

# FLATTEN DICTIONARY

data = {"a": 1, "b": {"x": 2, "y": 3}}
flattened = {}

for key, value in data.items():
    if isinstance(value, dict):
        for subkey, subvalue in value.items():
            flattened[f"{key}.{subkey}"] = subvalue
    else:
        flattened[key] = value

print(flattened)

# HOLLOW PYRAMID

n = 5

for i in range(1, n + 1):
    print((n - i) * " ", end="")
    print(1, end=" ")
    if (i) == n:
        for k in range(2, n + 1):
            print(k, end=" ")
    for j in range(1, i):
        if i - (j + 1) == 0 and i != n:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()

# CALCULATE BMI

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your wieght in kgs: "))
bmi = weight / (height * height)
print(bmi)

# count of even odd from a list
lst1 = input("Enter the list of numbers: ").split()
lst2 = [int(i) for i in lst1]  ##lst2 = list(map(int, lst1))

even_counter = 0
odd_counter = 0
for i in lst2:
    if i % 2 == 0:
        even_counter += 1
    elif i % 2 == 1:
        odd_counter += 1

print(f"The number of even numbers is: {even_counter}")
print(f"The number of odd numbers is: {odd_counter}")

## Login Validation

username = input("Enter your username: ")

correct = {"username": "admin", "password": "admin@123"}
if username == correct["username"]:
    password = input("Enter your password: ")
    if password == correct["password"]:
        print("Access granted")
    else:
        print("Invalid password")
else:
    print("Access denied")

# FLATTEN DICTIONARY

data = {"x": 10, "y": {"a": 5, "b": {"z": 1}}}
# {'x': 10, 'y.a': 5, 'y.b.z': 1}
flattened = {}
for key, value in data.items():
    if isinstance(value, dict):
        for subkey, subvalue in value.items():
            if isinstance(subvalue, dict):
                for subsubkey, subsubvalue in subvalue.items():
                    flattened[f"{key}.{subkey}.{subsubkey}"] = subsubvalue
            else:
                flattened[f"{key}.{subkey}"] = subvalue
    else:
        flattened[key] = value

print(flattened)

# HOURGLASS PATTERN

n = 5

for i in range(n):
    for j in range(i + 1):
        print(" ", end="")
    for j in range(i, n - 1):
        print("*", end="")
    for j in range(i, n):
        print("*", end="")

    print()
for i in range(n - 1, 0, -1):
    for j in range(i):
        print(" ", end="")
    for j in range(i, n + 2):
        print("*", end="")
    for j in range(i, n - 1):
        print("*", end="")

    print()

# Add Two Floats and Print Boolean

x = float(input("Enter a float value: "))
y = float(input("Enter another float value: "))
hundred = x + y > 100
print(f" Their sum is 100 : {hundred}")

# Reverse list manually

x = input("Enter a list of numbers seperated by space: ").split()
str1 = list(map(int, x))
str2 = []

for i in str1:
    str3 = str2.insert(0, i)
print(str2)

# Leap Year Checker


year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# FLATTEN DICTIONARY


data = [{'a': 1}, {'b': 2, 'c': 3}, {'d': {'e': 4}}]
# {'a': 1, 'b': 2, 'c': 3, 'd.e': 4}
flattened = {}
for item in data:
    for key, value in item.items():
        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                flattened[f"{key}.{subkey}"] = subvalue
        else:
            flattened[key] = value

print(flattened)

# DIAMOND STAR PATTERN

n = 5

for i in range(n):
    for j in range(i, n):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    for j in range(i):
        print("*", end="")

    print()

for i in range(n):
    if i == 0:
        continue
    for j in range(i + 1):
        print(" ", end="")
    for j in range(i + 1, n):
        print("*", end="")
    for j in range(i, n):
        print("*", end="")
    print()

# Simple Calculator


x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
op = input("Choose any operation ( +, -, *, /): ")
if op == "+":
    print("Addition : ", end="")
    print(x + y)
elif op == "-":
    print("Subtraction : ", end="")
    print(x - y)
elif op == "*":
    print("Multiplication : ", end="")
    print(x * y)
else:
    print("Division : ", end="")
    print(x / y)

# Float list

flt_lst = list(map(float, input("Enter the values seperated by space: ").split()))
sum1 = 0
len1 = 0
for i in flt_lst:
    sum1 += i
    len1 += 1

avg = sum1 / len1
print("The average is: ", avg)
res = avg > 60
print("Is it greater than 60 : ", res)

# Login attempt Limit


i = 0
username = input("Enter your username : ")
correct = {"username": "admin", "password": "password"}
if username == correct["username"]:
    while i < 3:
        i = i + 1
        password = input("Enter your password : ")
        if password == correct["password"]:
            print("Welcome " + username + "!")
            break
        else:
            if i == 3:
                print("Your account has been locked as you have exceeded the maximum limit of login attempts")
                break
            print("Wrong password!, Try Again")

else:
    print("Wrong username!, Try Again")

# Recursive Dictionary


# Pascal Triangle PATTERN


# AREA CALCULATOR

shape = input("Enter a shape (circle or square): ")
if shape == "circle":
    radius = float(input("Enter a radius: "))
    area = 3.14 * radius * radius
    print("The area of the circle is", area)
elif shape == "square":
    side = float(input("Enter a side: "))
    area = side * side
    print("The area of the square is", area)
else:
    print("Invalid shape")

    FLATTEN FULL DICTIONARY
    AND
    SORT
    AESC

data = [{'a': {'x': 5, 'y': 3}, 'b': 1, 'c': {'z': 2}}]
flattened = {}

for item in data:
    for key, value in item.items():
        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                flattened[f"{key}.{subkey}"] = subvalue
        else:
            flattened[f"{key}"] = value

sorted_items = sorted(flattened.items(), key=lambda item: item[1])

print(sorted_items)



