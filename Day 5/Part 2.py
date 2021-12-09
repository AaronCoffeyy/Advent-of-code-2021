import re


class Field:
    def __init__(self):
        self.locations = {}

    def add_vents_to_locations(self, locations_dict):
        for location in locations_dict:
            current_value = self.locations.get(f"{location[0]}_{location[1]}", 0)
            self.locations[f"{location[0]}_{location[1]}"] = current_value + 1

    def print_details(self):
        print(self.locations)

    def count_crossover(self):
        return len([x for x in list(self.locations.values()) if x > 1])


def convert_coords_to_line(x1, y1, x2, y2):
    if x1 == x2:
        return [[x1, y] for y in range(min([y1, y2]), max([y1, y2]) + 1)]
    elif y1 == y2:
        return [[x, y1] for x in range(min([x1, x2]), max([x1, x2]) + 1)]
    elif abs(x2 - x1) == abs(y2 - y1) and x1 != x2:
        x = list_between_numbers(x1, x2, -1 if x1 > x2 else 1)
        y = list_between_numbers(y1, y2, -1 if y1 > y2 else 1)
        return [[x[i], y[i]] for i in range(len(x))]
    return []


def list_between_numbers(num_1, num_2, step_value):
    return [num_1 + iterator * step_value for iterator, i in
            enumerate(range(min([num_1, num_2]), max([num_1, num_2]) + 1))]


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        field = Field()
        for line in lines:
            field.add_vents_to_locations(convert_coords_to_line(*[int(x) for x in re.findall("\-?\d+", line)]))
        print(field.count_crossover())


if __name__ == '__main__':
    main()
