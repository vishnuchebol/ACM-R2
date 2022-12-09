t=int(input())
for i in range(t):
    n=int(input())
    if n==1:
        print("Alice")
    elif n==2:
        print("Bob") 
    elif n==3:
        print("Alice")  
    elif n%2==0:
        print("Alice")    
    else:
        print("Bob")         