#1
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         return f"Ім'я: {self.name}"


# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group

#     def info(self):
#         return f"Учень: {self.name}, група: {self.group}"


# student1 = Student("Anna Ivanenko", "IT-10")
# student2 = Student("Ivan Petrenko", "IT-11")

# print(student1.info())
# print(student2.info())




#2
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         return f"Ім'я: {self.name}"


# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group

#     def info(self):
#         return f"Учень: {self.name}, група: {self.group}"


# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

#     def info(self):
#         return f"Викладач: {self.name}, предмет: {self.subject}"


# people = [
#     Person("Ivan Komarov"),
#     Student("Anna Ivanenko", "IT-10"),
#     Student("Ivan Petrenko", "IT-11"),
#     Teacher("Olena Kovalenko", "Python")
# ]

# for person in people:
#     print(person.info())



#3
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         return f"Ім'я: {self.name}"


# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group

#     def info(self):
#         return f"Учень: {self.name}, група: {self.group}"


# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

#     def info(self):
#         return f"Викладач: {self.name}, предмет: {self.subject}"


# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         for existing in self.students:
#             if existing.name.casefold() == student.name.casefold():
#                 print("Такий студент уже існує.")
#                 return

#         self.students.append(student)

#     def remove_student(self, name):
#         for student in self.students:
#             if student.name.casefold() == name.casefold():
#                 self.students.remove(student)
#                 print("Студента видалено.")
#                 return

#         print("Студента не знайдено.")

#     def show_students(self):
#         print(f"Курс: {self.title}")
#         print(self.teacher.info())
#         print("Студенти:")

#         for index, student in enumerate(self.students, start=1):
#             print(f"{index}. {student.info()}")


# teacher = Teacher("Olena Kovalenko", "Python")
# course = Course("Python", teacher)

# course.add_student(Student("Anna Ivanenko", "IT-10"))
# course.add_student(Student("Ivan Petrenko", "IT-10"))
# course.add_student(Student("Olha Shevchenko", "IT-11"))
# course.add_student(Student("Andrii Bondar", "IT-11"))

# course.remove_student("Ivan Petrenko")
# course.show_students()



#4

class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Ім'я: {self.name}"


class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
        self.grades = []

    def info(self):
        return f"Учень: {self.name}, група: {self.group}"

    def add_grade(self, grade):
        if not isinstance(grade, (int, float)) or isinstance(grade, bool) or not 1 <= grade <= 12:
            raise ValueError("Оцінка повинна бути від 1 до 12.")

        self.grades.append(grade)

    def average(self):
        if len(self.grades) == 0:
            return 0

        return sum(self.grades) / len(self.grades)


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def info(self):
        return f"Викладач: {self.name}, предмет: {self.subject}"


class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        if self.find_student(student.name) is not None:
            print("Такий студент уже існує.")
            return

        self.students.append(student)
        print("Студента додано.")

    def remove_student(self, name):
        student = self.find_student(name)

        if student is None:
            print("Студента не знайдено.")
            return

        self.students.remove(student)
        print("Студента видалено.")

    def find_student(self, name):
        for student in self.students:
            if student.name.casefold() == name.strip().casefold():
                return student

        return None

    def add_grade_to_student(self, name, grade):
        student = self.find_student(name)

        if student is None:
            print("Студента не знайдено.")
            return

        try:
            student.add_grade(grade)
            print("Оцінку додано.")
        except ValueError as error:
            print(error)

    def show_students(self):
        print(f"\nКурс: {self.title}")
        print(self.teacher.info())
        print("Студенти:")

        if len(self.students) == 0:
            print("Список порожній.")

        for index, student in enumerate(self.students, start=1):
            print(f"{index}. {student.info()}")

    def show_rating(self):
        print("\nРейтинг:")

        # Сортування без lambda
        sorted_students = sorted(
            self.students,
            key=average_key,
            reverse=True
        )

        for index, student in enumerate(sorted_students, start=1):
            print(f"{index}. {student.name} — {student.average():.2f}")

    def save(self, filename="course_data.txt"):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for student in self.students:
                    grades = ",".join(map(str, student.grades))
                    file.write(
                        f"{student.name}\t{student.group}\t{grades}\n"
                    )

            print("Дані збережено.")

        except OSError as error:
            print(f"Помилка збереження: {error}")

    def load(self, filename="course_data.txt"):
        self.students = []

        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    try:
                        parts = line.rstrip("\n").split("\t")

                        if len(parts) != 3:
                            raise ValueError("Неправильний формат рядка.")

                        name, group, grades_text = parts

                        if not name.strip() or not group.strip():
                            raise ValueError("Порожнє ПІБ або група.")

                        student = Student(name, group)

                        if grades_text:
                            for grade_text in grades_text.split(","):
                                student.add_grade(float(grade_text))

                        if self.find_student(student.name) is not None:
                            raise ValueError("Дублікат ПІБ.")

                        self.students.append(student)

                    except ValueError as error:
                        print(f"Помилка у рядку {line_number}: {error}")

            print("Завантаження завершено.")

        except FileNotFoundError:
            print("Файл не знайдено. Починаємо з порожнього списку.")

        except OSError as error:
            print(f"Помилка читання файлу: {error}")


def average_key(student):
    return student.average()


def main():
    teacher = Teacher("Olena Kovalenko", "Python")
    course = Course("Python", teacher)

    course.load()

    while True:
        print("\n===== НАВЧАЛЬНИЙ КУРС =====")
        print("1 — Показати курс")
        print("2 — Додати студента")
        print("3 — Видалити студента")
        print("4 — Знайти студента")
        print("5 — Виставити оцінку")
        print("6 — Показати рейтинг")
        print("7 — Зберегти дані")
        print("0 — Вихід")

        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            course.show_students()

        elif choice == "2":
            name = input("ПІБ студента: ").strip()
            group = input("Група: ").strip()

            if name and group:
                course.add_student(Student(name, group))
            else:
                print("ПІБ і група не можуть бути порожніми.")

        elif choice == "3":
            name = input("ПІБ студента: ")
            course.remove_student(name)

        elif choice == "4":
            name = input("ПІБ студента: ")
            student = course.find_student(name)

            if student is not None:
                print(student.info())
                print("Оцінки:", student.grades)
                print(f"Середній бал: {student.average():.2f}")
            else:
                print("Студента не знайдено.")

        elif choice == "5":
            name = input("ПІБ студента: ")

            try:
                grade = float(input("Оцінка (1–12): "))
                course.add_grade_to_student(name, grade)
            except ValueError:
                print("Введіть правильну оцінку від 1 до 12.")

        elif choice == "6":
            course.show_rating()

        elif choice == "7":
            course.save()

        elif choice == "0":
            course.save()
            print("Програму завершено.")
            break

        else:
            print("Неправильний пункт меню.")


if __name__ == "__main__":
    main()
