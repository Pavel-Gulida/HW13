
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.last_name} {self.first_name}, {self.age} age, {self.gender}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.gender = gender
        self.record_book = record_book

    def __str__(self):
        return f"{self.last_name} {self.first_name}, {self.age} age, {self.gender}, {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student = 0
        for el in self.group:
            if el.last_name == last_name:
                student = el
        self.group.discard(student)


    def find_student(self, last_name):
        for el in self.group:
            if el.last_name == last_name:
                return el

    def __str__(self):
        all_students = ""
        for el in self.group:
            all_students += str(el) + "\n"
        return f'Number: {self.number}\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
