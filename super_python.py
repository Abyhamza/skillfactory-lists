my_list = [1, 2, 3, 4]
print(my_list)
last = my_list.pop()
print(my_list)
print(last)
del my_list[-1]
print(my_list)

# Меняет значение конкретного элемента
thislist = ["яблоко", "банан", "вишня"]
thislist[1] = "черника"
print(thislist)

# Указываем новый список и меняем значение по указаному диапозону
thislist = ["яблоко", "банан", "вишня", "апельсин", "киви", "манго"]
thislist[3:5] = ["арбуз", "черника"]
print(thislist)

# Меняем и добовляем новое значение в список
thislist = ["яблоко", "банан", "вишня"]
thislist[1:2] = ["арбуз", "черника"]
print(thislist)

# Меняем второе и трьете одним элементом
thislist = ["яблоко", "банан", "вишня"]
thislist[1:3] = ["арбуз"]
print(thislist)


#thislist = []
#thislist[0] = ["apple"]
#print(thislist)
# Метод insert добавляет в список новый элемент таким обрзом у нас список будет состят из 4 элементов
thislist = ["яблоко", "банан", "вишня"]
thislist.insert(1, "апельсин")
print(thislist)

# Таким образом методом extend мы добавили список в список этим мы получили один большой
thislist = ["яблоко", "банан", "вишня"]
tropical = ["манго", "ананс", "папая"]
cars = ["БМВ", "ВАЗ", "АУДИ"]
thislist.extend(tropical)
thislist.extend(cars)
thislist.extend(cars)
print(thislist)

# Таким оброзом метод extend не ограничиваеться дабалением только списка в список но и других типов даных как картеджи,славаря и т.д.
thislist = ["яблоко", "банан", "вишня"]
thistuple = ("арбуз", "дыня")
thislist.extend(thistuple)
print(thislist)

# При помощьи метода remove мы удаляем кокретно указаный элемент
thislist = ["яблоко", "банан", "вишня"]
thislist.remove("банан")
print(thislist)

print("При помощьи pop мы удаляем по указаному индексу")
thislist = ["яблоко", "банан", "вишня"]
print(thislist.pop(1))


# При помощьи del так же удаляем указанный индекс
thislist = ["яблоко", "банан", "вишня"]
del thislist[0]
print(thislist)

print("Так же при помощьи del можно удалит весь список")
thislist = ["яблоко", "банан", "вишня"]
del thislist

print("При помощьи метода remove можно опусташить весь список")
thislist = ["яблоко", "банан", "вишня"]
if "вишня" in thislist:
    thislist.remove("вишня")
print(thislist)


x = 1
print(type(x))
mylist = ["яблоко", "банан", "вишня"]
try:
    print(type(mylist[5]))
except IndexError:
    print("ошибка")

thislist = ["яблоко", "банан", "вишня", "апельсин", "киви", "дыня", "манго"]
print(thislist[1:-1])

is_apple_in_list = "яблоко" in thislist
print(is_apple_in_list)
if is_apple_in_list:
    print("Яблоко есть в списке")

if 0 < 1 and is_apple_in_list:
    print("0 больше одного")

is_true = 0 == 0
print(type(is_true))
is_true = "True"
print(type(is_true))

massiv = ["яблоко", "банан", "вишня"]
print(massiv[1:2])
print(massiv[0][0])

for i in range(0,  10):
    if i > 5 and is_apple_in_list:
        print(i)

list_1 = ["яблоко", "банан", "арбуз"]
name_1, name_2, name_3 = list_1
print(name_1, name_2, name_3)


name = "artur"
name = "kazbek"
name = ["artur", "kazbek"]
print(name)


