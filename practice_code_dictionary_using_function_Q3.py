print("PYTHON DICTIONARY USING FUNCTIONS :")

# Q1: Create a dictionary to store a student's name, age, and city

print("Q1: Create a dictionary to store a student's name, age, and city")

def create_student_dict():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    city = input("Enter student city: ")
    student = {"name": name, "age": age, "city": city}
    return student

student = create_student_dict()
print("Student Dictionary:", student)

# Q2: Print all the keys of a dictionary

print("\nQ2: Print all the keys of a dictionary")

def print_keys(dictionary):
    print("Keys:", list(dictionary.keys()))

print_keys(student)

# Q3: Print all the values of a dictionary

print("\nQ3: Print all the values of a dictionary")

def print_values(dictionary):
    print("Values:", list(dictionary.values()))

print_values(student)

# Q4: Add a new key-value pair to an existing dictionary

print("\nQ4: Add a new key-value pair to an existing dictionary")

def add_key_value(dictionary):
    key = input("Enter new key to add: ")
    value = input(f"Enter value for '{key}': ")
    dictionary[key] = value
    return dictionary

student = add_key_value(student)
print("Updated Dictionary:", student)

# Q5: Update the value of an existing key in a dictionary

print("\nQ5: Update the value of an existing key in a dictionary")

def update_value(dictionary):
    key = input("Enter key to update: ")
    if key in dictionary:
        new_value = input(f"Enter new value for '{key}': ")
        dictionary[key] = new_value
        print("Dictionary after update:", dictionary)
    else:
        print(f"Key '{key}' not found in dictionary.")
    return dictionary

student = update_value(student)

# Q6: Check whether a given key exists in a dictionary

print("\nQ6: Check whether a given key exists in a dictionary")

def check_key_exists(dictionary):
    key = input("Enter key to check: ")
    if key in dictionary:
        print(f"Key '{key}' EXISTS in the dictionary.")
    else:
        print(f"Key '{key}' does NOT exist in the dictionary.")

check_key_exists(student)

# Q7: Remove a key-value pair from a dictionary

print("\nQ7: Remove a key-value pair from a dictionary")

def remove_key(dictionary):
    key = input("Enter key to remove: ")
    if key in dictionary:
        dictionary.pop(key)
        print(f"Key '{key}' removed. Updated Dictionary:", dictionary)
    else:
        print(f"Key '{key}' not found in dictionary.")
    return dictionary

student = remove_key(student)

# Q8: Count the total number of key-value pairs in a dictionary

print("\nQ8: Count the total number of key-value pairs in a dictionary")

def count_pairs(dictionary):
    return len(dictionary)

print(f"Total key-value pairs: {count_pairs(student)}")

# Q9: Iterate through a dictionary and print all keys and values

print("\nQ9: Iterate through a dictionary and print all keys and their values")

def print_all_keys_values(dictionary):
    print("Key-Value pairs:")
    for key, value in dictionary.items():
        print(f"  {key} : {value}")

print_all_keys_values(student)


# Q10: Dictionary of student names and marks, find the highest scorer

print("\nQ10: Find the student with the highest marks")

def find_highest_scorer():
    n = int(input("How many students do you want to enter? "))
    students = {}
    for i in range(n):
        name = input(f"Enter name of student {i + 1}: ")
        marks = int(input(f"Enter marks of {name}: "))
        students[name] = marks
    print("\nStudent Marks Dictionary:", students)
    top_student = max(students, key=students.get)
    print(f"Highest scorer: {top_student} with {students[top_student]} marks")

find_highest_scorer()