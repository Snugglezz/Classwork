def main():
    with(open("Span.txt","r")) as notes:
        for line in notes:
            print(line)


    # file = open("Span.txt", "r")
    # guess = file.readline()
    # while guess != "":
    #    answer = input(f"what is the correct translation for{guess}")


if __name__ == '__main__':
    main()