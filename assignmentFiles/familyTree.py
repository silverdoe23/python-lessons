#!/usr/bin/python

Family = {
        'Nama':['Valerie', 'Eric', 'Tim', 'Pablo', 'Pete', 'Michelle', 'Stephanie', 'Marc'], 
        'Papi':['Valerie', 'Eric', 'Tim', 'Pablo', 'Pete', 'Michelle', 'Stephanie', 'Marc'], 
        'Valerie':['Sofia', 'Carlo', 'Vivian'],
        'Eric': ['Amaya', 'Diego'],
        'Tim': ['Mai-Linh', 'Emile', 'Andres'],
        'Pablo':['Estela', 'Ada'],
        'Pete': ['Lola'],
        'Michelle': ['Vandylan'],
        'Stephanie': [],
        'Marc': [],
        'Amaya': [],
        'Sofia': [],
        'Diego': [],
        'Mai-Linh': [],
        'Estela': [],
        'Carlo': [],
        'Emile': [],
        'Ada': [],
        'Vivian': [],
        'Andres': [],
        'Lola': [],
        'Vandylan': []}

FamilyTree = []

def familyTreeSearch(name, people, tree):
    if tree[name] == []:
        people.append(name) # O(1) 
        return None
    else:
        theseKids = tree[name] #O(1) expected
        people.append(name) #O(1)
        for i in theseKids: # O(k) worst case    O(k) expected
            familyTreeSearch(i, people, tree) #number of times called is g where g is the number of generations --  O(g) worst case
    return FamilyTree


if __name__ == '__main__':
    print(familyTreeSearch('Valerie', FamilyTree, Family))


    # O(k**g) expected, where p is the number of children 'name' has, and q is the number of generations
