t=int(input())
for j in range(t):
    count=0
    n=int(input())
    string=input()
    for i in range(1,int((n+1)/3)+1):
        if string[3*i-2]!=string[3*i-1]:
            print("NO")
            break
        else:
            count=count+1
    if count== int((n+1)/3)+1:
        print("YES")    