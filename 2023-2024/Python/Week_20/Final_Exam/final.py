def main() -> object:
    words = []
    with open('dictionary.txt', 'r') as f:
        for line in f:
            words.append(line.strip())

    print(words)

    words.sort()
    print("ACE" in words)
    print("face" in words)

    words

if __name__ == '__main__':
    main()
