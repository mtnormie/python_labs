#1
# while True:
#     try:
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
#         op = input("Choose operation (+, -, *, /): ")

#         if op == "+":
#             print(num1 + num2)
#         elif op == "-":
#             print(num1 - num2)
#         elif op == "*":
#             print(num1 * num2)
#         elif op == "/":
#             print(num1 / num2)
#         else:
#             print("Unknown operation")

#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     except ValueError:
#         print("Please enter valid integers")


#2
# def get_grade():
#     while True:
#         try:
#             value = int(input("Enter grade: "))

#             if value < 1 or value > 12:
#                 print("Grade must be between 1 and 12")
#                 continue

#             return value

#         except ValueError:
#             print("Please enter an integer")

# grade = get_grade()
# print(f"Your grade: {grade}")


#3
# students = ["Vorobiov", "Leshenko", "Plush", "Sidelnik"]

# grades = {
#     "Math": 11,
#     "Ukrainian": 2,
#     "Physics": 9,
#     "History": 6
# }

# try:
#     option = int(input("Choose 1 for student or 2 for subject: "))

#     if option == 1:
#         try:
#             index = int(input("Enter student index: "))
#             print("Student:", students[index])
#         except ValueError:
#             print("Index must be an integer")
#         except IndexError:
#             print("Student not found")

#     elif option == 2:
#         try:
#             subject = input("Enter subject name: ")
#             print("Grade:", grades[subject])
#         except KeyError:
#             print("Subject not found")

#     else:
#         print("Choose 1 or 2")

# except ValueError:
#     print("Please enter an integer")


#4
try:
    records = []
    skipped = 0

    with open("students.txt", "r", encoding="utf-8") as source:
        for line_num, row in enumerate(source, start=1):
            row = row.strip()

            if row == "":
                continue

            try:
                data = row.split(";")

                if len(data) != 2:
                    raise ValueError("invalid format")

                name = data[0].strip()
                mark = int(data[1].strip())

                if mark < 0 or mark > 100:
                    raise ValueError("mark must be from 0 to 100")

                records.append((name, mark))

            except ValueError as error:
                skipped += 1
                print(f"Line {line_num}: {error}")

except FileNotFoundError:
    print("File not found")

else:
    records.sort(key=lambda record: record[1], reverse=True)

    with open("report.txt", "w", encoding="utf-8") as output:
        for name, mark in records:
            print(f"{name};{mark}", file=output)

    print("Valid records:", len(records))
    print("Skipped lines:", skipped)
    print("Report saved successfully")
