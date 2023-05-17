# Используя вложенные циклы for, напишите программу, которая выводит все возможные комбинации двузначных чисел, которые в сумме дают заданное число n.
# Значение n должно быть предварительно задано.
n = 11
for i in range(n):
    for j in range(n):
        if i + j == n:
            print(f'{i} + {j} = {n}')

print('-------------')

# Используя вложенные циклы for, напишите программу, которая выводит общее количество способов,
# которыми можно разменять заданную сумму n с использованием монет заданных номиналов coins.
# Значение n и список coins должны быть предварительно заданы.
n1 = 10
coins = [1, 2, 5]
for i in coins:
    if i + i + i + i + i + i + i + i + i + i == n1:
        for j in coins:
            if j + j + j + j + j == n1:
                for y in coins:
                    if y + y == n1:
                        print("Количество способов:", n1)



def encode(in_str):
    result = ""
    lastChar = None
    counter = 0
    for i in in_str:
        if lastChar == i and lastChar == None:
            result == "a"
            counter += 1
            print(i)
        elif counter > 1 and counter > 0:
            result == "b"
            counter += 1
            return result
        print(i)


encode("aaabbbbaaabbcccddddd")













