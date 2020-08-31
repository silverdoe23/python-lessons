#!/usr/bin/python

def addStrNum(string, number):
    try:
        return string + number
    except:
        print("...it didn't work.\n")
        print("However, this is what happens if we change the number to a string of itsself. Example: 43 --> '43'.")
        print(string + str(number))
        return



if __name__ == '__main__':
    print("We are going to try and add a word and a number.")
    s = str(input("Enter your  word, with quotation marks (example: 'helloworld')\n"))
    n = input("Enter the number, without quotations.\n")
    print("Aaaand...")
    addStrNum(s, n)
    
