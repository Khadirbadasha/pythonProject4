#Write a Python program to calculate the area of a circle given its radius using the formula
#area=π×r^2 ( Take pie as 3.14)

PI= 3.14
r = float(input("enter the radius of circle\n"))
area =PI*r*r
print("Area of circle=%.2f"%area)
#Create a program that takes two numbers as input and
# prints whether the first number is greater than, less than, or equal to the second number.
a = input("Enter the first number\n")
b = input("Enter the second\n")
print(a>b)
print(a<b)
print(a==b)
#Use the ternary operator to find the maximum of three numbers entered by the user
#it is if else
#age>18 you can vote
#age<18 you cannot vote
age=input("Enter you age")
age = int(age)
result = "yes you can vote" if age>18 else "cannot vote"
print(result)
#Develop a Python script that calculates the square and cube of a given number
num = int(input("enter the number\n"))
sq=num**2
print("squre of the given number",sq)
num2 = int(input("enter the number\n"))
cube =num**3
print("cube of the given number",cube)
