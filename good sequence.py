n=int(input())
count=0
array=list(map(int,input().split()))
if n<3:
    print("not possible")

for i in range(n-2):
    if (array[i]+array[i+1] == array[i+2]) or (array[i]-array[i+1] == array[i+2] and array[i+2]>=0) or (array[i+1]-array[i] == array[i+2] and array[i+2]>=0) :
        count=count+1
if n>=3:
    print(count)


