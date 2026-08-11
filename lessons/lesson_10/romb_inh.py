

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print('Unknown sound')

class Mammal(Animal):
    def __init__(self, name, num_legs):
        self.num_legs = num_legs
        Animal.__init__(self, name)

    @staticmethod
    def sound():
        print('Rrrrr')

class Bird(Animal):
    def __init__(self, name, wingspan):
        self.wingspan = wingspan
        Animal.__init__(self, name)

    @staticmethod
    def sound():
        print('url..')

class Bat(Mammal, Bird):  # Ромбовидне наслідування
    def __init__(self, name, num_legs, wingspan):
        Mammal.__init__(self, name, num_legs)
        Bird.__init__(self, name, wingspan)



print('Mammal', Mammal.__mro__)
print('Bird', Bird.__mro__)
print('Bat', Bat.__mro__)

# Mammal (Mammal, Animal, <class 'object)
# Bird (Bird, Animal, <class 'object)
# Bat (Bat, Mammal, Bird, Animal, <class 'object)

dog = Mammal(name='brovko', num_legs=4)
man = Bat(name='Bruce', num_legs=2, wingspan=2)

man.sound()
# parrot = Bird(name='Archi', wingspan=2)
# MRO method resolution order



#
# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
# class Dev(Employee):
#
#     def __init__(self, name, salary, lang):
#         super().__init__
#         self.lang = lang
#
# class PM(Employee):
#
#     def __init__(self, name, salary, department):
#         super().__init__
#         self.department = department
#
# class TeamLead(Dev, PM):
#
#     def __init__(self, name, salary, department, team_size):
#         super().__init__
#         self.team_size = team_size





#
#
# man.sound()
#
# dog.sound()
# parrot.sound()
