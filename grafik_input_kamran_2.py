import matplotlib.pyplot as plt

fig = plt.figure()



x_axis = []
y_axis = []

go_next = ''
while go_next != "no":
    lang = input("Введи язык Программирования:")
    x_axis.append(lang)
    students = input("Введите количеcтво студентов:")
    y_axis.append(int(students))
    go_next = input("Продолжить?(yes/no)")

plt.bar(x_axis, y_axis)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.show()
