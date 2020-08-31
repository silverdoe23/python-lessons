#!/usr/bin/python
import random


subjectsTopicsHT = {'Math': ['PEMDAS', 'Algebra', 'Geometry', 'Calculus'], 'Science': ['Biology', 'Chemistry', 'Physics'], 'Art': ['Shapes', 'Color', 'Drawing', 'Painting', 'Printing', 'Charcoal']}






class teacher():
    def __init__(self, subject, name):
        self.subject = subject
        self.name = name
        self.classSize = 3
        self.bestStudent = 'Bob'
        self.worstStudent = 'Joe'
        self.roster = []
        self.syllabus = subjectsTopicsHT[subject]
        self.topic = 0



    def addStudent(self, studentName):
        self.roster.append(studentName)


    def teachStudents(self):
        print(self.name + ': Alright, today in '+self.subject+' class, we are going to learn about '+self.syllabus[self.topic]+'.\n')
        print('*'+self.name+': proceeds to teach '+self.syllabus[self.topic]+'*')
        for i in self.roster:
            i.learnTopic2(self.syllabus[self.topic])
        self.topic += 1
        #update the subjects that the students know by calling the actual method in the student class.


class student():
    def __init__(self, name, quote, teacher):
        self.name = name
        self.teacher = teacher
        self.teacher.addStudent(self)
        self.topicsLearned = []
        self.catchphrase = quote
        if self.name == self.teacher.bestStudent:
            self.grade = 'Outstanding'
        elif self.name == self.teacher.worstStudent:
            self.grade = 'Troll'
        else:
            self.grade = random.choice(['Exceeds Expectations', 'Acceptable', 'Poor', 'Dreadful'])

    def learnTopic1(self, topic):
        if self.name == self.teacher.bestStudent:
            self.topicsLearned.append(topic)
            print(self.name + ': '+ self.catchphrase)
        elif self.name == self.teacher.worstStudent:
            if random.choice([1, 2, 3, 4, 5]) == 5:
                self.topicsLearned.append(topic)
            else:  print(self.name+': '+self.catchphrase)
        else:
            numList = [1, 2, 3, 4, 5]
            chance = random.choice(numList)
            realChance = []
            realChance = numList[:chance]
            if random.choice(numList) in realChance:
                self.topicsLearned.append(topic)
                print(self.name+': '+self.catchphrase)
   

    def learnTopic2(self, topic):
        bestStudentList = [True, True, True, True, True]
        tflist = [True, False]
        averageStudentList = [random.choice(tflist), random.choice(tflist), random.choice(tflist), random.choice(tflist), random.choice(tflist)]
        worstStudentList = [False, False, False, False, True]
        if self.name == self.teacher.bestStudent:
            if bestStudentList[random.choice([0, 1, 2, 3, 4])]:
                    self.topicsLearned.append(topic)
                    print(self.name+': '+self.catchphrase)
        elif self.name == self.teacher.worstStudent:
            if worstStudentList[random.choice([0, 1, 2, 3, 4])]:
                self.topicsLearned.append(topic)
            else: print(self.name+': '+self.catchphrase)
        else:
            if averageStudentList[random.choice([0, 1, 2, 3, 4])]:
                self.topicsLearned.append(topic)
                print(self.name+': '+self.catchphrase)






if __name__ == '__main__':
    DrT = teacher('Science', 'DrT')
    print(DrT.name)
    print(DrT.subject)
    print(DrT.roster)
    print('----')
    Bob = student('Bob', '"This is fascinating!"', DrT)
    print(Bob.name)
    print(Bob.catchphrase)
    print(Bob.teacher.name)
    print(Bob.grade)
    print(Bob.topicsLearned)
    print('----')
    Kim = student('Kim', '"Oh, I get it now!"', DrT)
    print(Kim.name)
    print(Kim.catchphrase)
    print(Kim.teacher.name)
    print(Kim.grade)
    print(Kim.topicsLearned)
    print('----')
    Joe = student('Joe', '"BORING!"', DrT)
    print(Joe.name)
    print(Joe.catchphrase)
    print(Joe.teacher.name)
    print(Joe.grade)
    print(Joe.topicsLearned)
    print('---------------------')
    DrT.teachStudents()
    print(Bob.topicsLearned)
    print(Kim.topicsLearned)
    print(Joe.topicsLearned)
    DrT.teachStudents()
    print(Bob.topicsLearned)
    print(Kim.topicsLearned)
    print(Joe.topicsLearned)
    DrT.teachStudents()
    print(Bob.topicsLearned)
    print(Kim.topicsLearned)
    print(Joe.topicsLearned)


        #use the bestStudentName and worstStudentName and random generators. BSN learns immediatly, WSN has 1/5 chance of learning it, and average student has (random: 1-5)/5 chance of learning. add to topicsLearned list if learned.



#make a main where you create a teacher and some students. add two more methods to each class, one set that is relevant to both and  where they interact with each other, and one set where it is only relevant to the teacher or the student but NOT BOTH.
