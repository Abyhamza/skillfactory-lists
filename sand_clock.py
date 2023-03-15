def clock(n):
    for i in range(1, n)[::-1]:
        print(i * '* ')
    for i in range(2, n):
        print(i * '* ')

clock(5)
