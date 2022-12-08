n=int(input("enter the length of array"))
count=0
array=[]
for i in range(n):
    x=int(input())
    array.append(x)
for i in range(n-1):
    if array[i]>array[i+1]:
        count=count+(array[i]-array[i+1])

print(count)

