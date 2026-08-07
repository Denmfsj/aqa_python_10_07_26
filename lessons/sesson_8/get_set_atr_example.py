

class User:

    def __init__(self, name, age, description):


        self.name = name
        self.age = age
        self.description = description


    def __setattr__(self, key, value):  # self.aaa =

        if key == 'name':
            if not isinstance(value, str):
                raise TypeError('Name must be str')

            if value == '':
                raise ValueError('Name cannot be empty')

        self.__dict__[key] = value  # словник внутрішніх значеннь


    def __str__(self):
        return f'User: {self.name}, age: {self.age}, description: {self.description}'



alex = User(name='Alex', age=30, description=None)

print(getattr(alex, 'name'))

alex.unicorn = 555
alex.name = ''
print(alex)