# def clock(n):
#     for i in range(1, n)[::-1]:
#         print(i * '* ')
#     for i in range(2, n):
#         print(i * '* ')
#
# clock(5)
#
# def fantesi(n):
#     for i in range(0, n):
#         if i >= 0:
#             print('# ', end= '')
#         else:
#             print(' *')
#         for j in range(0, n):
#             print('* ', end= ' ')
#         print()
#
# fantesi(3)

genre = ['поп', 'рок', 'джаз']

for i in range(len(genre)):
    if i == 1:
        print("Мне не нравиться рок")
    else:
        print("Мне нравится", genre[i])