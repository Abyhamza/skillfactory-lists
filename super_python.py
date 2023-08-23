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
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
cars = ["bmx", "vaz", "audi"]
thislist.extend(tropical)
thislist.extend(cars)
print(thislist)

# Таким оброзом метод extend не ограничиваеться дабалением только списка в список но и других типов даных как картеджи,славаря и т.д.
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# При помощьи метода remove мы удаляем кокретно указаный элемент
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# При помощьи pop мы удаляем по указаному индексу
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# При помощьи del так же удаляем указанный индекс
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Так же при помощьи del можно удалит весь список
thislist = ["apple", "banana", "cherry"]
del thislist[0]

# При помощьи метода clear можно опусташить весь список
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


x = 1
print(type(x))
mylist = ["apple", "banana", "cherry"]
try:
    print(type(mylist[5]))
except IndexError:
    print("ошибка")

thislist = ["яблоко", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
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
print(massiv[:2])

