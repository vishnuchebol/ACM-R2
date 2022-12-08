N,X = map(int, input().split())
array = (list(map(int, input().split())))
array.sort()
i=0
k=N-1
while i<=k:
    
    if array[i]+array[k]==X:
        print("YES")
        break
    elif array[i] + array[k] > X:
        k=k-1
    else:
        i=i+1
    if i==k:
        print("NO")
        i=i+1    
         
