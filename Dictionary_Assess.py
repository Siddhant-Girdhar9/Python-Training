bird = {}
value = None
bird.update({
    'name' : 'parrot',
    'color' : value,
    'breed': value,
    'legs': value,
    'age': value})
print(bird)

student = {}
student.update({
    'first_name': 'student1',
    'last_name' : value,
    'gender' : value,
    'age' : value,
    'marital_status' : value,
    'skills' : ['programming','coding'],
    'country' : value,
    'city' : value,
    'address' : value
})

len1 = len(student)

print(type(student['skills']))

keys = []
for key in student.keys():
    keys.append(key)
print(keys)

values= []
for value in student.values():
    values.append(value)
print(values)

student_items = list(student.items())
print(student_items)

student.popitem()
print(student)

print(bird)
del bird


