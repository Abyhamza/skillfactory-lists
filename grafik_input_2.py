import matplotlib.pyplot as plt

fig = plt.figure()



x_axis = []
y_axis = []

quantity = int(input("Сколько языков программирования вы хотите ввести:"))
while quantity >= 1:
    lang = input("Введи язык Программирования:")
    x_axis.append(lang)
    students = input("Введите количеcтво студентов:")
    y_axis.append(int(students))
    quantity -= 1


plt.bar(x_axis, y_axis)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.show()
