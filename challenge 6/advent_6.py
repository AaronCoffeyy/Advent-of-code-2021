


class Tracker:
    def __init__(self, length):
        self.num_zero = []
        self.num_one = []
        self.gamma = ''
        self.epsilon = ''
        for i in range(length):
            self.num_zero.append(0)
            self.num_one.append(0)

    def add_to_numbers(self, number: []):
        for iterator, i in enumerate(number):
            if int(i) == 1:
                self.num_one[iterator] = self.num_one[iterator] + 1
            else:
                self.num_zero[iterator] = self.num_zero[iterator] + 1

    def print_details(self):
        print("0:", self.num_zero)
        print("1:", self.num_one)
        print("gamma:", self.gamma)
        print("epsilon:", self.epsilon)

    def power_consumption(self):
        for iterator, i in enumerate(self.num_zero):
            if self.num_zero[iterator] > self.num_one[iterator]:
                self.gamma = self.gamma + str(0)
                self.epsilon = self.epsilon + str(1)
            else:
                self.gamma = self.gamma + str(1)
                self.epsilon = self.epsilon + str(0)


def find_number(value, number_list, iterator):
    new_list = []
    for number in number_list:
        if number[iterator] == value[iterator]:
            new_list.append(number)
    return new_list


def getter(list_line, value):
    for i in range(len(list_line[0])):
        tracker = Tracker(len(list_line[0]))
        if len(list_line) == 1:
            break
        for line in list_line:
            tracker.add_to_numbers(line)

        tracker.power_consumption()
        if value == "gamma":
            list_line = find_number(tracker.gamma, list_line, i)
        else:
            list_line = find_number(tracker.epsilon, list_line, i)
    return list_line


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        list_line = lines
        oxygen = getter(list_line, "epsilon")
        co2 = getter(list_line, "gamma")
        print("rate:", int(oxygen[0], 2) * int(co2[0], 2))


if __name__ == '__main__':
    main()

#ans = 2817661

