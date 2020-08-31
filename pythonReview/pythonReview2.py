#!/usr/bin/python

Names = ['Amanda', 'Melanie', 'Deneen', 'Debbie', 'Chris', 'Jake', 'Josephine', 'Ryan', 'Dr. Deani', 'Lisa']
Names2 = []

def captions(n, length, n2):
    if length == 1:
        print(n[0] + " is presenting")
        n2.append(n[0])
        print("Thank you for listening! That's all for now.")
        return n2
    else:
        print(n[0] + " is presenting.")
        n2.append(n[0])
        return captions(n[1:], length-1, n2)


def fibbonacciNumber(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibbonacciNumber(n-1) + fibbonacciNumber(n-2)

if __name__ == '__main__':
    #finalNames = captions(Names, len(Names), Names2)
    #print(finalNames)
    num = input("What fib number?\n")
    print(fibbonacciNumber(num))
