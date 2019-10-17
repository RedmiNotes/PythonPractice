my_list = ["India","America","canada","australia"]

print(my_list)   # -- print all list values

print(my_list[2]) # -- print index position value

#Change index position value
my_list[0] = "London"  # --change index value

print(my_list)

for i in my_list:    # -- traversing element one by one
    print(i)

print(len(my_list))   # -- length of the list

my_list.append("india")  # -- append use to insert the new element into the list

print(my_list)

my_list.insert(3,"new york")  # -- insert the value in the specific index position

print(my_list)

my_list.remove("india")   # -- remove the particular index value

print(my_list)

my_list.pop(3)     # -- hide the index value(default hide index value is last element)

print(my_list)

del my_list[0]   # -- delete the index value

print(my_list)

my_list.clear()  # -- clear the list all index values

print(my_list)

state = ["Andhra","karnadaka","india","telungana","kerala"]

print(state)

state.reverse()

print(state)

my_list_1 = ["Letters",1,3.94,True,'x']   #  -- store all type of elements

print(my_list_1)

my_list_2 = ["hi",[1,2,3],['a','b','c']]   # -- nested list

print(my_list_2)

print(my_list_2[1])  # -- print nested list index value

print(my_list_2[1][2])  # -- print inner list value specify index position