import re


def check_adj(center, top, bottom, left, right):
    return center + 1 if (center < top and center < bottom and center < left and center < right) else 0


def get_adj_values(center_pos_x, center_pos_y, array):
    return [
        array[center_pos_y-1][center_pos_x] if center_pos_y >= 1 else 99,
        array[center_pos_y+1][center_pos_x] if center_pos_y < len(array) - 1 else 99,
        array[center_pos_y][center_pos_x-1] if center_pos_x >= 1 else 99,
        array[center_pos_y][center_pos_x+1] if center_pos_x < len(array[center_pos_y]) - 1 else 99,
    ]


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        points = []
        for line in lines:
            points.append([int(i) for i in re.findall('[0-9]', line)])
        risk_count = sum([
            check_adj(x, *get_adj_values(e_x, e_y, points))
            for e_y, y in enumerate(points) for e_x, x in enumerate(y)
        ])
        print(risk_count)


if __name__ == '__main__':
    main()


