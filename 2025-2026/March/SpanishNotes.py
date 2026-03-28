def main():
    file = open("Span.txt", "r")
    guess = file.readline()
    while guess != "":
       answer = input(f"what is the correct translation for{guess}")


if __name__ == '__main__':
    main()