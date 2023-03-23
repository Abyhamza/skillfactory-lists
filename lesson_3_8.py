ages = [1, 5, 8, 12, 17, 18, 25, 30, 45, 60, 73]

print(ages[5:])

ages1 = [25, 30, 1, 5, 45, 60, 8, 12, 17, 18, 73]
ages1.sort()

print()

for i in ages1[5:]:
    print(i)

print()

ages_1 = [1, 5, 8, 12, 17, 18, 25, 30, 45, 60, 73]

def printAges(ages_1):
    for i in ages_1:
        if i >= 18:
            print(i)
print("printAges function:")
printAges(ages_1)


print()
ages_2 = [('john', 25), ('tom', 30), ('tim', 1), ('jane', 5), ('jack', 45), ('joseph', 60), ('maria', 8), ('kate', 12), ('phillip', 17), ('jody', 18), ('arthur', 73)]
def tupleAges(ages_2):
    for i in ages_2:
        if i[1] >= 18:
            print(i[0])

tupleAges(ages_2)


my_tuple = ("name", 20)
print(my_tuple[1])
if my_tuple[1] >= 18:
    print(my_tuple)