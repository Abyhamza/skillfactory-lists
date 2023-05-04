# Напишите программу с использованием вложенных циклов for, которая создает таблицу умножения от 1 до 10 и выводит ее.
for i in range(1, 11):
    print()
    for j in range(1, 11):
        print(i * j, end=' ')

print()

# Используя вложенные циклы for, напишите программу, которая выводит все комбинации карт из колоды карт для игры в покер
# (масть: "♠", "♣", "♦", "♥"; ранг: "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A").
# Выведите каждую комбинацию в отдельной строке.
mast = ["♠", "♣", "♦", "♥"]
rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
for i in (mast):
    print()
    for j in (rank):
        print(i + j)

print("_____________")

#Используя вложенные циклы for, напишите программу, которая выводит все возможные пары сумма которых равна заданному числу n.
# Значение n должно быть предварительно задано.
n = 5
for i in range(1, n):
    for j in range(1, n)[::-1]:
        if i + j == n:
            print(f"{i}, {j}")

print('---------')

# Используя вложенные цикл for,напишите программу,которая выводит все возможные тройки чисел из списка numbers.
# Сумма которых равна заданному чисел target_sum.
# Список numbers должен быть предварительно задан.
numbers = [1, 2, 3, 4, 5]
target_sum = 7
for i in numbers:
    for j in numbers:
        for x in numbers:
            if i + j + x == target_sum:
                print(i, j, x)

print('_________')

#Используя вложенные циклы for, напишите программу, которая выводит все подмножества заданного списка elements.
# Результат должен быть представлен в виде строк, в которых элементы подмножества разделены запятыми.
elements = ['A', 'B', 'C']
for i in elements:
    print(i)
    for j in elements:
        if i != j and j != i:
            print(f'{i}, {j}')
        for x in elements:
            if i != j and j != x and i != x:
                print(f'{i}, {j}, {x}')


numbers1 = [1, 2, 3, 4, 5]
target_sum1 = 25
for i in numbers1:
    for j in numbers1:
        for x in numbers1:
            for y in numbers1:
                for h in numbers1:
                    if i + j + x + y + h == target_sum1:
                        print(i, j, x, y, h)


