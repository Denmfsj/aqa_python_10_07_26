class User:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f'You are going to delete object with id {id(self)}')


user1 = User('Ihor')
user2 = User('Alex')

print(id(user1))
