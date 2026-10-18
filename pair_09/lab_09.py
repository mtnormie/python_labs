#1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

#     def info(self):
#         print(f"{self.width} * {self.height}: area = {self.area()}, perimeter = {self.perimeter()}")


# r1 = Rectangle(5, 3)
# r2 = Rectangle(10, 4)

# r1.info()
# r2.info()


#2
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []

#     def add_grade(self, grade):
#         if 1 <= grade <= 12:
#             self.grades.append(grade)
#         else:
#             print('grade should be in diapazon from 1 to 12')

#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)

#     def __str__(self):
#         return f"{self.name}: {self.grades}, average = {self.average():.2f}"


# student = Student("Ivan Vorobiov")

# student.add_grade(10)
# student.add_grade(12)
# student.add_grade(15)
# student.add_grade(9)

# print(student)



#3
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []

#     def add_grade(self, grade):
#         if 1 <= grade <= 12:
#             self.grades.append(grade)

#     def average(self):
#         if not self.grades:
#             return 0
#         return sum(self.grades) / len(self.grades)

#     def __str__(self):
#         return f"{self.name} — {self.average():.2f}"


# students = [
#     Student("Anna"),
#     Student("Ivan"),
#     Student("Sidelnik"),
#     Student("Illya"),
#     Student("Puzenko")
# ]

# students[0].grades = [10, 11, 11]
# students[1].grades = [9, 10]
# students[2].grades = [11, 12, 11]
# students[3].grades = [8, 9, 10]
# students[4].grades = [12, 10, 11]

# for student in students:
#     print(student)

# best_average = max(student.average() for student in students)

# print("\nbest result:")
# for student in students:
#     if student.average() == best_average:
#         print(f"{student.name} — {student.average():.2f}")


#4
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Помилка: сума поповнення має бути більшою за 0")
#         else:
#             self.balance += amount

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Помилка: сума списання має бути більшою за 0")
#         elif amount > self.balance:
#             print(f"Помилка: недостатньо коштів для -{amount}")
#         else:
#             self.balance -= amount

#     def info(self):
#         print(f"{self.owner}: баланс {self.balance}")


# account1 = BankAccount("Ivan", 1000)
# account2 = BankAccount("Olha", 700)

# account1.deposit(500)
# account1.withdraw(300)
# account1.withdraw(2000)

# account2.withdraw(200)
# account2.deposit(100)

# account1.info()
# account2.info()