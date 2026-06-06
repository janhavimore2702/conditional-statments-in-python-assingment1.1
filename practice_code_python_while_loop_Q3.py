print(" WHILE LOOP IN PYTHON : ")


# Q1. Print numbers from 1 to 10 using a while loop

print("Q1. Numbers from 1 to 10:")
i = 1
while i <= 10:
    print(i)
    i += 1


# Q2. Print numbers from 10 to 1 in reverse order using a while loop

print("\nQ2. Numbers from 10 to 1:")
i = 10
while i >= 1:
    print(i)
    i -= 1


# Q3. Print all even numbers between 1 and 20 using a while loop

print("\nQ3. Even numbers between 1 and 20:")
i = 2
while i <= 20:
    print(i)
    i += 2


# Q4. Print all odd numbers between 1 and 20 using a while loop

print("\nQ4. Odd numbers between 1 and 20:")
i = 1
while i <= 20:
    print(i)
    i += 2


# Q5. Find the sum of numbers from 1 to 100 using a while loop

print("\nQ5. Sum of numbers from 1 to 100:")
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print("Sum =", total)


# Q6. Print the multiplication table of a given number using a while loop

print("\nQ6. Multiplication Table")
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1


# Q7. Count the number of digits in a given number using a while loop

print(" Q7. Count Digits")
num = int(input("Enter a number: "))
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num //= 10

print("Number of digits =", count)


# Q8. Reverse a given number using a while loop

print("Q8. Reverse a Number")
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number =", reverse)


# Q9. Find the factorial of a given number using a while loop

print("Q9. Factorial")
num = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print("Factorial =", factorial)


# Q10. Keep asking the user for a password until the correct password is entered

print("Q10. Password Check")
correct_password = "python123"
password = ""

while password != correct_password:
    password = input("Enter password: ")

print("Access Granted!")