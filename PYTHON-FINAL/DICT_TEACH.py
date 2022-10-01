# We use dictionary in python to show key value pairs and examples like name = Ehtesham , age = 28

# Python dictionary is ordered, changeable but donot allow duplicate values

# Lets create  a dictionary of Ehtesham



Ehtesham = {
       'sis' : {
           "age" : 28,
          "country" : "Pakistan",
          "hobbies": "Travelling and Gossips with friends",
          "cars": ["Toyota" , "Land Cruiser" , " MG ", " Kia Sportage "],
          "Wife": "Shumaila Ehtesham",
         },
     'brot': {
        "name1" : "Hassan Ali Khan",
        "relation1" : "Brother",
        "Age1" : 22,
        "Status1" : "Married",
        "name" : "Seemab Shaheen",
        "relation": "Sister",
        "Age" : 26,
        "Status" : "Married"}}
# a = Ehtesham[1]['cars']
# print(a)
# for cars in a:
#     print(cars)
# print(Ehtesham['brot']['name'])
# Ehtesham['brot']['name'] = "Shumaila Khan"
# print("After Changing ",Ehtesham['brot']['name'])

a = input("Which car do you want to check in Ehtesham Garage")
b = a.title()
c = Ehtesham['sis']['cars']
# if carss in c == a :
#     print(carss)
print("Your input",b)
if b == c:
    print("He has this car")
else:
    print("this car not found in the garage of EAK")