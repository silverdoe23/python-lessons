#!/usr/bin/python
import math

def mathmaticalGuess(minm, maxm, guesses):
    if minm == maxm:
        return "I'm smart enough to know when you're playing by the rules :)\n" #O(1) worst case
    midpoint = math.ceil((minm+maxm)/2) #O(1) worst case
    guesses += 1 #O(1) worst case
    print("Guess number " +str(guesses)+": "+str(midpoint)+"\n") #0(1) worst case
    answ = input("Is your number higher, lower, or am I right? Type 'higher', 'lower', or 'correct'.\n") #O(1) worst case
    if answ == 'higher': #O(1) worst case
        #Recursion run time = run time of each step * number of steps, both in big O form
        return mathmaticalGuess(midpoint, maxm, guesses) #O(1) worst case * O(log2(n)) worst case - where n is the range 
                                                                                               #  = O(log(n)) worst case
    elif answ == 'lower': #O(1) worst case
        return mathmaticalGuess(minm, midpoint, guesses) #O(log(n)) worst case
    elif answ == 'correct': #O(1) worst case
        return "Yay, I got it right! It took me "+ str(guesses)+ " guesses.\n" #O(1) worst case






def mathmaticalGuessv2(minm, maxm, guesses):
    print("If you're following the rules, your number will be one of these:\n") #O(1) worst case
    maxm = int(maxm) #O(1) worst case 
    minm = int(minm) #O(1) worst case 
    for i in range(minm, maxm+1, 1): #O(n) worst case
        print(i) #O(1) worst case
    if minm == maxm: #O(1) worst case 
        return "I'm smart enough to know when you're playing by the rules :)\n" #O(1) worst case
    midpoint = math.ceil((minm+maxm)/2) #O(1) worst case
    guesses += 1 #O(1) worst case
    print("Guess number " +str(guesses)+": "+str(midpoint)+"\n") #0(1) worst case
    answ = input("Is your number higher, lower, or am I right? Type 'higher', 'lower', or 'correct'.\n") #O(1) worst case
    if answ == 'higher': #O(1) worst case
        #Recursion run time = run time of each step * number of steps, both in big O form
        return mathmaticalGuessv2(midpoint, maxm, guesses) # O(n) worst case * O(log(n)) worst case = --O(n*log(n)) worst case---
    elif answ == 'lower': #O(1) worst case
        return mathmaticalGuessv2(minm, midpoint, guesses) #O(n*log(n)) worst case
    elif answ == 'correct': #O(1) worst case
        return "Yay, I got it right! It took me "+ str(guesses)+ " guesses.\n" #O(1) worst case








if __name__ == '__main__':
    minimum = input("Input your minimum.\n") #O(1) worst case
    maximum = input("Input your maximum.\n") #O(1) worst case
    print("Choose a number between those two.\n") #O(1) worst case
    a = mathmaticalGuessv2(minimum, maximum, 0) #O(n*log(n)) worst case 
    b = mathmaticalGuess(minimum, maximum, 0) #O(log(n))
    print(a) #O(1) worst case





    #1000
    #0100
    #0010
    #0001

    #0010
    # 0100
    #1000
