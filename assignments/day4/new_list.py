# list of students with details
students = [{'name':'Sarah', 'gender':'female', 'age': 20},
{'name':'Peter', 'gender':'male', 'age': 25},
{'name':'Mark', 'gender':'male', 'age': 22},
{'name':'Jane', 'gender':'female', 'age': 28},
{'name':'John', 'gender':'male', 'age': 23},
{'name':'Mary', 'gender':'female', 'age': 30}
]
# print the original list
print("\n \nOriginal list of dictionaries :\n ")
print(students)
# sort list by age from oldest to youngest
sorted_students = sorted(students, key = lambda student: student['age'],reverse=True)
# print the sorted list 
print("\n \nSorted List of dictionaries : \n ")
print(sorted_students)
