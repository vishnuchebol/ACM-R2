t=int(input())
for i in range(t):
    N=int(input())
    x=N*(N+1)*(2*N+1)/6
    y=N*N*(N+1)*(N+1)/4
    print(int(y-x))   #y>=x for n>=1 so not checking the other condition