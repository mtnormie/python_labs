#1
# with open("text.txt", encoding="utf-8") as file:
#     text = file.read()

# lines = text.splitlines()
# words = text.split()

# print("Рядків:", len(lines))
# print("Слів:", len(words))
# print("Символів:", len(text))

# if lines:
#     longest = max(lines, key=len)
#     number = lines.index(longest) + 1
#     print("Найдовший рядок: No", number, ",", len(longest), "символів")
#     print("Текст:", longest)

#2
# fragment = input("Фрагмент: ").lower()
# found = False

# with open("text.txt", encoding="utf-8") as file:
#     lines = file.readlines()

# for i in range(len(lines)):
#     if fragment in lines[i].lower():
#         print(i + 1, ":", lines[i].strip())
#         found = True

# if not found:
#     print("Збігів немає")


#3

# students = []

# with open("students.txt", encoding="utf-8") as file:
#     for line in file:
#         name, score = line.strip().split(";")
#         score = int(score)

#         if score > 80:
#             students.append([name, score])

# for i in range(len(students)):
#     for j in range(i + 1, len(students)):
#         if students[i][1] < students[j][1]:
#             students[i], students[j] = students[j], students[i]

# with open("result.txt", "w", encoding="utf-8") as file:
#     for student in students:
#         file.write(student[0] + ";" + str(student[1]) + "\n")


#4
# students = {}

# with open("grades.csv", encoding="utf-8") as file:
#     for line in file:
#         name, subject, grade = line.strip().split(";")
#         grade = float(grade)

#         if name not in students:
#             students[name] = []

#         students[name].append(grade)

# results = []

# for name in students:
#     grades = students[name]
#     average = sum(grades) / len(grades)
#     results.append([name, len(grades), average])

# for i in range(len(results)):
#     for j in range(i + 1, len(results)):
#         if results[i][2] < results[j][2]:
#             results[i], results[j] = results[j], results[i]

# with open("report.txt", "w", encoding="utf-8") as file:
#     for student in results:
#         file.write(student[0] + "; Кількість оцінок: " + str(student[1]) +
#                    "; Середній бал: " + str(round(student[2], 2)) + "\n")

#     if len(results) > 0:
#         file.write("\nBest student " + results[0][0] + " , : " + str(round(results[0][2], 2)))