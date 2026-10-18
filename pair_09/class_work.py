# book = {
#     'title': "Kobzar",
#     'author': "T. Shevchenko",
#     'copies': 15
# }
# print(book)

# class Book:
#     def __init__(self, title, author, pages, copies):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.copies = copies

#     def available(self):
#         return self.copies > 0



# book1 = Book('Kobzar', "T. Shevchenko", 15)
# # book2 = Book()

# print(book1.title, book1.author, book1.copies)
# print(book1.available())
# print(book2)




# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

#     def info (self):
#         print(f'Recatngle width: {self.width}, height: {self.height}')
#         print(f'Perimeter: {self.perimeter()}')
#         print(f'area: {self.area()}')

# rectangle = Rectangle(4, 5)
# rectangle.info()


# class Counter:
#     def __init__(self):
#         self.value = 0
#     def increment(self):
#         self.value += 1

# counter1 = Counter()
# counter2 = Counter()
# print(f'{counter1.value, counter2.value}')

# counter1.increment()
# counter1.increment()
# print(f'{counter1.value, counter2.value}')


# class Book:
#     def __init__(self, title, copies):
#         self.title = title
#         self.copies = copies

#     def give(self):
#         if self.copies > 0:
#             self.copies -= 1
#             print(f'book was given: {self.title}')
#         else:
#             print(f'there are no copies of {self.title} left')

# book = Book('Kobzar', 3)
# book.give()
# book.give()
# print(f'left: {book.copies}')



class Student:
    def __init__(self, name):
        self.name = name
        self.grades=[]

    def add_grade(self, grade):
        if grade >= 1 and grade <= 12:
            self.grades.append(grade)
        else:
            print('grade must be between 1 and 12')

    def average_grade(self, grade):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def info(self):
        print(f'Name: {self.name}, Grades: {self.grades}')

    def __str__(self):
        return f'Student {self.name}, Grades: {self.grade}, average {self.average_grade}'

# student1 = student('Ivan')
# student2 = student('Ann')
# student1.add_grade(12)
# student2.add_grade(1)
# print(f'Ivan: {student1.grades}, Ann: {student2.grades}')
# print(f'average : {student1.average_grade()}')
# print(f'average : {student2.average_grade()}')


students = [
    Student
]