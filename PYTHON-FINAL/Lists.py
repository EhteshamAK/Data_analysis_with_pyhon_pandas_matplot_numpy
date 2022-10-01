# list, tuples, sets and dictionaries

# List items are ordered, mutable and allow duplicate values

# a = ["Ehtesham","Ali","Khan",28,5,1,True]
# # you can add value in list on your desired point
# # a.insert(0,"First")
# # a.append("added")
# # a.pop()
# # a.pop()
# # #slice a specific content
# # b = a[-6:]
# # print(a)
# # print(b)
#

# Using the list() constructor to make a list using double round brackets
# a = list(("Ehtesham", 28, 1, 0, 199))
# print("Original list",a)
# a.pop()
# print("Removed last element",a)
# a.append("1 element added by append")
# print("append",a)
# a.reverse()
# print("Reverse",a)
# for i in a:
#     if i == "Ehtesham" and i == 28:
#         continue
#     print("He is in the list")

# -----
# a = list(("Ehtesham", 28, 1, 0, 199))
# a.pop(0)
# print("First item removed",a)
# a.remove(1)
# print(a)
# for i in range(len(a)): # Print all numbers by referring there index numbers
#     print(a[i])

# ----------- loop using list comprehension ----------
# this_list = ["hello","world",1994,2090]
# [print(x) for x in this_list]

# fruits = ["apple","banana","mango","kiwi","pear"]
# pak_fruits = []
# for x in fruits:
#     if "m" in x:
#         pak_fruits.append(x)
# print(pak_fruits)

#  List comprehension offers a shorter
#  -when you want to create a new list based
#  --on the values of an existing list.

# With list comprehension you can do all that with only one line of code
# new_list = [x for x in fruits if "m" in x]
# print("List comprehension method",new_list)
# sort list alphabatically
# fruits.sort()
# print(fruits)
# sort desending
# fruits.sort(reverse=True)
# print("Reverse Sort",fruits)

# copy_a = fruits.copy()
# print(copy_a)

#  using extend method which puprose is to  add one list of element into another
# a = [1,2,3,4,5,9,8]
# b = [10,11,12,16,18,19]
# a.extend(b)
# a.sort()
# d = c.sort()
# print(a)

