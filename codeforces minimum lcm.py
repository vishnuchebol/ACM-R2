t=int(input())

a=1
b=1
for i in range(t):
    n=int(input())
    j=1
    k=n-1
    while j<=k:
        if k%j==0:
            
            a=j
            b=k
            k=k-1
            j=j+1
            
        else:
            k=k-1
            j=j+1    
    print(a,b)        