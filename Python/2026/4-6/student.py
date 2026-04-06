#Isaiah Hensley
#April 6th, 2026
class Student:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
def main():
    isaiah = Student("Isaiah", 18, 6.1, 250)

    print(isaiah.age)
    print(isaiah.height)
    print(isaiah.weight)

if __name__ == '__main__':
    main()
