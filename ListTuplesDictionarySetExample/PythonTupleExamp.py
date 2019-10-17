my_tuple = ("apple","orange","grape","cherry")

print(my_tuple)

print(my_tuple[3])  # -- print specify index value

print(my_tuple[-2])  # -- print negative value index statrt from last inde

print(my_tuple[1:4])  # -- print range also 1,2,3

for x in my_tuple:
    print(x)

# my_tuple[2] = "pineapple"   --- does not allow duplicates..
# print(my_tuple)  ----->  TypeError: 'tuple' object does not support item assignment

# del my_tuple        # --> delete entire values..

print(len(my_tuple))  # --> length of my tuble

my_tuple_1 = ("hi","hello",(1,2,3),["welcome","to","python"])  # -- can use nested tuple and use list also.

print(my_tuple_1)

print(my_tuple_1[3][2])

# note : in tuple we can store list.
    # : we can update the list of tuble.

my_tuple_1[3][1] = "the"

print(my_tuple_1)

print("hi" in my_tuple_1)  # -- print True
print("to" in my_tuple_1)  # -- print False
print(2 in my_tuple_1[2])