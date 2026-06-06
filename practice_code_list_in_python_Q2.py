print(" LIST IN PYTHON ")


# Q1: Create a list of 10 numbers and print all the elements

print("Q1: Create a list of 10 numbers and print all the elements")

def create_list():
    numbers = []
    print("Enter 10 numbers:")
    for i in range(1, 11):
        num = int(input(f"  Enter number {i}: "))
        numbers.append(num)
    return numbers

numbers = create_list()
print("Your List:", numbers)

# Q2: Find the largest element in a list

print("\nQ2: Find the largest element in a list")

def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

print(f"Largest element: {find_largest(numbers)}")

# Q3: Find the smallest element in a list

print("\nQ3: Find the smallest element in a list")

def find_smallest(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

print(f"Smallest element: {find_smallest(numbers)}")

# Q4: Calculate the sum of all elements in a list

print("\nQ4: Calculate the sum of all elements in a list")

def calculate_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

print(f"Sum of all elements: {calculate_sum(numbers)}")

# Q5: Calculate the average of all elements in a list

print("\nQ5: Calculate the average of all elements in a list")

def calculate_average(lst):
    return calculate_sum(lst) / len(lst)

print(f"Average of all elements: {calculate_average(numbers):.2f}")

# Q6: Count how many even numbers are present in a list

print("\nQ6: Count how many even numbers are present in a list")

def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

print(f"Count of even numbers: {count_even(numbers)}")

# Q7: Create a new list containing only the odd numbers

print("\nQ7: Create a new list containing only the odd numbers")

def get_odd_numbers(lst):
    odd_list = []
    for num in lst:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list

print(f"Odd numbers: {get_odd_numbers(numbers)}")

# Q8: Find whether a given element exists in a list

print("\nQ8: Find whether a given element exists in a list")

def search_element(lst):
    element = int(input("Enter the element to search: "))
    if element in lst:
        print(f"{element} EXISTS in the list.")
    else:
        print(f"{element} does NOT exist in the list.")

search_element(numbers)

# Q9: Reverse a list without using built-in reverse functions

print("\nQ9: Reverse a list without using built-in reverse functions")

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print(f"Reversed List: {reverse_list(numbers)}")

# Q10: Find the second largest element in a list

print("\nQ10: Find the second largest element in a list")

def find_second_largest(lst):
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    if len(unique) < 2:
        return "Not enough unique elements to find second largest"
    largest = second_largest = None
    for num in unique:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest

print(f"Second largest element: {find_second_largest(numbers)}")