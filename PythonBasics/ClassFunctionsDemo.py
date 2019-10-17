class DemoClass_1:
    name = "Python Lang."

x = DemoClass_1()
print(x.name)
#-----------------------------------------------------------------------------------------------
class DemoClass_2:

    def sum(self,a,b):
        print(a+b)

DemoClass_2().sum(10,20)
#-----------------------------------------------------------------------------------------------
class DemoClass_3:

    def __init__(self,name,age):
        self.name = name
        self.age = age

x = DemoClass_3("Selenium",100)
print(x.name,x.age)
#-----------------------------------------------------------------------------------------------