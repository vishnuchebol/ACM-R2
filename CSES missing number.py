n=int(input("enter the number"))
sum=0

inputstring=input()
string = inputstring.split(" ")[:n]

for j in range(len(string)) :
    sum=sum+int(string[j])     
y=(n*(n+1))/2

print("missing number is ",y-sum) 

