# Basic Variables& Data types
name= "Ramya"
age= 21
height= 5.4
is_student= True
extra_info= None

#Arithmetic Operations
a= 10
b= 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

#Assignment Operators
score=50
score += 10  
print(score)
score -= 5  
print(score)
score *= 2
print(score)
score /= 4
print(score)

#Comparison Operators
age1= 25
age2= 30
print(age1 == age2)
print(age1 != age2)
print(age1 > age2)
print(age1 < age2)
print(age1 >= age2)
print(age1 <= age2)
print(age1 > 20 and age2 > 20)
print(age1 > 20 or age2 > 20)

#Bitwise Operators
x= 5
y= 10
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << 2)
print(x >> 2)

#Membership and Identity Operators
text="python programming"
print("python" in text)

list1= [1, 2, 3]
list2= [1, 2, 3]
print(list1== list2)
print(list1 is list2)

# Collection
#list
subjects= ["Math", "Science", "History"]
subjects.append("English")
print(subjects)

#tuple
tuple1= ("Math", "Science", "English")
print(tuple1)

#dictionary
student= {"name": "Ramya", "age": 21, "marks":{"maths": 85, "science": 90}, "subjects":["maths","science"]}
print(student)

#set
subjects_set= {"Math", "Science","Math", "History"}
print(subjects_set)

#report
print("Name:", student["name"])
print("Age:", student["age"])
print("Marks:", student["marks"])
print("Subjects:", student["subjects"])
print("sum of marks:", student["marks"]["maths"] + student["marks"]["science"])
print("Average marks:", (student["marks"]["maths"] + student["marks"]["science"]) / 2)
print("Results:", "Pass" if (student["marks"]["maths"] >= 40 and student["marks"]["science"] >= 40) else "Fail")