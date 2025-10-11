students_classA = ["John", "Mary", "Clinton", "Mary", "Paul", "John"]
students_classB = ["Grace", "Mary", "Paul", "James", "Clinton"]
print(set(students_classA))
print(set(students_classB))
students_classA = {'Paul', 'Mary', 'John', 'Clinton'}
students_classB = {'Mary', 'James', 'Grace', 'Clinton', 'Paul'}
print(students_classA.intersection(students_classB))
print(students_classA.union(students_classB))
print(students_classA.difference(students_classB))