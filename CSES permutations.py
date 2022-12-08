n=int(input("enter a number"))
x=int((n+1)/2)
if n<=3:
    print("not possible")
if n%2==0:
    for i in range(1,int(n/2)+1):
        print(2*i,end=" ")
    for j in range(1,int(n/2)+1):
        print(2*j-1,end=" ")   

else:
    for k in  range(1,x):
        print(2*k,end=" ")
    for p in range(1,x+1):
        print(2*p-1,end=" ")





