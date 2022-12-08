t=int(input())
for i in range(t):
    n,m=list(map(int,input().split()))
    string1=list(map(str,input().split()))
    string2=list(map(str,input().split()))
    string1.sort()
    string2.sort()
    if n==m and string1==string2:
        print("YES")
    else:
        print("NO")    



 


