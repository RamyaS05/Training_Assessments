#assignment operators
x=10
x+=5  
print(x)
x-=4
print(x)
x*=2
print(x)
x//=3
print(x)

#Bitwise Operators   
a,b= 5, 3
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 2)
print(a >> 2)

#string slicing
s="DataScienceIsAwesome12345"
print(s[4:11])
print(s[:13]+s[13:20][::-1]+s[20:])
print(s[::2])
print(s[::-5])
new_string= s[:4][::-1]+s[4:-4]+s[-4:][::-1]
print(new_string)

#Student Data
name=input("enter your name: ")
age=int(input("enter your age: "))
marks=list(map(int, input("enter your marks : ").split()))
subjects= input("enter your subjects: ").split()
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Subjects:", subjects)

#Data Structures
marks= [85, 90, 78, 92]
tuple_marks= tuple(marks)
print(tuple_marks)
set_marks= set(marks)
print(set_marks)
student_data={"name": "ramya", "age": 21, "marks": [50,45], "subjects": ["maths", "science"]} 
print(student_data)

#Slicing
print("first 2:", marks[:2])
print("last 2:", marks[-2:])
print("reversed:", marks[::-1])

#arithmetic operators
total=sum(marks)
average= total/len(marks)
if average >= 75:
    result= "Distinction"
elif average >= 50 and average < 75:
    result= "Pass"
else:
    result= "Fail"
print("Total:", total)
print("Average:", average)
print("Result:", result)

#Mutable and Immutable
marks.append(100)
marks.insert(1,50)
print(marks)
set_marks.add(100)
print(set_marks)

#Membership and Identity Operators
a= [1, 2]
b= [1, 2]
print(a == b)
print(a is b)

#Bitwise Operators
a,b= 5, 3
print(a & b)
print(a | b)
print(a ^ b)
print(a<<1)
print(a>>1)

#Functions
def calculate_total(marks):
    return sum(marks)
def calculate_average(marks):
    total= calculate_total(marks)
    return total/len(marks)
def get_result(average):
    if average >= 75:
        return "Distinction"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"
total= calculate_total(marks)
average= calculate_average(marks)
result= get_result(average)

#Even or Odd
num= int(input("enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#largest of three numbers
a= int(input("enter first number: "))
b= int(input("enter second number: "))
c= int(input("enter third number: "))
if a >= b and a >= c:
    largest= a
elif b >= a and b >= c:
    largest= b
else:
    largest= c
print("Largest number:", largest)

#grade system
marks= int(input("enter your marks: "))
if marks >= 75:
    print("distinction")
elif marks >= 50:
    print("pass")
else:
    print("fail")

#for loop
for i in range(1, 11):
    print(i)

#sum of numbers
n= int(input("enter a number: "))
sum= 0
i=1
while i <= n:
    sum += i
    i += 1
print("Sum of 1 to", n, "is:", sum)


#skip multiples of 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

#stop at first negative number
nums=[5, 10, 15, -2, 20]
for n in nums:
    if n < 0:
        break
    print(n)

#Multiplication table
n1=int(input("enter a number: "))
for i in range(1, 11):
    print(n1*i)

#Prime number
n2=int(input("enter a number: "))
if n2 <=1:
    print("Not prime")
else:
    for i in range(2, n2):
        if n2 % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")


#Nested loops
for i in range(1, 6):
    for j in range(1, i):
        print("*", end="")
    print()


#Basic function
def welcome():
    print("Welcome to student system")
welcome()

#function with parameters
def get_total(marks):
    return sum(marks)
marks= [85, 90, 78]
total= get_total(marks)
print("Total marks:", total)

#function with default argument
def greet(name="pree"):
    return f'Hello, {name}'
print(greet())

#function with multiple returns
def calculate(marks):
    total= sum(marks)
    average= total/len(marks)
    return total, average
marks1= [85, 90, 78]
total, average= calculate(marks1)
print("Total:", total)
print("Average:", average)

#function with args
def total_marks(*marks):
    return sum(marks)
result= total_marks(85, 90, 78)
print("Total marks:", result)

#function with kwargs
def student_info(**data):
    print(data)
info=student_info(name="Ramya", age=21, marks=[85, 90], subjects=["maths", "science"])

#lambda function
square= lambda x: x*x
marks2= [85, 90, 78]
squared_marks= list(map(square, marks2))
print("Squared marks:", squared_marks)

#High-order function
def apply_operation(func, value):
    return func(value)
result= apply_operation(lambda x: x*x,6)
print("Result:", result)

#Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num= int(input("enter a number: "))
print("Factorial of", num, "is:", factorial(num))

#mutable and immutable
def modify_list(lst):
    lst.append(100)
def modify_num(x):
    x += 10
    return x
my_list= [10, 20, 30]
modify_list(my_list)
print("after modifying list:",my_list)
my_num=50
modify_num(my_num)
print("after modifying number:",num)

#Input handling
name= input("enter your name: ")
marks= list(map(int, input("enter your marks: ").split()))
print("Name:", name)
print("Marks:", marks)

#External module usage
import math
print(math.sqrt(sum(marks)))

#student report
print("\nStudent Report")
print("Name:", name)
print("Marks:", marks)
print("Total:", sum(marks))
print("Average:", sum(marks)/len(marks))
print("result:",result)