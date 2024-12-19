
"""
print("hello")
print("first","second")
a = "hello"
b = 'hey'
print(a+" "+b)
print(type(a))
print(type(15.5))
print(type(155))

print(int(15.5))
print(float(15))

c = 'Simon\'s skateboard is in the garage.'
print(c)
# d = 'Simon's skateboard is in the garage.' # error = while we use apostrophe(') without backslash(\) in single quotes
#solution use a backslash or type the string in double quotes
# print(d)

#to find length of a string
d = len(c)
print(d)

#or

print(len(c))

print(a *5)

num = 55
print(type(num))
print(type(str(num)))

test = "ksdnlk lkdnf"

print('ksdnlk lkdnf' .title()) # captal all starrting letters
print(test.title())
print(test.islower())
print("one fish,two fish,blue fish, 3 fish.".count('fish'))
print("my name is {}".format('mohak'))
name = "Mohak"
print("my name is {}".format(name))
print(f"my name is {name}")
print("one fish,two fish,blue fish, 3 fish.".index('two'))
print("one fish,two fish,blue fish, 3 fish.".rfind("fish"))

#list = can store multiple types if data types 
list = ["hkjskn",564,654.54]
print(list[0])
print(list[1])
print(list[2])
print(list[-1])
print(list[-2])

#slicing in list
months =  ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months[6:9]) #lowerbond included and upperbond excluded
print(months[6:])#second half
print(months[:6])#first half
#also works for string
print(name[2:4])
print('July' in months,'July' not in months)
print('Mo' in name,'Mo' not in name)

#nature
z = 'mohak'
y = z
z = 'khare'
print(y)
print(z)
#where as
marks = ['a','b','c','d']
scores = marks
marks[1] = 'e'
print(marks)
print(scores)
#it also updates asigned values

#some methods
print(len(months))
#if list contains string then return according to a-z
print(max(months))
print(min(months))
print(sorted(months))
print(sorted(months,reverse = True))

#this gives error
# random_list = ['oknc',54,4566.8,"inv"]
# print(max(random_list))

print("\n".join("one fish,two fish,blue fish, 3 fish."))
print("\n".join(months))

months.append("knsdck")
print(months)
print(months.pop())#it will pop the last element

#tuples
#diemensions = (10 , 10 , 10) or
diemensions = 10 , 10 , 10
l , b , h = diemensions
print(f"the cubes has h = {l}, b = {b}, and h = {h}")

#sets are unordered
num = [1,2,3,4,5,6,2,3,1,5,4]
num_set = set(num)
num_set.add(45)
print(num_set)
num_set.pop()
print(num_set)

#iterating through dictionary
dict1 = {
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards": "Cosmo Kramer"
}
#it will only print keys present in the dictionary
for keys in dict1:
    print(keys)

#to print both keys and values we use built in function items

for keys,values in dict1.items():
    # print(f"actor :{keys} and their role :{values}")
    #or use
    print("actor:{} and their role :{}".format(keys,values))

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for object, count in basket_items.items():
    if object in fruits:
       fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))

"""
"""
#while loop
 
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
#sum method return the sum of element present in the list
# print(sum(card_deck))

new_deck = []
while sum(new_deck) <= 17:
    new_deck.append(card_deck.pop())

print(new_deck)

#zip --> The zip() function in Python is used to combine two or more iterables (such as lists, tuples, or strings) into a single iterator of tuples
#Each tuple contains elements from the corresponding position of the input iterables. The zip() function is particularly useful when you need to iterate over multiple
#iterables in parallel.

letters = ['a', 'b', 'c']
nums = [1, 2, 3]
#combining/packing into a single tuple
combination = list(zip(letters,nums))

for l,n in combination:
    print(f"letter:{l} and num:{n}")

#unpacking
l,n = zip(*combination)

print(l)
print(n)

#enumerate --> The enumerate() function in Python is a built-in function that adds a counter (index) to an iterable (such as a list, tuple, or string) and
# returns it as an enumerate object, which is an iterator that generates pairs of the index and the value from the iterable.

for i,letter in enumerate(l):
    print(f"index:{i} letter:{letter}")

#list comprehension
# store_variable = [variable_name.(specify action*) for variable_name in iterable data type(list,tuple etc) condition*]
# specify action* --> any action to perform on elements present in the list.This is optional
# condition* --> any condition to be checked before inserting elements in the new list.This is optional

cities = ["lucknow","barabanki","kanpur","bihar"]

new_cities = [city.title() for city in cities]

print(new_cities)

#normal
squares = [x**2 for x in range(10)]
print(squares)

#with 1 condition
squares1 = [x**2 for x in range(10) if x%2==0]
print(squares1)

#special case - more than 1 condition(list is taken as an example above also)
#syntax --> new_list = [variable_name.(specify action*) condition1 condition2 for variable_name in list]
squares2 = [x**2 if x%2 == 0 else x+3 for x in range(10)]
print(squares2)


scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

for name,score in scores.items():
    print(name,score)

#for converting it into new list where minimum score is 65
passed = [name for name,score in scores.items() if score >= 65]
print(passed)"""


"""
#Functions

def function_name(arg1,arg2):
    print("or use return")

#calling
function_name(1,2)

# egg_count = 0

# def buy_eggs():
#     egg_count += 12 # purchase a dozen eggs

# buy_eggs()
# unboundLocalError

str1 = 'Functions are important programming concepts.'

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()#local variable
print(str1)#global variable

# use for comments (#)
# use for documentation string or docString(""" """)

#Lamda function --> it is a special function which has no name (or anonymous function)

# variable_name = lambda expression1,expression2 : work to do

Any_value = lambda x , y : x ** y #it returns a value stored in the variable

print(Any_value(2,3))

#map function --> used to apply condition to each elements
#example 1
numbers = [1,2,3,4,5]
def squares(x):
    return x*x

# variable = map(function,iterable)

result = map(squares,numbers)
print(list(result))

#example 2
number_matrix = [
            [34, 63, 88, 71, 29],
            [90, 78, 51, 27, 45],
            [63, 37, 85, 46, 22],
            [51, 22, 34, 11, 18]
]

mean = lambda num_list : sum(num_list) / len(num_list)

average = map(mean,number_matrix)

print(list(average))

# filter function --> used to filter each element which returns true for the function specified
# example 1
numbers = [1,2,3,4,5]

is_even = lambda x : x%2 == 0

ans = filter(is_even,numbers)

print(list(ans))

# example 2

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)

# Aspect	map()	filter()
# Purpose	Transforms each element in an iterable	Filters elements based on a condition
# Function Argument	Takes a function that operates on one or more elements	Takes a function that returns a boolean (True/False)
# Result	A new iterable with transformed elements	A new iterable with elements that satisfy the condition
# Return Type	Map object (iterator)	Filter object (iterator)
# When to Use	When you want to apply a transformation to each element	When you want to keep only elements that satisfy a condition

"""