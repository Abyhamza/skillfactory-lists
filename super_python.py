my_list = [1, 2, 3, 4]
print(my_list)
last = my_list.pop()
print(my_list)
print(last)
del my_list[-1]
print(my_list)

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# Меняет значение конкретного элемента

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# Указываем новый список и меняем значение по указаному диапозону

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackurrant", "watermelon"]
print(thislist)
# Меняем и добовляем новое значение в список

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# Меняем второе и трьете одним элементом

#thislist = []
#thislist[0] = ["apple"]
#print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# Метод insert добавляет в список новый элемент таким обрзом у нас список будет состят из 4 элементов

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
cars = ["bmx", "vaz", "audi"]
thislist.extend(tropical)
thislist.extend(cars)
print(thislist)
# Таким образом методом extend мы добавили список в список этим мы получили один большой

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
# Таким оброзом метод extend не ограничиваеться дабалением только списка в список но и других типов даных как картеджи,славаря и т.д.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# При помощьи метода remove мы удаляем кокретно указаный элемент

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# При помощьи pop мы удаляем по указаному индексу


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# При помощьи del так же удаляем указанный индекс

thislist = ["apple", "banana", "cherry"]
del thislist[0]
# Так же при помощьи del можно удалит весь список

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# При помощьи метода clear можно опусташить весь список


