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


