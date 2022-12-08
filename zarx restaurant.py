n,x,y = map(int, input().split())

priceA=0
priceB=0
totalsum=0
i=0

string=input()
length=len(string)
while i<length:
    if string[i]=="B":
        if string[i+1]=="B":
            priceB= priceB + 2*y
            totalsum=totalsum + 2*y
            i=i+2
        elif string[i+1]=="A":
            priceB=priceB + x+y
            totalsum=totalsum+x+y
            i=i+2
        
    elif string[i]=="A":
        totalsum=totalsum+x
        i=i+1


priceA=totalsum-priceB
print(priceA,priceB)        