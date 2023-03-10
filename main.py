from typing import List
# В вашем распоряжении есть некоторые информация о пользователелях банка и их статусе:
# Ушли ли они от нас или нет.
# Необходимо организовать программу,которая:

# 1: Расчитать среднее по признаку кредитного рейтинга для ушедших клиентов
# 2: Средний вораст всех клиентов
# 3: Долю ушедших клиентов
# 4: Выведите идентификаторы клиентов,котрые ущли от банка

users = [
    [15634602, 15647311, 15619304, 15701354],#'CustomerId'
    ['Hargrave', 'Hill', 'Onio', 'Boni'],#'Surname'
    [619, 608, 502, 699],#'CreditScore'
    ['Female', 'Female', 'Female', 'Female'],#'Gender'
    [42, 41, 42, 39],#'Age'
    [1, 0, 1, 0]#'Exitend'
]

# credit_sum = 0
# for score in credit_scores:
#     credit_sum += score
# avg_credit = credit_sum / len(credit_scores)
# print(avg_credit)

# вычиление среднего из списка
def avg(list: List[int]):
    sum = 0
    for score in list:
        sum += score
    avg = sum / len(list)
    return avg
# задача 1 средний кредитный рейтинг
credit_scores = users[2]
print('1: Расчитать среднее по признаку кредитного рейтинга для ушедших клиентов')
print(avg(credit_scores))

# задача 2  средний возрост
ages = users[4]
print('2:Средний вораст всех клиентов')
print(avg(ages))

# задача 3 вычилить долю ушедших клиентов
total_users = len(users[5]) # все пользователи
users_left = 0 #  все ушедшие пользователи
for exited in users[5]:
    if exited == 1:
        users_left += 1
percentage_left = users_left * 100 / total_users
print('3:Долю ушедших клиентов')
print(percentage_left, '%')
print('4: Выведите идентификаторы клиентов,котрые ущли от банка')
for index in range(len(users[5])):
    exited = users[5][index]
    user_id = users[0][index]
    # print(index, exited, user_id)
    if exited == 1:
        print(user_id)

print(not True)
print(not False)

# можно проверить, находиться ли число 1 в промежутке (0,4)
cond1 = 0 < 1
cond2 = 1 < 4

print(cond1 and cond2)

# или, например, содержит ли две строки один и тот же символ
cond3 = 't' in 'python'
cond4 = 't' in 'django'

print(cond3 and cond4)

# к слову, логическое вырожения можно сразу объеденять в одно целое
print(('t' in 'python') or ('t' in 'django'))

print((not True) or (True and not True))

a = 3
b = 4
print(a >= 1 and a > b)
print(a > b or a <= b)
print(not (a > b) and a != b)
print(b != 4 and not(a <= 3))

print('1 : Задача')
# Запишите вместо вопросительных знаков выражение, которое вернет True, если указывается високосный год, иначе False.
#
# Например, x = 2000 -> True; x = 1900 -> False; и т.д.

def is_leap_year_1(x):
    if x % 4 == 0 and x % 100 == 0 and x % 400 == 0:
        return True
    elif x % 4 == 0 and x % 100 == 0:
        return False
    elif x % 4 == 0:
        return True
    return False

def is_leap_year_2(x):
    return ((x % 4 == 0 and x % 100 == 0 and x % 400 == 0) or (x % 4 == 0)) \
        and not (x % 4 == 0 and x % 100 == 0 and not x % 400 == 0)

def is_leap_year(x):
    return (x % 400 == 0) or ((x % 4 == 0) and (x % 100 != 0))

print('Високосная 2000 ', is_leap_year(2000))
print('Високосная 2008 ', is_leap_year(2008))
print('Високосная 1900 ', is_leap_year(1900))

str_list = list(str(123456789))
int_list = list(map(int, str_list))
print('5' in str_list)

def has_3_and_7(n):
    return '3' in str(n) and '7' in str(n)

print(has_3_and_7(123))

a = [1, 2, 3]
print(id(a)) # id возвращает идентификатор объекта

b = a
print(id(b))

print(a is b) # a и b являются одним и тем же объектом

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)

# Хорошо
x = None
print(x is None)

#if # Условие:
    # Блок инструкций 1
#else:
    # Блок инструкций 2

is_rainy = True  # Дождь будет
heavy_rain = False  # несильный дождь

if is_rainy:
    if heavy_rain:
        print("Брать зонт")
    else:
        print("Надеть дождевик")
else:
    print("Не брать зонт")
# msg = input()
# while msg != 'Пока':
#     if msg == 'Привет':
#         print('привет как дела')
#         msg = input()
#         if msg == "Хорошо":
#             print("отлично, а что именно?")
#             msg = input()
#             if msg == 'Работа':
#                 print('super')
#         elif msg == 'Плохо':
#             print("Почему")
#
#     else:
#         print('Я тебя не понял')
#         print('test')
#     msg = input()

# print(bool(0))
# print(bool(1))
#
# print(bool(""))
# print(bool("1"))
#
# print(bool([]))
# print(bool([1]))"


print('2: Задача')
#Запишите вместо вопросительных знаков выражение, которое вернет True, когда каждое из чисел А и В нечетное.
def are_both_odd(A, B):
    if A % 2 == 1 and B % 2 == 1:
        return True
    else:
        return False

print(are_both_odd(2,4))
x = -1
y = -5
if x > 0 and y > 0:
        print("Первая четверть")
if y < 0 and x > 0:
        print("Четвертая четверть")
if x < 0 and y < 0:
        print("Вторая четверть")
if y < 0 and x < 0:
        print("Третья четверть")

# month = int(input())
#
# if month in [3, 4, 5]:
#     print("Весна")
# elif month in [6, 7, 8]:
#     print("Лето")
# elif month in [9, 10, 11]:
#     print("Осень")
# elif month in [12, 1, 2]:
#     print("Зима")

def get_wind_class(speed):
    if speed >= 1 and speed <= 4:
        return "weak [1]"
    elif speed >= 5 and speed <= 10:
        return "moderate [2]"
    elif speed >= 11 and speed <= 18:
        return "strong [3]"
    elif speed >= 19:
        return "hurricane [4]"

get_wind_class(19)

user_database = {
    'usszdzbdzer': 'passwosdhkfbshdjfbdrd',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

db_username: str = 'kazbek'
db_password: str = '1234'

def check_user(username, password):
    return username in user_database and password == user_database[username]


print(check_user('hesoyam','tgm'))

name_phone = {
    'kazbek': '8784734',
    'kamran': '85734909',

}
print(name_phone['kazbek'])

name = [1, 'kazbek', (12, 15, 16)]

print(len(name))

import datetime

open_until = 20
time_now = datetime.datetime.now().hour

tsekh_open = 'open' if time_now < open_until else 'closed'
print(tsekh_open)


print(list(range(12)))

print(list(range(3, 5)))

print(list(range(1, 6, 2)))


S = 0
N = 5

for i in range(1, N + 1):
    print("Значение суммы на предыдушем шаге: ", S)
    print("Текущее число: ", i)
    S = S + i
    print("Значение суммы после сложения: ", S)
    print("___")
print("Конец цикла")
print("Ответ: сумма равна = ", S)


P = 1
N = 5

for i in range(1, N + 1):
    P *= i
    print(P)
