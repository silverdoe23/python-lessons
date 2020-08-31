#!/usr/bin/python
import sys



def readFile(myFilePath):
    with open(myFilePath) as f:
        f_read = f.read()
        fList = f_read.split(',')
        print(fList)
        print(type(fList))
        seperator = ', '
        fString = seperator.join(fList)
        print(fString)
        print(type(fString))
        #f_encoded = f_read.encode('base64')
        #print(f_encoded)
        #print(type(f_encoded))
        #f_decoded = f_encoded.decode('base64')
        #print(f_decoded)
        #print(type(f_decoded))






if __name__ == '__main__':
    print(sys.argv)
    filePath = sys.argv[1]
    #filePath = "/home/artsgirlsofia/dotTXT/input2.txt"
    readFile(filePath)
