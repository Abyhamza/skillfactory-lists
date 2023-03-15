def print_ladder(n):
    if n <= 0:
        print("Число должно быть больше нуля")
        return
    for i in range(1, n + 1):
        print(n * '* ')

print_ladder(10)
print_ladder(6)
print_ladder(7)
