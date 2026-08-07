

class BaseParameterCalculation:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def calculate_formula(self, *args, **kwargs):
        pass

    def __str__(self):
        return f'{self.name}: {self.value}\n{self.calculate_formula()}'


class NetRevenue(BaseParameterCalculation):

    def __init__(self, name, value, second_value):
        super().__init__(name, value)
        self.second_value = second_value

    def calculate_formula(self):
        print('formula is  x*b /(x+b)')
        print(f'base value is {self.value}')
        print(f'second value is {self.second_value}')
        print(f'result is {self.value*self.second_value}')

        return self.value*self.second_value


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f'Student name is {self.name} and his age is {self.age}'

    def __repr__(self):
        return f'Student("{self.name}", {self.age})'


net_rev = NetRevenue('net revenue', 55, 10)
user_1 = Student('Alex', 25)
user_1.age = 26

print(f'repr of student is:  {repr(user_1)}')

print(user_1)
# print(str(user_1))
# print(user_1.__str__())

user_1.age = 26

print(user_1)