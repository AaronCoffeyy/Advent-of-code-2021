import re


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        list_of_fish = []
        for line in lines:
            list_of_fish = [*list_of_fish, *[int(i) for i in re.findall('[0-9]', line)]]
        births_per_day = [len([fish for fish in list_of_fish if fish == i]) for i in range(9)]
        for i in range(256):
            start_value = births_per_day[0]
            for j in range(1, 9):
                births_per_day[j-1] = births_per_day[j]
            births_per_day[8] = start_value
            births_per_day[6] += start_value
        print(sum(births_per_day))


if __name__ == '__main__':
    main()
