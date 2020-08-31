#!/usr/bin/python
letters_numbers = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
numbers_letters = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

def encrypt(string, shift):
    ''' 
    hello world
    8 5 12 12 15  23 15 18 12 4
    11 8 15 15 18  26 18 21 15 7
    khoor zruog
    '''
    encryptedString = ''
    string_numbers = []
    for i in string:
        string_numbers.append(letters_numbers[i])
    numbers_encrypted = []
    for j in string_numbers:
        newNumber = j+shift
        if newNumber > 26:
            newNumber = newNumber % 26
        numbers_encrypted.append(newNumber)
    for k in numbers_encrypted:
        encryptedString += numbers_letters[k]
    return encryptedString

def decrypt(string, shift):
    decryptedString = ''
    string_numbers = []
    for i in string:
        string_numbers.append(letters_numbers[i])
    numbers_decrypted = []
    for j in string_numbers:
        newNumber = j-shift
        if newNumber < 1:
            newNumber = newNumber + 26
        numbers_decrypted.append(newNumber)
    for k in numbers_decrypted:
        decryptedString += numbers_letters[k]
    return decryptedString




if __name__ == '__main__':
    myString = raw_input('What string would you like to encrypt?\n')
    myShift = input('What would you like your string to be shifted by? Please input a number.\n')
    x = encrypt(myString, myShift)
    print(x)
    print(decrypt(x, myShift))
