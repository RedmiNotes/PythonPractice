
print("Enter the Number :")
n = int(input())
sum = 0
while 0<n:
    r = n%10
    sum+=int(r)
    n/=10
print(sum)
