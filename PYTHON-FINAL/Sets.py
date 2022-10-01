# Sets are unordered, unchangeable and donot allow duplicate values

# Sets are written with curly brackets

a = {"Shumaila Ehtesham", 1, 2, 3,}
# print("Original",a)
# a.append("append method")
# a.append("appen2")
# print(a)

# Note - Once set is created you cann't change it's items,
# - but you can remove and add new items
# a.add("using add method")
# print(a)
# a.pop()
# a.add("Shumaila Ehtesham") # duplicat not allowed
# a.remove(2)
# print(a)
# print(len(a))
# print(type(a))
# for elem in a:
#     print(elem)

# using update method you can add element in this set
# set_1 = {1,2,3,4,5}
# set_2 = {6,7,8,9,10}
# set_1.update(set_2)
# print(set_1)

# using update u can add add set with list and tuple etc

# a[0] = "Butterfly"
# print(a)
# remove an item using remove and discrad method
# if the item you want to delete does not exist remove will show an error, discard does not show an error

# a.discard("Shumaila")
# print("discard method",a)
# a.remove("Shumaila")
# print("remove",a)
# a.pop()
# a.pop()
# print(a)

# Union method returns a new set with all items from
# both sets

# set1 = {1,2,3}
# set2 = {4,5,6}
# set3 = set1.union(set2)
# print(set3)

# insert method insert the item 2 in item 1
# set1 = {1,2,3}
# set2 = {4,5,6}
# set1.update(set2)
# print(set1)

# both these does not show any duplicate items

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection(y)
# print("Items present in both sets",z)
# x.intersection_update(y)
# print(x)