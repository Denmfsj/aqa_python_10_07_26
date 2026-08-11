

class Course:

    def __init__(self, name, duration, students: list = None ):
        self.name = name
        self.duration = duration
        self.students = students or []  # if bool(students) is True ==> students else []

    def __str__(self):
        return f'{self.name} - {self.duration}, list of students: {self.students}'

    def __len__(self):
        return self.duration


math = Course('Math', 20)
lyth = Course('Lyth', 7, ['Ivan'])

math.students.append('Alex')
lyth.students.append('Alex')

print(math)  # --> print(str(print)) --> print(math.__str__())
print(lyth)

print(len(math))
print(len(lyth))
