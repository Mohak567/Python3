#class is a blueprint for creating objects.It is a collection of attributes and methods
#attribute types --> (i). class attribute
#                    (ii). object/instance object

"""class Cars:
    company = "local"
    model = 2024
    color = "red"

objOfCars = Cars()

print(objOfCars.color)"""

#constructor --> it is also called as init function.It is invoked automatically whenever a new object is created

"""
class Class_Name :
    default constructor

        def __init__():
            work to do

    parametrized constructor

    def __init__(p1,p2):
        work

"""
"""
class Student:

    @staticmethod
    def print_hello():
        print("helllllllllo")

    #class attribute
    school_Name = "Sainik School"
    name = "none"#class attribute < object attribute (presidence)

    #self(variable name) is the first parameter which refers to the current instance of the class,and is used to access variables
    #that belong to the class
    def __init__(self,name,age): #--> self is a parameter which is pointed by the object created
        self.name = name#--> instance/object attribute
        self.age = age#--------^
        print("Student added in db")# --> it will run automatically whenever a new object is created

    def get_age(self): #-->user defined methods
        print(self.age)

    #for creating a static method we use @staticmethod.Decorator allow us to wrap a function without permanetly changing it
    #it is made on class level and specify it in the statring
    #Because they are specified at class level,they don't require self parameter
    #sytax

# class Class_Name:
#     @staticmethod
#     def function_name():
#         work

        


s1 = Student("mohak",23)
print(s1.name)
print(s1.age)
print(s1.school_Name)
#above is a instance/object access

print(Student.school_Name)#class attribute access

s1.get_age()#function calling

s1.name = "Mohak" #can manipulate the values directly

s1.print_hello()
"""

#praciceQ1
"""class Stu:
    def __init__(self,name,l):
        self.name = name
        self.l = l

    def print_Details(self):
        print(self.name)
        for el in self.l:
            print(el,end=" ")
        print()

    def average(self):
        avg = 0
        idx = 0
        for el in self.l:
            avg += el
            idx += 1

        print("Average =",int((avg/idx)))

obj = Stu("mohak",[65,67,68])
obj.print_Details()
obj.average()"""

#Abstraction --> Hidding implementaion details of the class and showing only essential features to the user
#Encapsulation --> Wrapping methods and data into a single unit(Object)

"""class Car:
    def __init__(self):
        self.engine = False
        self.acc = False
        self.lights = False
    def start(self):
        self.engine = True
        self.acc = True
        self.lights = True
        print("Car is ready to go")

obj = Car()
obj.start()"""


#practiceQ2
class Bank:
    def __init__(self,balance,acc_num):
        self.balance = balance
        self.acc_num = acc_num
    
    def credit(self,cNum):
        self.balance += cNum
        print(cNum," credited to the account",self.acc_num)
        print("current balance = ",self.balance)

    def debit(self,dNum):
        self.balance -= dNum
        print(dNum," debited from the account",self.acc_num)
        print("current balance = ",self.balance)

    def balance_check(self):
        print("rs =",self.balance,"in",self.acc_num)

obj = Bank(1000,12345)
obj.credit(100)
obj.debit(500)
obj.balance_check()