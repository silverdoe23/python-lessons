#!/usr/bin/python
import random
genders = ['F', 'M']





class FamilyMember():
    def __init__(self, name, mom, dad, siblings, dateOfBirth, gender):
        self.name = name
        self.mom = mom
        self.dad = dad
        self.dob = dateOfBirth
        self.children = []
        self.siblings = siblings
        self.spouse = None
        self.gender = gender
    
    
    def newSibling(self, sibling):
        self.siblings.append(sibling)
        print(sibling.name + ' has been added as a sibling of '+ self.name +'.')
    
    
    def getMarried(self, newSpouse):
        self.spouse = newSpouse
        print('CONGRATULATIONS!!! Now '+ self.name +' is married to '+ newSpouse.name + '!')
    
    
    def haveAKid(self, childName, childDOB):
        if self.gender == 'F':
            childMom = self
            childDad = self.spouse
        elif self.gender == 'M':
            childDad = self
            childMom = self.spouse
        childSiblings = self.children
        childGender = random.choice(genders)
        child = FamilyMember(childName, childMom, childDad, childSiblings, childDOB, childGender)
        #add new child to children list
        self.children.append(child)
        self.spouse.children.append(child)
        for c in child.siblings:
            c.siblings.append(child)
        print('Wow, '+self.name+ ' and '+self.spouse+' had a kid!')

