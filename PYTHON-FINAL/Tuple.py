# Tuples are ordered, unchangeable and allow duplicate members
# You can create tuple with round brackets

# a = tuple(("Hello", "world")) # using tuple keyword
# print("using tupel command tuple has created",a)

# When you don't want to change the value inthe program later use tuple

# a = (1,2,3,4,True,'Hello World')
# print(a)
# a.append("new value added")
# a.pop()
# a.remove()
#  YOU CANNOT CHANGE THE VALUE OF TUPLE BUT YOU CAN DO IT ONLY AFTER CONVERTING IT TO LIST
# b = list(a)
# b.append("New value added using list method's")
# print(b)
# a = tuple(b)
# print(a)
# print(type(a))

# Accessing index

# b = a[0]
# c = a[-4:]
# print(b)
# print(c)

#check if item exist
# if "Hello World" in a:
#     print("You are awesome")

# unpacking tuple -
# a1 = ("apple","mango","banana","blueberry")
# a,b,*c = a1
# print(a)
# print(b)
# print(c)

# looping through index number
# for i in range(len(a1)):
#     print(a1[i])

# Multiplying tuple and joining tuple
# c = a + a1
# print(c)
#  multiplying tuple
# d = c * 3
# print("multiply",d)