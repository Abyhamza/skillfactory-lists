import matplotlib.pyplot as plt

fig = plt.figure()



x_axis = []
y_axis = []

newland = ""
while newland != "end":
    lang = input("Введи язык Программирования:")
    x_axis.append(lang)
    students = input("Введите количеcтво студентов:")
    y_axis.append(int(students))
    newland = "end"

plt.bar(x_axis, y_axis)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.show()
