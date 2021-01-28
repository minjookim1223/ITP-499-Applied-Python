# Minjoo Kim
# ITP 499, Spring 2020
# Assignment #1
# minjook@usc.edu

# This assignment is composed of Boxer and Swimmer classes,
# as well as the function that finds common elements in two lists


# Athlete Object
# Declare five instance variables
class Athlete(object):
    def __init__(self, firstName, lastName, birthYear, country, college):
        self.firstName = firstName
        self.lastName = lastName
        self.birthYear = birthYear
        self.country = country
        self.college = college

# Define getter and setter methods for each variable
    def setFirstName(self, firstName):
        self.firstName = firstName

    def getFirstName(self):
        return self.firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getLastName(self):
        return self.lastName

    def setBirthYear(self, birthYear):
        self.birthYear = birthYear

    def getBirthYear(self):
        return self.birthYear

    def setCountry(self, country):
        self.country = country

    def getCountry(self):
        return self.country

    def setCollege(self, college):
        self.college = college

    def getCollege(self):
        return self.college

# bio() method
# kind of works like a __str__ method
# basically prints information about each object (athlete)
    def bio(self):
        print(self.firstName, self.lastName, "was born in", self.country, "in",
              self.birthYear, "and attended", self.college)


# class Swimmer
# inherit all the traits from Athlete object
class Swimmer(Athlete):
    def __init__(self, firstName, lastName, birthYear, country, college):
        self.swimStrokes = {}       # dictionary to contain all the strokes and speed
        super().__init__(firstName, lastName, birthYear, country, college)  # super() to inherit all the var/methods

    def add_swim_stroke(self, swimStrokes, speed):      # This function is used to add a stroke into the collection of
        self.swimStrokes[swimStrokes] = speed           # all the swim strokes including the speed in the dict

    def display_swim_strokes(self):                     # Display the collection (dictionary)
        print(self.swimStrokes)


# class Boxer
# inherit all the traits from Athlete object
class Boxer(Athlete):
    def __init__(self, firstName, lastName, birthYear, country, college):
        self.numFights = 40         # set the number of fights as 40
        super().__init__(firstName, lastName, birthYear, country, college)  # super() to inherit all the var/methods

    def num_of_fights_remaining(self):      # Show the number of fights remaining by returning self.numFights
        return self.numFights

    def fight(self):                        # If a boxer fights, reduce the number of fights by 1
        if self.numFights > 0:              # Make sure the number of fights do not go below 0
            self.numFights -= 1


# This function is used to find a number of common elements between two lists
# If the lists are of different sizes, then return -1
def findCommonElements(listOne, listTwo):
    count = 0

    if len(listOne) != len(listTwo):
        return -1
    else:
        for i in range (len(listOne)):
            if listOne[i] in listTwo:
                count += 1

    return count
