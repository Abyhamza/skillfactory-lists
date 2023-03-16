def clock(n):
    for i in range(1, n)[::-1]:
        print(i * '* ')
    for i in range(2, n):
        print(i * '* ')

clock(5)

def fantesi(n):
    for i in range(0, n):
        print(n * '* # ')
        print(n * '# * ')

fantesi(3)