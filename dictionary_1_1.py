# Создайте словарь,где ключи-это название фруктов,а значение-их.
# Используя цикл for,напечатайте каждый ключ и значение.
fruit_color = {
    "яблоко": "красный",
    "банан": "желтый",
    "апельсин": "оранжевый"
}
def printColor(fruit_color):
    for i in fruit_color.items():
        print(i[0], i[1])

printColor(fruit_color)

print('--------')

# Создай словарь,где ключи-это названия города,а значение-их население.
# Используя цикл for,напечатайте каждый ключ и значение.
city_population = {
    "Москва": 12615000,
    "Санкт-Петербург": 5393000,
    "Новосибирск": 1625680
}
def printCity(city_population):
    for i in city_population.items():
        print(i[0], i[1])

printCity(city_population)

print('----------')

# Создайте словарь,где ключи-это название атомобтлей,а значения-их скорости.
# Используя цикл for,напечатайте только ключи.
car_speed = {
    "BMW": 240,
    "Audi": 230,
    "Mercedes": 250
}
def printCar_s(car_speed):
    for i in car_speed.keys():
        print(i)

printCar_s(car_speed)

print('_________')

# Создайте словарь,где ключ-это название книг,а значения-их авторы.
# Используя цикл for,напечатайте только значения.
books_authors = {
    "Война и мир": "Лев Толстой",
    "Преступление и наказания": "Федор Достоевский",
    "Мастер и Маргарита": "Михаил Булгаков"
}
def printBooks_a(books_authors):
    for i in books_authors.values():
        print(i)


printBooks_a(books_authors)

print("_________")

# Создайте словарь,где ключи-это название стран,а значения-их столицы.
# Используя цикл for,напечатайте ключ и значение для каждой страны,где сталица начинаеться с буквы "М"
country_capital = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Италия": "Рим",
    "Германия": "Берлин",
    "Беларусь": "Минск"
}

def printCountry_c(country_capital):
    for i in country_capital.items():
        if i[1][0] == "М":
            print(i[0], i[1])

printCountry_c(country_capital)

