import re


def get_adj_valid_adj_coords(center_pos_x, center_pos_y, array):
    coords = []
    if center_pos_y >= 1 and array[center_pos_y - 1][center_pos_x] == 0:
        coords.append([center_pos_y - 1, center_pos_x])
    if center_pos_y < len(array) - 1 and array[center_pos_y + 1][center_pos_x] == 0:
        coords.append([center_pos_y + 1, center_pos_x])
    if center_pos_x >= 1 and array[center_pos_y][center_pos_x - 1] == 0:
        coords.append([center_pos_y, center_pos_x - 1])
    if center_pos_x < len(array[center_pos_y]) - 1 and array[center_pos_y][center_pos_x + 1] == 0:
        coords.append([center_pos_y, center_pos_x + 1])
    return coords


def large_basin_checker(x, y, array, counter):
    if array[y][x] == 0:
        counter += 1
        array[y][x] = 2
    for coord in get_adj_valid_adj_coords(x, y, array):
        counter = large_basin_checker(x=coord[1], y=coord[0], array=array, counter=counter)
    return counter


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        points = []
        for line in lines:
            points.append([1 if int(i) == 9 else 0 for i in re.findall('[0-9]', line)])
        basins_array = []
        basins_array.extend([
            large_basin_checker(x=e_x, y=e_y, array=points, counter=0)
            for e_y, y in enumerate(points) for e_x, x in enumerate(y)
        ])
        basins_array = sorted(basins_array, reverse=True)
        print(basins_array[0] * basins_array[1] * basins_array[2])


if __name__ == '__main__':
    main()
