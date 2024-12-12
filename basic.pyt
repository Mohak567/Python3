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