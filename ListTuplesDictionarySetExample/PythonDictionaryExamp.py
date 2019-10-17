my_dict = {
           "name" : "Kuruvila",
           "designation" : "Software Developer",
           "role" : "Developing",
           "industry" : "IT"
          }

print(my_dict)

print(my_dict["name"])  # -- give key value print the value of the key

print(my_dict.get("name"))  # -- using get method

print(my_dict.values())  # -- print dictionary all values.

for x in my_dict:
    print(x)   # -- print all key names.

print("--------------------------------------")

for x in my_dict:
    print(my_dict[x])  # -- print all values of dictionary

print("--------------------------------------")

for x,y in my_dict.items():  # -- items function use
    print(x ,":",y)

print("--------------------------------------")

my_dict["role"] = "Testing"

print(my_dict)

my_dict["Language"] = "Python"

print(my_dict)

my_dict.pop("role")

print(my_dict)

my_dict.popitem() # -- remove the last element

print(my_dict)

del my_dict["designation"]

print(my_dict)

my_dict.clear()

print(my_dict)

del my_dict