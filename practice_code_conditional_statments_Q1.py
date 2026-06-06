print("PYTHON CONDITIONAL STATMENTS : ")

print(" Q1. program  to find positive or negative")

a=int(input("enter any number to find positive or negative number:"))
if a>0:   #comparision operator
    print("positive:")
else:
    print("negative:")

print(" Q2. checking wheather the number is even or odd ")

b=int(input("enter any number to find even or odd :"))
if b%2==0:   #comparision operator
    print("even number:")
else:
    print("odd number:")

print(" Q3. program find greater number between two numbers ")

c=int(input("enter first number:"))
d=int(input("enter second number:"))
if c>d:      #comparision operator
    print(f"{c} is greater than {d} :")
else:
    print(f"{d} is greater than {c} :")

print(" Q4. checking whether the person os eligible to vote or not")

age=int(input("enter your age :"))
if age>=18:
    print(" you are eligile to vote :")
else:
    print("you are not eligible to vote:")

print(" Q5. checking whether the number is divisible by 5")

e=int(input("enter any number to check whether it is divisible to 5 or not :"))
if e%5==0:
    print("divisible by 5 :")
else:
    print("it is not divisible by 5 :")

print(" Q6. checking whether the year is leap or not:")

year=int(input("enter any year to check it is leap or not :"))
if year%4==0:
    print("it is a leap year :")
else:
    print("it is not a leap year :")

print(" Q7. checking whether the chaeacter is a vowel or not : ")

ch=(input("enter any character to check it is a vowel or not :"))
if ch.lower() in ('a','e','i','o','u'):       #built-in function
    print("vowels :")
else:
    print("it is a constant character :")

print(" Q8. program to find the largest among three numbers :")

num1=int(input("enter first number to check it is greater or not among three numbers :"))
num2=int(input("enter second number to check it is greater or not among three numbers :"))
num3=int(input("enter third number to check it is greater or not among three numbers :"))

if num1>=num2 and num1>=num3:           #logical operator
    print(f"{num1} is the greatest number among {num2} and {num3}")
elif num2>=num1 and num2>=num3 :
    print(f"{num2} is the greatest number among {num1} and {num3}")
else:
    print(f"{num3} is the greatest among {num1} and {num2}")

print(" Q9. assingning grades based on marks :" )
marks=int(input("enter your marks :"))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("fail ")

print(" Q10. to check whether the number is in the range 1 to 100 :")

num=int(input("enter the number you want to check :"))
if 1<= num <= 100:
    print("number is within range 1 to 100 :")
else:
    print("numer is not in range from 1 to 100 :")