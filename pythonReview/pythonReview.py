#!/usr/bin/python3

def addition(x, y):
    return x+y


def subtract(x, y):
    return x-y


def divide(x, y):
    return x/y


def multiply(x, y):
    return x*y


def fireMDASTest():
    TestAdd(5, 3, 8, 'a1')
    TestAdd(5, -3, 2, 'a2')
    TestAdd(5, 0.5, 5.5, 'a3')
    TestAdd(0, 3, 3, 'a4')
    TestAdd(0, -2, -2, 'a5')
    TestSubtract(5, 3, 2, 's1')
    TestSubtract(5, -3, 8, 's2')
    TestSubtract(0, 3, -3, 's3')
    TestSubtract(5, 2.5, 2.5, 's4')
    TestSubtract(0, -3, 3, 's5')
    TestMultiply(5, 3, 15, 'm1')
    TestMultiply(5, -3, -15, 'm2')
    TestMultiply(-5, -3, 15, 'm3')
    TestMultiply(5, 0, 0, 'm4')
    TestMultiply(2, 0.5, 1, 'm5')
    TestMultiply(2, 1.5, 3, 'm6')
    TestDivide(6, 3, 2, 'd1')
    TestDivide(6, -3, -2, 'd2')
    TestDivide(-6, 3, -2, 'd3')
    TestDivide(0, 3, 0, 'd4')
    TestDivide(5, 5, 1, 'd5')
    TestDivide(4, 0.5, 8, 'd6')
    TestDivide(3, 0, 5, 'd7')

def Test(actual, expected, name):
    if actual == expected:
        print(name, 'Success')
    else: print(name, 'Fail')

def TestAdd(n1, n2, expected, name):
    if n1 == str or n2 == str or expected == str:
        print("Please do not input a string. Thank you!")
    else: Test(addition(n1, n2), expected, name)

def TestSubtract(n1, n2, expected, name):
    if n1 == str or n2 == str or expected == str:
        print("Please do not input a string. Thank you!")
    Test(subtract(n1, n2), expected, name)

def TestMultiply(n1, n2, expected, name):
    if n1 == str or n2 == str or expected == str:
        print("Please do not input a string. Thank you!")
    Test(multiply(n1, n2), expected, name)

def TestDivide(n1, n2, expected, name):
    if n1 == str or n2 == str or expected == str:
        print("Please do not input a string. Thank you!")
    if n2 == 0:
        print("This would theoretically throw an error. Let's see!")
        return None
    Test(divide(n1, n2), expected, name)








def iteration(L, mode):
    if mode == "For loop range":
        print("For loop range")
        for x in range(0, len(L)):
            print(L[x])
    elif mode == "For loop non-range":
        print("For loop non-range")
        for x in L:
            print(x)
    elif mode == "While loop":
        print("While loop")
        x = 0
        while x < len(L):
            print(L[x])
            x += 1
    else: print("Sorry, that is not a valid mode of iteration. Please try again.")

def fireIterationTest():
    List = ['Sally', 'Lucy', 'Mary']
    print(List)
    iteration(List, "For loop range")
    iteration(List, "For loop non-range")
    iteration(List, "While loop")
    iteration(List, "oops")



def studentIDLookup(HT, k):
    if k not in HT:
        return None
    return HT[k]

def fireIDLookupTest():
    ht1 = studentIDLookup(Dict, 1115)
    Test(ht1, "Jonathan", "StudentFound")
    ht2 = studentIDLookup(Dict, 1117)
    if not ht2: print("StudentNotFound Success")

Dict = {1111:"Amanda", 1112:"Sofia", 1113:"Vivian", 1114:"Valerie", 1115:"Jonathan", 1116:"Carlo"}
def newStudentID():
    k = input("What would you like the student ID code to be? Please use four numbers.\n")
    k = int(k)
    v = input("What would you like the student first name to be? Please capitalize the first letter.\n")
    if k not in Dict:
        Dict[k] = v
        print("Your ID has been added to the database!")
    else: print("This ID is already in use. Sorry!")



if __name__  == "__main__":
    #fireMDASTest()
    #fireIterationTest()
    #fireIDLookupTest()
    newStudentID()
