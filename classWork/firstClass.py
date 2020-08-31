#!/usr/bin/python

class person:

    def __init__(self, FN, LN, SSN):
        self.fName = FN
        self.lName = LN
        self.ssNum = SSN

    def concat(self):
        return str(self.fName) + " " + str(self.lName)


PersonA = person("Mary", "Bosch", 592780271)
PersonB = person("Jack", "Reissman", "793756394")


print(PersonA.concat())
print(PersonA.ssNum)

print("\n\n")

print(PersonB.concat())
print(PersonB.ssNum)

#print(PersonA.lName)
#print(PersonA.fName)
