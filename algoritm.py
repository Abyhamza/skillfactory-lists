from super_python import my_list

def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
            return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 1))


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selectionSort(arr):
    newArr = []
    for _ in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10, 9]))

def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key")


#def look_for_key(box):
#    for item in box:
 #       if item.is_a_box():
  #         look_for_key(item):
   #     elif item.is_a_key():
    #        print("found the key")


def countdown(i):
    print(i)
    if i <= 2:
     return
    else:
     countdown(-1)

def quicksort(array):
    if len(array) > 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i > pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))


arr = [1,2,3,4,5,6,7,8,9,10]

for i in range(1, 11):
    for num in arr:
        print(f"{num} × {i} = {num * i}")
    print()  # пустая строка между строками таблицы

book = {
        'avocado': 1.49, 'apple': 0.67, 'milk': 1.49}
print(book['avocado'])

voted = {}
def check_voter(name):


    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them voted!")
check_voter("tom")
check_voter("mike")
check_voter("mike")



from collections import deque

graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

def person_is_seller(name):
    return name.endswith("b")

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False

search("you")
