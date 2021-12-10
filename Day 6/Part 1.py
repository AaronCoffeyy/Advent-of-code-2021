import re


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        list_of_fish = []
        for line in lines:
            list_of_fish = [*list_of_fish, *[int(i) for i in re.findall('[0-9]', line)]]
        for day in range(80):
            print(f"Day {day+1}")
            for iterator, fish_timer in enumerate(list_of_fish):
                if fish_timer == 0:
                    list_of_fish[iterator] = 6
                    list_of_fish.append(9)
                else:
                    list_of_fish[iterator] -= 1
        print(len(list_of_fish))


if __name__ == '__main__':
    main()
