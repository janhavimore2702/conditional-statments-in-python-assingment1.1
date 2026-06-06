
print("PYTHON FUNCTIONS : ")

# Q1: Check whether a number is positive, negative, or zero

print("Q1: Check whether a number is positive, negative, or zero")
number = int(input("Enter a number: "))

def check_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(check_sign(number))

# Q2: Check whether a number is even or odd

print("\nQ2: Check whether a number is even or odd")
number = int(input("Enter a number: "))

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(number))

# Q3: Accept two numbers and return the greater number

print("\nQ3: Accept two numbers and return the greater number")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def find_greater(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both are equal"

print(f"Greater number: {find_greater(a, b)}")

# Q4: Check whether a person is eligible to vote (age >= 18)

print("\nQ4: Check whether a person is eligible to vote (age >= 18)")
age = int(input("Enter your age: "))

def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

print(check_voting_eligibility(age))

# Q5: Check whether a number is divisible by 5

print("\nQ5: Check whether a number is divisible by 5")
number = int(input("Enter a number: "))

def check_divisible_by_5(number):
    if number % 5 == 0:
        return f"{number} is divisible by 5"
    else:
        return f"{number} is not divisible by 5"

print(check_divisible_by_5(number))

# Q6: Check whether a given year is a leap year or not

print("\nQ6: Check whether a given year is a leap year or not")
year = int(input("Enter a year: "))

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a Leap Year"
    else:
        return f"{year} is not a Leap Year"

print(check_leap_year(year))

# Q7: Check whether a character is a vowel or a consonant

print("\nQ7: Check whether a character is a vowel or a consonant")
char = input("Enter a character: ")

def check_vowel_or_consonant(char):
    char = char.lower()
    if char in "aeiou":
        return f"'{char}' is a Vowel"
    elif char.isalpha():
        return f"'{char}' is a Consonant"
    else:
        return "Not a valid alphabet character"

print(check_vowel_or_consonant(char))

# Q8: Find the largest among three numbers

print("\nQ8: Find the largest among three numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(f"Largest number: {find_largest(a, b, c)}")

# Q9: Calculate the sum of numbers from 1 to 100

def sum_1_to_100():
    total = 0
    for i in range(1, 101):
        total += i
    return total

print("\nQ9: Calculate the sum of numbers from 1 to 100")
print(f"Sum = {sum_1_to_100()}")

# Q10: Print the multiplication table of a given number

print("\nQ10: Print the multiplication table of a given number")
number = int(input("Enter a number: "))

def multiplication_table(number):
    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        print(f"  {number} x {i} = {number * i}")

multiplication_table(number)

# Q11: Calculate and return the square of a number

print("\nQ11: Calculate and return the square of a number")
number = int(input("Enter a number: "))

def calculate_square(number):
    return number ** 2

print(f"Square of {number} = {calculate_square(number)}")

# Q12: Calculate the factorial of a number using a loop

print("\nQ12: Calculate the factorial of a number using a loop")
number = int(input("Enter a number: "))

def calculate_factorial(number):
    if number < 0:
        return "Factorial not defined for negative numbers"
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

print(f"Factorial of {number} = {calculate_factorial(number)}")

# Q13: Check whether a number is prime

print("\nQ13: Check whether a number is prime")
number = int(input("Enter a number: "))

def check_prime(number):
    if number < 2:
        return f"{number} is not a Prime number"
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return f"{number} is not a Prime number"
    return f"{number} is a Prime number"

print(check_prime(number))

# Q14: Calculate the sum of digits of a number

print("\nQ14: Calculate the sum of digits of a number")
number = int(input("Enter a number: "))

def sum_of_digits(number):
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

print(f"Sum of digits of {number} = {sum_of_digits(number)}")

# Q15: Accept a number n and return the sum of all numbers from 1 to n

print("\nQ15: Accept a number n and return the sum of all numbers from 1 to n")
n = int(input("Enter a number n: "))

def sum_1_to_n(n):
    if n < 1:
        return "Please enter a positive integer"
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(f"Sum from 1 to {n} = {sum_1_to_n(n)}")