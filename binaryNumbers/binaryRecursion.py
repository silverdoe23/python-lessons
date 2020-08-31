#!/usr/bin/python

numDict = {}

def mmMain():
    inp = getFibon()
    print(calcFibon(inp-1))

def getFibon():
    isTrue = False
    while isTrue == False:
        inpp = input('Which fibonacci number would you like to find?\n')
        if type(inpp) == int:
            isTrue = True
    return inpp
        
def calcFibon(n):
    if n == 0 or n == 1:
        return 1
    elif n in numDict:
        return numDict[n]
    else:
        x = calcFibon(n-1) + calcFibon(n-2)
        numDict[n] = x
        return x

if __name__ == '__main__':
    mmMain()
