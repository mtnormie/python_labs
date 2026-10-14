import os

# print("creating file")
# with open('hello.txt', "w", encoding ="utf-8") as file:
#     file.write("Ann promises to learn")

# r - read
# w - write
# a - append
# x - exclusive creation


if not os.path.exists('numbers.txt'):
    with open('numbers.txt', "w", encoding ="utf-8") as file:
        file.write("12\n8\n25\n4\n16\n")


if not os.path.exists('student.txt'):
    with open('student.txt', "w", encoding ="utf-8") as file:
        file.write("Ivanenko Anna;91\n")
        file.write("Leshchenko Ivan;76\n")
        file.write("Komarova Sophie;97\n")
        file.write("Bondarenko Illya;84\n")


if not os.path.exists('grades.csv'):
    with open('grades.csv', "w", encoding ="utf-8") as file:
        file.write("Anna;Python;11\n")
        file.write("Anna;Math;10\n")
        file.write("Ivan;Python;6\n")
        file.write("Ivan;Math;5\n")
        file.write("Sophie;Python;11\n")
        file.write("Sophie;Math;12\n")
        file.write("Illya;Python;9\n")
        file.write("Illya;Math;8\n")


with open('text.txt', 'r', encoding="utf-8") as file:
    text = file.read()
print(text)

with open('log.txt', 'w', encoding = "utf-8") as file:
    file.write('first launch\n')

with open('log.txt', 'w', encoding = "utf-8") as file:
    file.write("second launch, first is deleted")

with open('log.txt', 'a', encoding = "utf-8") as file:
    file.write('new info adding to the end\n')

with open('log.txt', 'r', encoding = "utf-8") as file:
    print(file.read())


#methods of reading
with open('text.txt', 'r', encoding = "utf-8") as file:
    text = file.read()
print(f'read -> {type(text)}, count -> {len(text)}')

with open('text.txt', 'r', encoding="utf-8") as file:
    line1 = file.readline()
    line2 = file.readline()
    other_lines = file.readlines()

print(line1)
print(line2)
print(other_lines)

with open('text.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
print(other_lines)
print(other_lines[0] if lines else 'file is empty')



#перебір файлу
with open('text.txt', 'r', encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        clean_line = line.strip()
        print(f'number -> {number}, line -> {clean_line}')



