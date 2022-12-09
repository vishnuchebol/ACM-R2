x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x=(1/(x1-x3))
y=((y1-y2)/(x1-x2) - (y2-y3)/(x2-x3))
a=x*y
b=(y1-y2)/(x1-x2) - a*(x1+x2)
c = y1 - a*x1*x1 - b*x1
print(int(a+b+c))

