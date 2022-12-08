t=int(input())

for i in range(t):
    count=0
    n=int(input())
    inputstring=input()
    string = inputstring.split(" ")[:n]
    for j in range(n-1):
        if string[j]==string[j+1]: #if x divides y and y divides x, then x=y
            count=count+1
    if count==n-1:
            print("YES")
    else:
            print("NO")
