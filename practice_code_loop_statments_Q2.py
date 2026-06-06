print("LOOPING STATMENTS IN PYTHON : ")


#1.	Write a program to print numbers from 1 to 10 using a for loop. 

print(" Q1. print numbers from 1 to 10 using for loop :")

for a in range(1,11):
    print(a)

#2.	Write a program to print numbers from 10 to 1 in reverse order. 
    
print(" Q2. print numbers from 10 to 1 in reverse : ")

for b in range(10,0,-1):
    print(b)

#3.	Write a program to print all even numbers between 1 and 20. 

print(" Q3. print all even numbers between 1 to 20 : ")

for c in range(2,21,2):
    print(c)

#4.	Write a program to print all odd numbers between 1 and 20. 

print(" Q4. print all odd numbers between 1 to 20 :")

for d in range(1,21,2):
    print(d)

#5.	Write a program to find the sum of numbers from 1 to 100. 

print(" Q5. sum of all numbers from 1 to 100 : ")

sum=0
for e in range(1,101):
    sum=sum+e
    print("sum=",sum)

#6.	Write a program to print the multiplication table of a given number. 

print(" Q6. print the multiplication table of a given number :")

num=int(input("enter number to do the multliplication table :"))
for f in range(1,11):
    print(num,"x",f,"=",num*f)

#7.	Write a program using nested for loops to print pattern

print(" Q7. pattern using nested for loop :")

for g in range(1,6):
    for h in range(g):
        print("*",end=" ")
    print()

#8.	Write a program to print each character of a string using a for loop. 

print(" Q8. each character of string using for loop : ")

text=input("enter a string to print each character :")
for ch in text:
    print(ch)

#9.	Write a program to find the factorial of a given number using a for loop. 

print(" Q9. find the factorial of a given number :")

num=int(input("enter any number to find factorial of it :"))
fact=1
for i in range(1,num+1):
    fact*=1
print("factorial=",fact)

#10. Write a program to print the following pattern:

print(" Q10. print the following pattern :")

for j in range(5,0,-1):
    for s in range(j):
        print("*",end=" ")
    print()