thislist = ["яблоко", "вишня"]
thislist_2 = ["яблоко", "банан"]
for x in thislist:
  print(x)

for i in range(len(thislist)):
    print(thislist[i])

thislist = ["яблоко", "банан", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i += 1

i = 0
frukt = thislist[0]
while frukt != "cherry":
    print(frukt)
    i = i + 1
    frukt = thislist[i]


x = 1
x += 2
print(x)

line = input()
print(line)
print(type(line))
while line != "end":
    # обработка
    num = int(line)
    print(num ** 2)
    line = input()


