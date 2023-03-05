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
