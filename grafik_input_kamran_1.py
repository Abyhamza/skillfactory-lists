import matplotlib.pyplot as plt

fig = plt.figure()



x_axis = []
y_axis = []

lang = ''
while True:
    lang = input("Введи язык Программирования:")
    if lang == "end":
        break
    x_axis.append(lang)
    students = input("Введите количеcтво студентов:")
    y_axis.append(int(students))

plt.bar(x_axis, y_axis)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.show()
