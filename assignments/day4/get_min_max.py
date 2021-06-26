def max_min_list_tuples(students):
    return_max = max(students,key=lambda item:item[1])[1]
    return_min = min(students,key=lambda item:item[1])[1]
    return return_max, return_min
    
students = [('Jane', 70), ('John', 68), ('Peter', 54), ('Mary', 71), ('Sarah', 84), ('Mark', 50)]
print("\n \n Original list with tuples:")
print(students)
print("\n Maximum and minimum values of the said list of tuples:")
print(max_min_list_tuples(students))