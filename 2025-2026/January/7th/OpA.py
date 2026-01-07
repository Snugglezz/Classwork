
my_list = []
print(my_list)
fruits = ["apple", "banana", "orange"]
print(fruits)
fruits.append("grape")
fruits += ["mango"]
print(fruits)
fruits.insert(2, "kiwi")
print(fruits)
print(fruits[0])
print(fruits[5])
print(fruits[2])
fruits.remove("orange")
print(fruits)
fruits.pop(0)
print(fruits)
numbers = [10, 20, 30, 40, 50]
print(len(numbers))
if 30 in numbers:
    print(True)
else:
    print(False)
if 100 in numbers:
    print(True)
else:
    print(False)
print(numbers[0:3])
print(numbers[3:5])
print(numbers[1:3])
colors = ["red", "blue"]
more_colors = ["green", "yellow"]
colors.extend(more_colors)
print(colors)
scores = [85, 92, 78, 90, 88]
scores.sort()
print(scores)
scores.sort(reverse=True)
print(scores)
letters = ["a", "b", "a", "c", "a", "b"]
print(letters.count("a"))
num = [1, 2, 3, 4, 4, 5, 9, 6, 7, 8]
num.clear()
print(num)
movies = ["venom", "SMITSV", "Real Steel", "King Kong", "Cars"]
print(movies)
print(len(movies))
movies.append("Rio")
movies.remove("King Kong")
print(movies)
