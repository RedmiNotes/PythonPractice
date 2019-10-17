
def function_1():                                 # without arguments
    print("Python Functions Example")

function_1()
#-----------------------------------------------------------------------------------------------

def function_2(name):
    print("Welcome",name)

function_2("Python")
#-----------------------------------------------------------------------------------------------
def function_3(name="Selenium"):
    print("Welcome",name)

function_3("Python")
function_3()  # --> default value get in the arguments
#-----------------------------------------------------------------------------------------------

"""Return type using"""
def function_4(a,b):
    return (a+b)

print(function_4(100,200)) # or
x = function_4(10,20)
print(x)
#-----------------------------------------------------------------------------------------------