import re


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        list_of_positions = []
        for line in lines:
            list_of_positions = [*list_of_positions, *[int(i) for i in re.findall('\-?\d+', line)]]
        fuel = [0 for i in range(max(list_of_positions))]
        for pos, i in enumerate(fuel):
            fuel[pos] += sum([sum(range(1, (abs(x - pos)+1))) for x in list_of_positions])
        print(min(fuel))


if __name__ == '__main__':
    main()
