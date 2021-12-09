def sum_and_compare(a, b, c, d, e, f):
    if (int(a) + int(b) + int(c)) < (int(d) + int(e) + int(f)):
        return 1
    return 0


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        counter = 0
        for i in range(len(lines)-3):
            counter = counter + sum_and_compare(*lines[i:3 + i], *lines[i + 1:3 + i + 1])
        print(counter)


if __name__ == '__main__':
    main()

#ans = 1858