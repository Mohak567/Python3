#same line
print("mohak","khare")
#to change line
print("mohak")
print("khare")

a = 32
A = 23
print("a = ",a)
print("A = ",A)
print(type(a))

#string can be written in 3 types
s1 = 'type1'
s2 = "type2"
s3 = '''type3'''
print(s1,s2,s3)

#multiplication of string
a = 2
b = 3
txt = '@'
print(a*txt*b)

#concatination of string
a = "2"
b = 3
txt = "@"
print((a+txt)*b)

#division
print(1/2)

#integer division --> round off to smaller value
print(1//2)
#floor and integer divison are same

#multiply
print(2*3)
#power
print(2**3)

""""Muti line comment"""

#print(input("enter string - "))
#print(int(input("enter number - ")))
#print(float(input("enter float value - ")))

age = 26

if(age>=18):
    print("vote")
elif(age<=1):
    print("kyu")
else:
    print("dont")

#age = int(input("enter age :"))
print("vote" if age >= 18 else "kyu" if age <= 1 else "dont")

#age = int(input("enter age :"))
ans = ("no","yes")[age >= 18] #first value = false value , second value = true value
print(ans)

#type cast

#conversion = auto
a = 2
b = 3.5
print(a+b)
#casting = manual
a = 2
b = int("2")
print(a+b)

#String & ConditionalStatements

str = "kdjvnd.\n ldvnxlkdn. \t lkdgm."
print(str)
#length
print(len(str))
#accessing character
print(str[2])
#slicing --> first val = starting index, second val = end index -1 
print(str[1:3])
print(str[:3])
print(str[3:])

#for negative index
#  A  P  P  L  E
# -5 -4 -3 -2 -1

str = "APPLE"
print(str[:-1]) # --> APPL
print(str[-1]) # --> E
print(str[-4:]) # --> PPLE

str = "i am a coder"
print(str.endswith("er"))
print(str.capitalize())
print(str.replace('am','AM'))#oldValue,newValue
print(str.find('code'))
print(str.count('a'))

#list --> mutable
list = [11, 15.6, 'str', 'c', 65, 65, 94, 100, 10.8]
print(type(list))
print(list)

#slicing
print(list[1 : 3])
print(list[1 : ])
print(list[ : 2])
print(list[-3 : -1])
print(list[-1 : -3]) #empty

#basic methods
#at last
list.append(45)
print(list.count(65))#return occurences
# for sorting list should be one type either string or number
#print(list.sort())
#print(list.sort(reverse = True))
list.insert(2,"insert")
list.reverse()
list.remove(65)#removes first occurence
print(list.pop(5))
print(list.copy())
print(list.index(94))#returns index of the given elemnet
list.clear()#removes all elements
print(list)

#tuples --> immutable
#it should be written with a commoa , otherwises pyhton will return the type according to the assinged value
tupleTemp = (1)
print(type(tupleTemp))

tupleTemp1 = (1,)
print(type(tupleTemp1))

tuple = (11, 15.6, 'str', 'c', 65, 65, 94, 100, 10.8)
print(tuple)
print(tuple[1 : 5])
print(tuple.index(15.6))
print(tuple.count(65))

#dictionary --> stores in key value pair,mutable,unsorted,don't allow duplicate 
#dictionary  == HashMap
# but dictionary  != HashMap because dictionary can store different types of data types

dictionary1 = {
    "name" : "Mohak Khare",
    "age" : 23,
    "hobbies" : ["gaming","coding","music",13+13+10+3+15+15],
    "tupple" : ("gaming","coding","music",13+13+10+3+15+15),
    15 : 15,
    26.5 : 26.5,
    "18+" : True,
}
print(dictionary1)
print(dictionary1["name"])
#updation of any key value
dictionary1["name"] = "Mohaks"
#added a new key value pair
dictionary1["surname"] = "Khare"
print(dictionary1)

dict1 ={
    "key1" : "value",
    "dict2" : {
        "key1" : "value",
        "key2" : "value",
    },
}
print(dict1)
print(dict1["dict2"])

print(dictionary1.keys())
print(len(dictionary1))
#or
print(len(dictionary1.keys()))
print(dictionary1.values())#return all values
print(dictionary1.items())#return all keys with its values
#print(dictionary1["name1"])#this type of accessing values can give error but using get() method it gives none
print(dictionary1.get("name1"))
print(dictionary1.get("lsdng"))
print(dictionary1.get("surname"))
dictionary1.update({"name" : "Mohak(vibhu)"})
print(dictionary1["name"])#comment of line 184

#sets --> unordered,immutable,unique
#it can store all types of immutable data types like --> String,Integer,Float,Boolean,Tuple
#can't store list and dictionary because both are mutable
nums = {1, 2, 3, 4, 5, 3}
random = {"dfnd", 45, 89.6, (45, 56, 87, 78),True}
nulll_set = {}
null_set = set()#correct way
print(type(nulll_set))
print(type(null_set))

#sets are mutable but the elements present in the sets are immutable
nums.add(6)
print(nums.remove(3))#does not retrun any value
#nums.remove(7)#the element should present in the set otherwise error will occur
print(nums.pop())#pop random element from set
print(nums)
#nums.clear()#clear set
nums1 = {1, 2 , 5, 9, 4}
print(nums.union(nums1))
print(nums.intersection(nums1))
print(nums.difference(nums1))#return values from set1 which are not in set2
print(nums)

"""                                                             Loops                                                           """
#while loop
"""count = 0
while count < 5 :
    print("hello",count)
    count += 1 #can't use ++"""

l = [1,5,6,7,8,9,11,22,33,55,66]
i = 0

"""while i < len(l) :
    print(l[i])
    i += 1

find = 9
i = 0
while i<len(l):
    if(l[i] == find):
        print(i)
        break
    i+=1"""

#for loop

"""for variable in l:
    print(variable)

for variable in l:
    print(variable)
else:
    print("done")"""

"""for el in l:
    if(el == 9):
        print("found")
        break
else:
    print("not found")"""#this will run only when above all the conditions are not met

#range(start,stop,step) but only 1 argument which is stop can also be given where it start from 0 and ends at given number - 1
#by taking 1 step or incresing by 1

"""seq = range(5)
for el in seq:
    print(el)"""

"""seq = range(3,31,3)
for el in seq:
    print(el)"""

#pass --> used to skip any loop

"""for el in l:
    pass    #or we can use break also
print("lsfsd")"""

#factorial
"""fact = 5
anss = 1
for ans in range(1,6):
    anss *= ans
print(anss)"""

#functions

"""
def function_Name(parameter1,parameter2,...):
    task
"""

def sum(a,b):
    return a+b

def sum1(a,b):
    print(a+b)

print(sum(5,5))#for a return value
sum1(6,6)#no return value (void)

def empty_func():
    print("empty Function")

empty_func()#call

def no_parameter_function(a=1,b=2):#we can call this function without any parameters,it takes value which is specifed
    return a*b
print(no_parameter_function())

def no_parameter_function1(a,b=2):#here first parameter should be present
    return a*b
print(no_parameter_function1(5))

# def no_parameter_function2(a=5,b): --> this gives error because default values can only be taken from last
#     return a*b

#test
"""lissst = [1,2,"m",45]
def print_List(collectionn):
    for el in collectionn:
        print(el)

print_List(lissst)

def print_list_In_singleLine(coll):
    for el in coll:
        print(el,end=" ")
print_list_In_singleLine(lissst)"""

#recursion
"""def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)
print(factorial(5))

def sum_Of_FirstN(n,sum=0):
    if(n == 0):
        return sum
    sum += n
    return sum_Of_FirstN(n-1,sum)

print(sum_Of_FirstN(5))

def call_For_Print(coll,idx = 0):
    if idx == len(coll):
        return
    print(coll[idx])
    call_For_Print(coll,idx+1)


lisst = [1,2,3,4,5,8,7,9]
call_For_Print(lisst)"""


#File I/o
"""
vaiable_name = open.("file_path" or if file is in same folder then "file name" , "mode" default "r")
"""

"""file = open("demo.txt")"""
"""data = file.read()
print(data)
print(type(data))"""

"""
r = read mode(defaut)
w = write mode --> it deletes all data then open it Or truncating the file first
x = create a new file and open it for writting
a = to append or add data in the existing file at the end
b = to open binary file
t = text mode(default)
+ = for making combitaion or to open a disk file for updating(read and writing)
"""
#to get first n characters for the file
"""someChar = file.read(8)
print(someChar)"""

#for reading lines
"""firstLine = file.readline()
print(firstLine)

lines = file.readlines()#n numbers of lines or if empty will return all lines
print(lines)
print(type(lines))"""

#now if we again read any data from the file it will be empty because the data is red like a pointer pointing to a data.
"""line = file.readline()
print(line)"""
#In the above case the pointer is already at the end and no data can be read from the file so it returns empty line

#write
"""file = open("demo.txt","w")

data = file.write("performing write function")"""

#append
"""file = open("demo.txt","a")
data = file.write("\nperforming write function")"""

#if a file is not created then append and write function will create a file named given by the user

# file = open("sample.txt","w")
# file = open("sample.txt","a")

# file = open("sample.txt") <-- this will give error

#features with + and without +
"""
``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
"""

#with --> it is same as above function but by using with create a block which is capable of accessing files

# with open("file_Name") as variable_name
with open("demo.txt") as f:
    print(f.read())
#using with the file automatically closes

#to delete a file from system
"""import os
os.remove("demo.txt")"""

# with open("practice.txt","w") as file:
#     file.write("first java line\nsecond line\nthird line java")

#practice
# with open("practice.txt","r") as file:
#     data = file.read()

# new_Data = data.replace("java","python")
# print(new_Data)

# with open ("practice.txt","w") as file:
#     file.write(new_Data)

# with open("practice.txt","r") as file:
#     data = file.read()

# print(data.find("second"))