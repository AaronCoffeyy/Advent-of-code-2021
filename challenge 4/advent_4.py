
class Submarine:
    def __init__(self, hor, depth, aim):
        self.hor = hor
        self.depth = depth
        self.aim = aim

    def move(self, command):
        if "forward" in command:
            self.hor = self.hor + int(command[-1])
            self.depth = self.depth + (self.aim * int(command[-1]))
        elif "up" in command:
            self.aim = self.aim - int(command[-1])
        elif "down" in command:
            self.aim = self.aim + int(command[-1])
        else:
            print("back comamand")

    def print_pos(self):
        print("hor:", self.hor, "depth:", self.depth, "aim:", self.aim)
        print("multiply:", self.hor * self.depth)


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        submarine = Submarine(0, 0, 0)
        for line in lines:
            submarine.move(line)
        submarine.print_pos()


if __name__ == '__main__':
    main()

#ans = 1858