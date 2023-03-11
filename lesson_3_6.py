
P2 = 1
P2 *= 1
print(P2)
P2 *= 2
print(P2)
P2 *= 3
print(P2)
P2 *= 4
print(P2)
P2 *= 5
print(P2)


str = 'abcdef'

# for i in range(len(str)):
#     print(str[i], end=' ')

count = 1

for i in range(7, 70, 7):
    print(count, '* 7 =', i)
    count += 1

def stars(n):
    for i in range(1, n + 1):
        print(i * '*')

# stars(3)
# stars(5)
# stars(50)

n = 10
class Math:
    n = 14
    def square(self, x):
        return x*x

my_math_object = Math()
print(my_math_object.square(2))
print(my_math_object.square(9))

print(n)
print(my_math_object.n)

S = 0

n = 1

while S < 500:
    S += n
    n += 1

    print("Еще считаюи ...")

print("Сумма равна:", S)
print("Количество чисел:", n - 1)

S = 1

while S * S < 1000:
    S += 1

print(S - 1)

for i in range(1, 1050):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)

def test_return():
    for i in range(1, 1050):
        if i == 3:
            continue
        if i == 5:
            return f'hsfdbd {i}'
        print(i)

result = test_return()
print(result)