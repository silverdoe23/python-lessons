#!/usr/bin/python
zooHT = {"swan":2, "robin":7, "bluejay":10}


def func(ht1):
    myBirdList = ["chickadee", "goose", "robin", "duck", "hawk", "swan"]
    for i in myBirdList: #O(n)
        if i in ht1.keys():#O(z)
            print("yay! " + i + " is in the zoo!\n") #O(1)
            print([key + "," + str(ht1[key]) for key in ht1]) #O(z)    O(1) expected
        else: print("not interesting enough") #0(1)
#O(n) * O(z) * O(1) 
#final print statement --> O(z) worst case * O(1) expected = O(z) expected
#first print statement --> O(1) worst case
#print statements --> O(z) expected + O(1) worst case = O(z) expected

#if statement --> O(z) worst case
#if statement down --> O(z) worst case + O(z) expected = O(z) expected
#else statement --> O(1) worst case
# O(z) expected > O(1) worst case

#inside for loop --> O(z) expected
#O(n) worst case * O(z) expected = ||  O(zn) expected  ||

if __name__ == "__main__":
    func(zooHT)
