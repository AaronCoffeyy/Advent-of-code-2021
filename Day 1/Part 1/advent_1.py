
def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        counter = 0
        previous_line = None
        for line in lines:
            if previous_line and int(line) > previous_line:
                counter = counter + 1
            previous_line = int(line)
        print(counter)


if __name__ == '__main__':
    main()
