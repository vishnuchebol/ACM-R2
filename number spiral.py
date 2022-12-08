
t=int(input("enter number of tests"))

for i in range(t):
    print("enter column number and row number")
    x,y = map(int, input().split())
    if y>x:
        print(y*y-x+1)
    if x>y:
        print(x*x-y+1)
    if x==y:
        print(x*x-x+1)    