t=int(input())
even=[]
odd=[]
for i in range(t):
    n=int(input())
    array = list(map(int, input().split()))
    for i in range(len(array)):
        if array[i]%2==0:
            even.append(array[i])
            
        else:
            odd.append(array[i])

    if (len(even) - len(odd) >1) or (len(odd)  - len(even)  >1):
        print("-1")
    elif len(even)  >= len(odd)  :
        p=0
        d=0
        for k in range(len(even)+len(odd)):
            if k==1:
                print(even[p],end=" ")
                p=p+1
            elif k== len(even)  + len(odd) -1:
                print(even[p])
            elif k%4==0 or k%4==1:
                print(even[p],end=" ")
                p=p+1
            else:
                print(odd[d],end=" ")
                d=d+1 
    else:
        p=0
        d=0
        for k in range(len(even)+len(odd)):
            if k==1:
                print(odd[p],end=" ")
                p=p+1
            elif k== len(even) +len(odd) - 1:
                print(odd[d])
                
            elif k%4==0 or k%4==1:
                print(odd[p],end=" ")
                p=p+1
            else:
                print(even[d],end=" ")
                d=d+1             

