import random
def main():
    trans = {}
    with(open("Span.txt","r")) as notes:
        for line in notes:
            span = line.strip()
            store = span.split(":")
            key = store[1]
            val = store[0]
            trans[key] = val
    # print(trans)
    quit = "Y"
    while quit == "Y":
        item = random.choice(list(trans.keys()))
        answer = input(f"Whats the translation to {item}? ")
        if answer == trans.get(item) :
            print(f"Correct! the Answer is {trans[item]}")
        else:
            print(f"Wrong! the Answer is {trans[item]}")
        quit = input("Do you want to continue? Y/N ")

if __name__ == '__main__':
    main()