#!/usr/bin/python

class pencil():
    def __init__(self, sharp=10, Material='wood'):
        self.material = Material
        self.length = 10
        self.eraserQuality = 'slightly worn'
        self.brand = 'Ticonderoga'
        self.number = 2
        self.sharpness = sharp
    
    def sharpen(self, sharpened):
        if sharpened:
            print("You do not need to sharpen your pencil!")
        elif self.length == 0:
            print("Go get a new pencil!")
        else:
            self.length -= 1
            sharpened = True
            self.sharpness = 10

    def usePencil(self):
        if self.sharpness <= 1:
            self.sharpness = 0
        else:
            self.sharpness -= 2


if __name__ == '__main__':
    myPencil = pencil(7)
    print("myPencil")
    print(myPencil.sharpness)
    print(myPencil.length)
    myPencil.usePencil()
    print(myPencil.sharpness)
    print(myPencil.length)
    myPencil.sharpen(False)
    print(myPencil.sharpness)
    print(myPencil.length)
    herPencil = pencil(2)
    print("herPencil")
    print(herPencil.sharpness)
    herPencil.sharpen(False)
    print(herPencil.sharpness)
    herPencil.usePencil()
    print(herPencil.sharpness)
    #hisPencil = pencil('metal')
    #print("hisPencil")
#    print(hisPencil.sharpness)
 #   print(hisPencil.material)
    hisCorrectPencil = pencil(Material='metal')
    print('hisCorrectPencil')
    print(hisCorrectPencil.sharpness)
    print(hisCorrectPencil.material)
