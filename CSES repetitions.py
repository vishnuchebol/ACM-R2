 #Program to calculate the length of the maximu string length

name = input("Enter the string:")
print (name)
strLength = len(name)
print ("Length of the String:",strLength)

# Initializations
localCounter = 1 
maxCounter = 0
k = 0

while k<strLength -1 :
    if name[k] == name[k+1]:
        localCounter = localCounter + 1 
        if k == strLength-2:
            if localCounter>maxCounter:
                maxCounter=localCounter

    else:
        if (maxCounter < localCounter):
            maxCounter = localCounter
        localCounter = 1 
    k = k + 1 

print ("Max Counter is", maxCounter)
         
