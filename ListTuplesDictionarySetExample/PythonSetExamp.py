my_set = {"america","london","australia","canada","newyork"}

print(my_set)

for x in my_set:
    print(x)

print("canada" in my_set)  # check value is present

my_set.add("mumbai")    # -- add only one element into the set.

print(my_set)

my_set.update(["england","china","norway"])  # -- we can store multiple values

print(my_set)

print(len(my_set))  #  -- length of the set

my_set.remove("china")  # -- remove the set value.

print(my_set)

my_set.discard("norway")  # -- discard the set value

print(my_set)

my_set.pop()  # -- randomly remove the one element

my_set.clear()  # -- clear the set value

print(my_set)

del my_set  # -- delete the entire set

my_set_1 = {"hi","hello",(1,2,3),5.5}

print(my_set_1)

# -- convert list to set

list = [1,2,3,4,5]

print(list)

set = set(list)

print(set)

set_1 = {'a','b','c',1,2,3}

set_2 = {3,'c',"python",2.5}

print(set_1.union(set_2))   # -- union operation

print(set_1 | set_2)  # -- union expression

print(set_1.intersection(set_2))  # -- intersection operation

print(set_1 & set_2)  # -- intersection expression

print(set_1.difference(set_2))  # -- differentiate operation

print(set_1 - set_2)  # -- differentiate expression

print(set_1.symmetric_difference(set_2))  # -- symmetric operation

print(set_1 ^ set_2)  # -- symmetric expression