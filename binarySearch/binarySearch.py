#!/usr/bin/python
import math



def makeList(mini, maxi):
    theList = []
    for i in range(mini, maxi+1, 1):
        theList.append(i)
    return theList



def binarySearch(numList):
    minm = numList[0]
    maxm = numList[-1]
    correctAnswerGuessed = False
    guessNumber = 0
    while not correctAnswerGuessed:
        midpoint = math.ceil((minm+maxm)/2)
        guessNumber += 1
        print("Guess number "+str(guessNumber)+": "+str(midpoint)+"\n")
        answ = str(input("Is your number higher, lower, or am I correct? Type higher, lower, or correct, in all lowercase.\n"))
        if answ == "correct":
            print('Yay, I got it right! It took me '+str(guessNumber)+' guesses!\n')
            correctAnswerGuessed = True
        elif answ == "higher":
            minm = midpoint
        elif answ == "lower":
            maxm = midpoint



if __name__ == '__main__':
    minimum = input("What is the minimum number?\n")
    maximum = input("What is the maximum number?\n")
    l = makeList(minimum, maximum)
    print("Pick a number between those two.\n")
    binarySearch(l)

