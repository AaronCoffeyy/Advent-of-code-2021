
class Tracker:
    def __init__(self, length):
        self.num_zero = []
        self.num_one = []
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

    def power_consumption(self):
        gamma = ''
        epsilon = ''
        for iterator, i in enumerate(self.num_zero):
            if self.num_zero[iterator] > self.num_one[iterator]:
                gamma = gamma + str(0)
                epsilon = epsilon + str(1)
            else:
                gamma = gamma + str(1)
                epsilon = epsilon + str(0)
        print("gamma:", gamma)
        print("epsilon:", epsilon)
        print("power consumption:", int(epsilon, 2) * int(gamma, 2))


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        tracker = Tracker(len(lines[0]))
        for line in lines:
            tracker.add_to_numbers(line)
        tracker.power_consumption()
        tracker.print_details()


if __name__ == '__main__':
    main()

#ans = 2035764