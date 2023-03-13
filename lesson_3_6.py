
P2 = 1
P2 *= 1
print(P2)
P2 *= 2
print(P2)
P2 *= 3
print(P2)
P2 *= 4
print(P2)
P2 *= 5
print(P2)


str = 'abcdef'

# for i in range(len(str)):
#     print(str[i], end=' ')

count = 1

for i in range(7, 70, 7):
    print(count, '* 7 =', i)
    count += 1

def stars(n):
    for i in range(1, n + 1):
        print(i * '*')

# stars(3)
# stars(5)
# stars(50)

n = 10
class Math:
    n = 14
    def square(self, x):
        return x*x

my_math_object = Math()
print(my_math_object.square(2))
print(my_math_object.square(9))

print(n)
print(my_math_object.n)

S = 0

n = 1

while S < 500:
    S += n
    n += 1

    print("Еще считаюи ...")

print("Сумма равна:", S)
print("Количество чисел:", n - 1)

S = 1

while S * S < 1000:
    S += 1

print(S - 1)

for i in range(1, 1050):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)

def test_return():
    for i in range(1, 1050):
        if i == 3:
            continue
        if i == 5:
            return f'hsfdbd {i}'
        print(i)

result = test_return()
print(result)

N = 2
M = 3
# заполнили матрицу последловательными числами
matrix = [
    [0, 1, 2],
    [3, 4, 5],
]

for i in range(N):# цикл, отвечающий за строки
    for j in range(M):# цикл, отвечающий за столбы
        print(matrix[i][j], end=" ")
    #print()# перенос на навую строку
print()


random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]

min_value_rows = []
min_index_rows = []
max_value_rows = []
max_index_rows = []

for row in random_matrix:
    min_index = 0
    min_value = row[min_index]
    max_index = 0
    max_value = row[max_index]

    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col

    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)

print("Минимальные элементы:", min_value_rows)
print("Их индексы:", min_index_rows)
print("Максимальные элементы:", max_value_rows)
print("Их индексы:", max_index_rows)

print()

# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# for i in range(len(list_)): # равносильна вырожению for i in [0, 1, 2, 3, 4, 5, 6]
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", list_[i]) # c помощью индекса получаем значение элемента
#     print("_____")
# print("Конец цикла")
#
# print()
#
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индек, а затем значение
# # [(0, -5)], (1, 2), (2, 4), ...]
# for i, value in enumerate(list_):
#     print("Индес элемента: ", i)
#     print("Значение элемента: ", value)
# # с помощью индекса получаем значение элемента
#     print("_____")
# print("Конец цикла")


list_ = [-5, 2, 4, 8, 12, -7, 5]
# Объявим переменную, в которой будем хранить индекс отрицательного элемента
index_negative = None

for i, value in enumerate(list_):
    if value < 0:
        print("Отрицательное число: ", value)
        index_negative = i  # перезаписываем значение индекса
        print("Новый индекс отрицательного числа: ", index_negative)
    else:
        print("Положительное число: ", value)
    print("---")
print("Конец цикла")
print()
print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

print("_______")


# Цикл for со строками и словарями

# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """
#
# text = text.lower()
# #text.text.replace(" ", "")
# #text.text.replace("\n", "")
#
# count = {}
# for char in text:
#     if char in count:
#         count[char] += 1
#         print(count)
#     else:
#         count[char] = 1


# for char, cnt in count.items():
#     print(f"Символ{char} встречается {cnt}раз")

# Break

# while True:
#     if n % 3 == 0:
#         n = n // 3
#         if n == 1:
#             break
#         else:
#             break



def check_h(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        if n % 2 == 1:
            n = (n * 3 + 1) // 2
        if n == 1:
            return True
        return False

print(check_h(6))

#n = int(input("Введите число\n"))

# while True:
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = (n * 3 + 1) // 2
#     print(n)
#
#     if n == 1:
#         print("Done")
#         break