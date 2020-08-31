#!/usr/bin/python

def oddEven(n):#this function will return odd or even depending on weather the inputed number is odd or even
    #calls: none
    if int(n) % 2 == 0:
        return 'even'
    return 'odd'

def callOnList(l):#this function changes the elements in the list to be even or odd depending on what oddEven returns
    #calls: oddEven()
    result = []
    for a in l:
        if oddEven(a) == 'even':
            result.append('even')
        else: result.append('odd')
    return result

def controller():#this is the main function, calling functions that call functions
    #calls: callOnList()
    x = getInput()
    y = callOnList(x)
    return y

def getInput():#calls makeInt() areNumbers()
    validInput = False
    while validInput == False:
        a = raw_input("input a list of positive numbers\n").split(', ')
        b = makeInt(a)
        try:
            if areNumbers(b) == True:
                validInput = True
        except:
            validInput = False
    return b

def areNumbers(l):
    for k in l:
        #print(k)
        if k <= 0 or type(k) != int:
            return False
    return True

def makeInt(y):
    llama = []
    try:
        for w in y:
            llama.append(int(w))
    except:
        return [0, 0, 0]
    return llama


if __name__ == '__main__':
    print(controller())
