n=int(input())
countof2=0
countof5=0
array = list(map(int, input().split()))
for i in range(len(array)):
    if array[i]%2==0:
        while array[i]%2==0:
            array[i]=array[i]/2
            countof2=countof2+1
    if array[i]%5==0:
        while array[i]%5==0:
            array[i]=array[i]/5
            countof5=countof5+1 
if countof5>int(countof2/2):
    print(int(countof2/2))
else:
    print(countof5)         

