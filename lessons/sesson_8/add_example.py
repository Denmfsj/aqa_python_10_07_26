

class Subject:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class Group:

    def __init__(self, name, subjects: list[Subject] = None, students: list = None):

        self.name = name
        self.subjects = subjects or []
        self.students = students or []


    def __str__(self):
        return f'Group {self.name}: has {len(self.subjects)} subjects and {len(self.students)} students'


    def __add__(self, other):   # gr1 + gr2, gr1 = self, gr2 = other

        if not isinstance(other, Group):
            print('You can add only another group')
            return None

        res_subj = []
        res_subj.extend(self.subjects)
        res_subj.extend(other.subjects)

        res_students = []  # if append ==> [['Ihor', 'Sofa'], ['Alex', 'Iryna']]
        res_students.extend(self.students)
        res_students.extend(other.students)  ## => ['Ihor', 'Sofa', 'Alex', 'Iryna']

        return Group(name=f'NEW: ({self.name} + {other.name})', subjects=res_subj, students=res_students)


math_subj = Subject('math', 18)
lith_subj = Subject('lith', 22)

math_class = Group('Math-26-01-01', subjects=[math_subj], students=['Ihor', 'Sofa'])
lith_class = Group('Lith-26-01-01', subjects=[lith_subj], students=['Alex', 'Iryna'])



mat_lt_glass = math_class + lith_class  # math_class.__add__(lith_class)
print(mat_lt_glass)
# if not isinstance(other, Group): --> if not isinstance(lith_class, Group):
