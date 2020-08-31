class fixedSizeArray(object):
	def __init__(self, arraySize=5):
		self.arraySize = arraySize
		self.array = [None] * self.arraySize

	def append(self, index=None, value=None):
		print("Append Operation cannot be performed on fixed size array")
		return
	
	def get(self, index=None):

		try:
			return self.array[index]
		except:
			print('This is Fixed Size Array: Please Use the available Indices')
			return

	def set(self, index=None, value=None):
		if not index and index - 1 not in xrange(self.arraySize):
			print('invalid Index or Array Size Exceeded')
			return
		try:
			self.array[index] = value
		except:
			print('This is Fixed Size Array: Please Use the available Indices')

#to create a fixed size array
myArray = fixedSizeArray(5)  #this creates a fixedSizeArray of size 5
myArray.set(4, 5) #this the alternative for myArray[4] = 5 - it sets the index 4 of myArray to be equal to 5

yourArray = fixedSizeArray(7) #this creates a fixedSizeArray of size 7
yourArray.set(6,1) #this sets the 6th index of yourArray to be equal to 1

#to iterate through a fixedSizeArray
for i in range(0, myArray.arraySize, 1):
	print(myArray.get(i))  #myArray.get(i) gets the element in the ith index of myArray
