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
    for char in in_str:
        if lastChar != char and lastChar != None:
            result += f"{lastChar}{counter}"
            counter = 1
            lastChar = char
        else:
            counter += 1
            lastChar = char
    return result

test_in_1 =  "aaabbbbaaabbcccddddd"
test_out_1 = "a3b4a3b2c3d5"
test_result_1 = encode(test_in_1)
print(f"{test_in_1} => {test_out_1} == {test_result_1} is {test_out_1 is test_result_1}")

test_in_2 =  "jjjjkkkkaaaaasss"
test_out_2 = "j4k4a5s3"
test_result_2 = encode(test_in_2)
print(f"{test_in_2} => {test_out_2} == {test_result_2} is {test_out_2 is test_result_2}")
















