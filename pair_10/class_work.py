class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return self.name

class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
    def info(self):
        return f'{self.name}, {self.group}'

class Teacher:
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        return f'{self.name}, {self.subject}'

student = Student("Anna", "10IT")
person = Person("Ivan")
teacher = Teacher("Bob", "PE")

people = [Person("Ivan"), Student("Anna", "10IT"), Teacher("MUzhlan", "Math"), Student("Vasyan", "10PTU")]
for person in people:
    print(person.info())

# print(student.name)
# print(student.group)
# print(student.info)
# print(person.info())
# print(student.info())
# print(teacher.info())

print(isinstance(student, Student))