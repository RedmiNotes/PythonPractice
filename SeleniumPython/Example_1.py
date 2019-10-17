
n = int(input("enter the number of rows u want"))
i,j = 1,1
for i in range (1,n):
    for j in range(1,i):
        print("*",end="")
    print("\n")