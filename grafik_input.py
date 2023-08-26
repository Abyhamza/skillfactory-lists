import matplotlib.pyplot as plt

fig = plt.figure()



x_axis = []
y_axis = []

str = input("Введи язык Программирования:")
x_axis.append(str)
str = input("Введите колтичечтво студентов:")
y_axis.append(int(str))
plt.bar(x_axis, y_axis)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.show()
