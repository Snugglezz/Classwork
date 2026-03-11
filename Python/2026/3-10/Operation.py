def main():
    a = int(input("please enter a number: "))
    b = int(input("please enter a number: "))
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mult(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")
    print(f"{a} // {b} = {IntDiv(a, b)}")
    print(f"{a} %  {b} = {mod(a, b)}")

def add(a:int, b:int):
    return a + b
def sub(a:int, b:int):
    return a - b
def mult(a:int, b:int):
    return a * b
def div(a:int, b:int):
    return a / b
def IntDiv(a:int, b:int):
    return a // b
def mod(a:int, b:int):
    return a % b

if __name__ == '__main__':
    main()



