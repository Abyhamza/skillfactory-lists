# def clock(n):
#     for i in range(1, n)[::-1]:
#         print(i * '* ')
#     for i in range(2, n):
#         print(i * '* ')
#
# clock(5)
#
def fantesi(n):
    for i in range(0, n):
        for j in range(0, n):
            if (i + j) % 2 == 0:
                print('* ', end= '')
            else:
                print('# ', end= '')
        print()

fantesi(10)

genre = ['поп', 'рок', 'джаз']

for i in range(len(genre)):
    if i == 1:
        print("Мне не нравиться рок")
    else:
        print("Мне нравится", genre[i])


a = 10

if a < 0:
    print("меньше 0")
else:
    print("больше 0")

d = [[1, 2, 3], [4, 5, 6]]

for i in range(2):
    for j in range(3):
        print(d[i][j])

