#delete --> use (del) keyword
"""class Student:
    def __init__(self,name):
        self.name = name
        print("added to db")

s1 = Student("mohak")
print(s1.name)
del s1.name #object's property delete
print(s1.name)
del s1#object delete
print(s1)"""


"""
class Bank:
    def __init__(self,name,acc_no,password):
        self.name = name
        self.acc_no = acc_no
        # self.password = password #public attribute
        self.__password = password #private attribute
    
    def details(self):
        print("name:",self.name,"account no:",self.acc_no)

    # def reset_passord(self):
    #     print("last password:",self.__password)

    def verification(self):
        print("approved")
        self.__reset_password()
    
    def __reset_password(self):
        print("last password:",self.__password)

obj = Bank("Mohak","12345",12345)
# print(obj.password)

#private --> add (__) two underscore before attribute

#obj.reset_password()#private attributes can be accessed using function which are defined in the class

#calling private method
obj.verification()
"""

#Inheritance
"""
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started...")

    def stop():
        print("car stopped...")
    

class ChildCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ChildCar("car1")
print(car1.name)
car1.start()#--> accessing parent class methods
print(car1.color)#-->accessing parent class attributes
"""

#types --> (i). single inheritance = 1 child 1 parent
#      --> (ii). mutlti-level inheritance = 1 parent se 1 child se 1 child se 1 child 
#      --> (iii). multiple inheritance

#multi-level inheritance

"""
class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")

    def stop():
        print("car stopped...")
    

class ChildCar(Car):
    def __init__(self,name,type):
        self.name = name
        # self.type = type#it will create another attribute inside child class
        #accssing parent class type
        super().__init__(type)#using attribute from parent class
        super().start()

car1 = ChildCar("car1","petrol")
print(car1.type)#value goes to childCar
"""

"""
class Person:
    name = "none"

    def changingNameOfObject(self,name):
        self.name = name#this will create a new attrubute for the current function and class attribute will be intact

    # def changingNameOfClass(self,name):
    #     #Person.name = name
    #     #or
    #     self.__class__.name = name
    #or a better approach is that, we can use class methods
    #classmethods = use @classmethod decorator for wrapping function made to use class attributes
    @classmethod
    def classMethodEx(cls,name):
        cls.name = name

p1 = Person()
p1.changingNameOfObject("mohak")
print(p1.name)
print(Person.name)

#p1.changingNameOfClass("Mohak")
#print(Person.name)

p1.classMethodEx("Mohak")
print(Person.name)
"""

"""
class Student:
    def __init__(self,marks1,marks2,marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        #self.persentage = str((self.marks1+self.marks2+self.marks3)/3) + "%"

    # def persentageCalc(self):
    #     self.persentage = str((self.marks1+self.marks2+self.marks3)/3) + "%"

    @property
    def persentage(self):
        return str((self.marks1+self.marks2+self.marks3)/3) + "%"

s1 = Student(98,96,69)
print(s1.persentage)

#but now if we change any marks then error will be there in calculation
s1.marks2 = 86
# print(s1.persentage)#no change in the persentage

#1st method
# s1.persentageCalc()
# print(s1.persentage)

#this will call the function after the values are updated

#2nd method

#use @property decorator --> using this we can write a function that returns a value which will be assigned to function named attribute.this will change function name to attribute

print(s1.persentage)
"""

#polymorphism = operator overloading
#when the same operator is allowed to have different meaning according to context.

#example --> +
# print(1+2)
# print("1"+"2")
# print([1]+[2])

"""
class Complex():
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def printNum(self):
        print(self.real,"i +",self.img,"j")

    # def add(self,num2):
    #     self.real = self.real + num2.real
    #     self.img = self.img + num2.img
    #     return Complex(self.real,self.img)

    def __add__(self,num2):
        self.real = self.real + num2.real
        self.img = self.img + num2.img
        return Complex(self.real,self.img)
    
    def __sub__(self,num2):
        self.real = self.real - num2.real
        self.img = self.img - num2.img
        return Complex(self.real,self.img)

num1 = Complex(3,6)
num1.printNum()

num2 = Complex(5,8)
num2.printNum()

# num3 = num1.add(num2)
# num3.printNum()

#but we cann't write to use
# num3 = num1 + num2

#so use dunder function means (__function__)
# num3 = num1 + num2
num3 = num1 - num2
num3.printNum()
"""

"""
#praciceQ2
class Employee:
    def __init__(self,role,dep,salary):
        self.role = role
        self.dep = dep
        self.salary = salary

    def showDetails(self):
        print("role =",self.role)
        print("department =",self.dep)
        print("salary = ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT",54564)

    def showDetails(self):
        print("name =",self.name)
        print("age = ",self.age)
        return super().showDetails()

e1 = Employee("Intern","SE",5454)
e1.showDetails()
print()
Engineer1 = Engineer("Mohak",23)
Engineer1.showDetails()
"""

#practiceQ3 use of greater than function (<,>)

class Order:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def __gt__(self,order2):
        return self.price > order2.price
    
order1 = Order("tea",12)
order2 = Order("coffee",25)

print(order1 < order2)