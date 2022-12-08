t=int(input())
sum=0
maxsum=0

for i in range(t):
    N,X=list(map(int,input().split()))
    array=list(map(int,input().split()))
    for j in range(N-X+1):
        for i in range(j,j+X-1):
            sum=sum+array[i]
    if sum>maxsum:
        maxsum=sum
    sum=0
print(sum)    



