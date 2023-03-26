# Создайте список из чисел и,используя цикл for,напечатайте куб каждого числа
number = [1, 3, 5, 7, 9]
def printNumbers(number):
    for i in number:
        print(i ** 3)

printNumbers(number)

print('________')

# Создай список из чисел и,используй цикл for,напечатай только четные числа
numbers = [2, 4, 6, 8, 10, 13, 15]
def printNumber1(numders):
    for i in numders:
        if i % 2 == 0:
            print(i)

printNumber1(numbers)

print('---------')

# Создайте список из чисел и,используя цикл for,выведите на печать сумму всех числе
number1 = [5, 10, 15, 20, 25]
def printNumbers1(number1):
    sum_ = 0
    for i in number1:
        sum_ += i
    print(sum_)

printNumbers1(number1)

print('---------')

# Создайте список из чисел и,используя цикл for,найдите нибольшее число в списке
max_number = [34, 2, 56, 12, 89, 5]
def printNumbers2(max_number):
    largest_number = None
    for i in max_number:
        if largest_number is None or i > largest_number:
            largest_number = i
    print(largest_number)

printNumbers2(max_number)

print('--------')

min_number = [34, 2, 56, 12, 89, 5]
def printNumbers2(min_number):
    largest_number = None
    for i in min_number:
        if largest_number is None or i < largest_number:
            largest_number = i
    print(largest_number)

printNumbers2(min_number)


print("_______")

# Создайте список из чисел и,испольуя цикл for,напечатайте все числа,которые делятся на 3 без остатка
number2 = [3, 15, 25, 30, 45, 50, 60, 70, 75, 90]
def printNumber2(number2):
    for i in number2:
        if i % 3 == 0:
            print(i)

printNumber2(number2)