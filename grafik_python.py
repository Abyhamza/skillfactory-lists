import matplotlib.pyplot as plt

fig = plt.figure()



x_axis = []
y_axis = []
data = [('C', 23), ('C++', 17), ('Java', 35), ('Python', 29), ('PHP', 12)]

for item in data:
    lang, students = item
    x_axis.append(lang)
    y_axis.append(students)
plt.bar(x_axis, y_axis)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.show()
