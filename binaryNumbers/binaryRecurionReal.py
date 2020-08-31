#!/usr/bin/python

def Maine():
    x = getBina()
    print(evaluateBina(x, 0, 1))


def getBina():
    k = False
    while k == False:
        k2 = False
        bina = input('Please input a binary number.\n\n')
        binaStr = str(bina)
        #print(binaStr)
        for x in binaStr:
            #print(x)
            #print(type(x))
            if x!="0" and x!="1":
                k2 = True
                break
        if k2 == False:
            k = True
    return binaStr

def evaluateBina(num, total, mod):
    if len(num) == 0:
        return total
    if num[-1] == "1":
        #print(total)
        total = total + mod
        #print(total)
    return evaluateBina(num[:-1], total, mod*2)

if __name__ == '__main__':
    Maine()

