#!/usr/bin/python
def isBinary(x): #this function will determine if the number inputed is a binary number
    for a in x:
        if a != 0 and a != 1:
             print('please input a valid binary number. Try again.')
             return False
    return True

def valueBinary(x):#this function will determine the value of the binary number
    thisValue = 1 #a, in this function, is what the value of the place is
    total = 0 #c is the value of the number
    for y in range(len(x)-1,-1, -1):
        if x[y] == 1:
            total = total + thisValue
        thisValue = thisValue * 2
    return total
    
def getInput():
    tf = False
    while tf == False:
        i = input("Please input a valid binary number.\n")
        tf = isBinary(i)
        if tf == True:
        return i

def calcMyBinary():
    inp = getInput()
    print(valueBinary(inp))

if __name__ == '__main__':
    calcMyBinary()
