#!/usr/bin/python

class hotChocolate():
    def __init__(self, marshmallows=0):
        self.quantity = 7
        self.mms = marshmallows
        self.i = 0
        self.temps = ['boiling', 'scalding', 'hot', 'warm', 'lukewarm', 'cool', 'cold']
        self.temp = self.temps[self.i]
        self.milk = 1

    def addMarshmallow(self, numMarsh):
        self.mms += numMarsh
        print("Your hot cocoa now has "+str(self.mms)+" marshmallows!")
        return

    def addMilk(self, numMilk):
        self.milk = min(10, self.milk+numMilk)
        print('Your cocoa now is '+str(self.milk)+'/10 full of milk.')
        self.regQuantity('add')
        return

    def regQuantity(self, regType):
        if regType == 'add':
            if self.quantity < 10:
                self.quantity += 1
        if regType == 'drink':
            if self.quantity > 0:
                self.quantity -= 1
                self.lowerTemp()
        print("Your mug is "+str(self.quantity)+"0% full.")
        return


    def lowerTemp(self):
        if  self.i < len(self.temps)-1:
            self.i += 1
            self.temp = self.temps[self.i]
            print("Your hot chocolate is " + self.temp+".")
        else: print("Your hot chocolate is cold!  :(")
        return

    def drinkCocoa(self):
       self.regQuantity('drink')
       return

if __name__ == '__main__':
    myMug = hotChocolate(1)
    print(myMug.quantity)
    print(myMug.mms)
    print(myMug.temp)
    print(myMug.milk)
    myMug.addMarshmallow(4)
    myMug.addMilk(3)
    myMug.drinkCocoa()
