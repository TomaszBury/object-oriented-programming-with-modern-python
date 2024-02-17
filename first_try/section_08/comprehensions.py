# Python 3: List comprehensions
fruits = ['Banana', 'Apple', 'Lime']
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)

# List and the enumerate function
print(f"\n{list(enumerate(fruits))}\n")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(f"{newlist}\n")

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda number: number**2, numbers))

print(f"{squares}")

mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]


highest_mountains = list(filter(lambda m: m[1] > 8600, mountains))

print(f"{highest_mountains}")