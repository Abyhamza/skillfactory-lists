# Создай список из 5 животных и,используй цикл for,напечатайте каждого животного из списка
animal = ['giraffe', 'tiger', 'a lion', 'hyena', 'puma']
def printAnimal(animal):
    for i in animal:
        print(i)

printAnimal(animal)

print('-------')

# Создай список из 5 чисел,используй цикл for,напечатайте квадрат каждого числа
number = [1, 2, 3, 4, 5]
def printNumber(number):
    for i in number:
        print(i ** 2)

printNumber(number)

print('---------')

# Создай список из 5 имен и, используй цикл for,напечатай длину каждого имени
names = ['artur', 'anwar', 'kamran', 'kazbek', 'nabis']
def printNames(names):
    for i in names:
        print(len(i))

printNames(names)

print('--------')

# Создай список из 5 дней недели и,используй цикл for, напечатайте каждый день недели в верхнем регистре
days_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
def pritnDays_week(days_week):
    for i in days_week:
        print(i.upper())

pritnDays_week(days_week)

print('--------')

# Создайте список из 5 цветов и,используя цикл for,напечатайте каждый цвет в обратном порядке
colors = ['красный', 'синий', 'желтый', 'черный', 'оранджевый']
def printColors(colors):
    for i in colors:
        print(i[::-1])

printColors(colors)





