#section 1
#t1, t2: create class employee with instance variables name and salary and class variable company and use instance method display to print employee details.
class Employee:
    company_name = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", self.company_name)


emp1 = Employee("Ramya", 20000)
emp1.display()
print("\n")

#section 2
#t3: Create a class method to change company(cls, new_name) to update company name.
class Method:
    company_name = "TechCorp"

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


Method.change_company("wipro")
print(Method.company_name)
print("\n")

#t4:create class method from_string(cls,data) that input and returns employee object.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split("-")
        return cls(name, int(salary))

    def details(self):
        return f"name:{self.name}, salary:{self.salary}"


emp_str = "ramya-20000"
new_emp = Employee.from_string(emp_str)
print(new_emp.details())
print("\n")

#Section 3: Static Method
#t5: create a static method is valid_salary(salary) that checks if salary > 0 or not.
class Employee1:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def valid_salary(salary):
        if salary>0:
            return True
        else:
            return False
print(Employee1.valid_salary(25000))
print("\n")

#t6: create a static method greet_company() that prints a welcome message.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def greet_company():
        print("Welcome to TechCorp!")

Employee.greet_company()
print("\n")


#Section 4:Property Method(Getter only)
#t7 & t8:create a private variable __salary and a property methods salary and annual_salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = float(salary)
    @property
    def salary(self):
        return self.__salary
    @property
    def annual_salary(self):
        return self.__salary * 12
emp1= Employee("ramya",25000)
print("salary:",emp1.salary)
print("annual_salary:",emp1.annual_salary)
print("\n")

#Section 5 & 6: combined behaviour and Final integration
#t9:Creating multiple employee objects using normal constructor from_string() class methods display() and property access using static method.
#t10:create 3 employees , change company using classmethod validate salary using class method and print annual salary using property.
class Employee:
    company_name = "TechCorp"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")
        return cls(name, float(salary))
    @classmethod
    def change_company(cls, new_name):
        cls.new_name = new_name
    @staticmethod
    def valid_salary(salary):
        return salary > 0
    def annual_salary(self):
        return self.salary * 12
    def details(self):
        return f"name:{self.name}, salary:{self.salary}, annual salary:{self.annual_salary()}"
emp1= Employee("ramya",25000)
emp2= Employee("ram",25000)
emp3= Employee.from_string("pree-45000")  
Employee.change_company("wipro digital")
print(Employee.company_name)
employees=[emp1, emp2, emp3]
for emp in employees:
    if Employee.valid_salary(emp.salary):
        print(emp.details())
        print(f'annual salary of {emp.name} is {emp.annual_salary()}')
        print("\n")
