
a = 1
b = 1.2
c = 5j
d = "a"
e = "Python"
f = True

print(type(a))  # int
print(type(b))  # float
print(type(c))  # complex
print(type(d))  # String
print(type(e))  # String
print(type(f))  # boolean


#Casting
i = int(3)
j = int(5.8)
k = float(9)
l = str(100)

print(i)   # 3
print(j)   # 5
print(k)   # 9.0
print(l)   # "100"

x = "Python Program"
print(x[4])  # print index value of the string
print(x[2:8]) # start 2nd index and finish 7th index
print(len(x)) # length of the x.

x = "  Selenium Python   "
print(x.strip())    # strip is remove unwanted spaces

x = "Jeve"
print(x.replace("e","a"))   # replace the letters wherever the 'e' is present replace the value of 'a'

x = "Selenium,Python"
print(x.split(","))     # split operation

#inputs
print("Enter the Value :")
x = input()               # inputs functions
print("The Value is : " + x)