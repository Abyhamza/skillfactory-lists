import matplotlib.pyplot as plt

fig = plt.figure()



x_axis = []
y_axis = []

newland = ""
quantity = int(input("Сколько языков программирования вы хотите ввести:"))
while quantity >= 0 and newland != "end":
    # quantity = int(input("Сколько языков программирования вы хотите ввести:"))
    # int_num = int(input())
    lang = input("Введи язык Программирования:")
    x_axis.append(lang)
    students = input("Введите количеcтво студентов:")
    y_axis.append(int(students))
    quantity += 1
    newland = input()

plt.bar(x_axis, y_axis)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.show()
