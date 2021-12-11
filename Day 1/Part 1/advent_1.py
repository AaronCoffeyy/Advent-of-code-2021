
def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        counter = sum([1 for num, x in enumerate(lines[:-1]) if (int(x) < int(lines[num + 1]))])
        print(counter)


if __name__ == '__main__':
    main()
