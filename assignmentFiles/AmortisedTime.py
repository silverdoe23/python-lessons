#!/usr/bin/python

class fixedSizeArray(object):
    def __init__(self, arraySize=5):
	self.arraySize34 = arraySize
        self.array = [None] * arraySize

    def append(self, index=None, value=None):
        print("Append Operation cannot be performed on fixed size array")
	return
	
    def get(self, index=None):
	try:
    	    return self.array[index]
        except:
            #print('Get: This is Fixed Size Array of size '+str(len(self.array)) +', you inputed ' + str(index))
	    return

    def set(self, index=None, value=None):
	if index not in xrange(self.arraySize34):
            #print('invalid Index or Array Size Exceeded '+str(len(self.array)) + ', you inputed ' + str(index))
            raise Exception('You have exceeded the maximum')
	try:
	    self.array[index] = value
	except:
            #print('Set: This is Fixed Size Array of size ' + str(len(self.array))+', you inputed ' + str(index))
            return



#make a list of 337 elements

def makeList():
    theList = []
    for i in range(0, 338, 1):
        theList.append(i)
    return theList



def makeArray():
    myArray = fixedSizeArray(5)
    for x in range(0, 5, 1):
        myArray.set(x, x)
    return myArray


def populateArray(theArray, theList, i=0):
    if i >= len(theList):
        return theArray
    else:
        for x in range(i, len(theList), 1):
            try:
                theArray.set(x, theList[x])
            except:
                newArray = resizeArray(theArray)
                return populateArray(newArray, theList, x)
        return theArray

def resizeArray(theArray):
    newArray = fixedSizeArray(2*theArray.arraySize34)
    for i in range(0, theArray.arraySize34, 1):
        newArray.set(i, theArray.get(i))
    return newArray




def printArray(anArray):
    for x in range(0, anArray.arraySize34, 1):
        g = anArray.get(x)
        print(g)


if  __name__ == '__main__':
    l = makeList()
    a = makeArray()
    print(l)
    print(a)
    finalArray = populateArray(a, l)
    printArray(finalArray)
    
# in resize function, take in current size of ndarray and make new ndarray of twice that size. return new ndarray. function that copies the elements from the old ndarray into the new ndarray. then add the 337 elements. resize when run out of space. use try accept statement. try: code a accept: code b -- if code a throws an error, do code b. 
