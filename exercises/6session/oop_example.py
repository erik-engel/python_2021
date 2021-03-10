class Person:

    species = 'Mammal' # class variable

    def __init__(self, *args):
    #self.name = name	# instance variabler
    
        if len(args) == 1:
            self.name = args[0]

        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]

    def name_age(self):
        return self.name + str(self.age)


class Instructor: 
    def __init__(self, course):
        self.course = course


class Student(Person, Instructor):

    def __init__(self, *args):
        Person.__init__(self, args[0])
        Instructor.__init__(self, args[1])
