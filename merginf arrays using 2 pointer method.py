n,m= map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
array3=[]
i=0
j=0

while (i < n or j < m):
    if j==m or i<n and array1[i]<=array2[j]:
        array3.append(array1[i])
        i=i+1
    else:
        array3.append(array2[j])
        j=j+1    
print(array3)


