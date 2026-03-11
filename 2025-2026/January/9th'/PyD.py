my_dict = {}
print(my_dict)
student = {"name": "Alice", "age": 20, "major": "Computer Science"}
print(student)
print(student["name"])
print(student["age"])
student.update({"gpa" : 3.8, "year" : "Senior"})
print(student)
popped = student.pop("gpa")
print(popped)
print(student)
print(student.keys())
print(student.values())
print(student.items())
if "major" in student:
    print(True)
else:
    print(False)
if "gpa" in student:
    print(True)
else:
    print(False)
inventory = {"apples": 5, "bananas": 3}
print(inventory.get("apples"))
print(inventory.get("oranges", 0))
prices = {"milk": 3.50, "bread": 2.00}
new_prices = {"egg": 4.00, "milk": 3.75}
prices.update(new_prices)
print(prices)
print(len(prices))
grades = {"Math": 95, "Science": 88, "English": 92}
print(grades)
for scores in grades.items():
    print(scores)
num = {"one": 1, "two": 2, "three": 3}
num.clear()
print(num)
contact = {"name": "isaiah", "email": "ihensley@bostonk12.org", "phone": 617-275-9845, "city": "boson"}
print(contact)
print(len(contact))
contact.update({"hobby": "music"})
contact.update({"phone": 222-333-4567})
print(contact.keys())
print(contact)













