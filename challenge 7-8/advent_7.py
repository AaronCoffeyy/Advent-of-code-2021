import collections


class Board:
    def __init__(self, board):
        self.board = board

    def check_win(self):
        # horizontal
        for i in self.board:
            if collections.Counter(i)['M'] and collections.Counter(i)['M'] == 5:
                return True
        for i in range(5):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.board[3][i] == self.board[4][i] == 'M':
                return True
        return False

    def mark_board(self, value):
        for iter_one, i in enumerate(self.board):
            for iter_two, j in enumerate(i):
                if j == value:
                    self.board[iter_one][iter_two] = 'M'

    def sum_unmarked(self):
        sum_result = 0
        for i in self.board:
            sum_result += sum([int(x) for x in i if x != 'M'])
        return sum_result


def remove_blank(array):
    return [x for x in array if x != '']


def create_board_array(start, end, step, array):
    list_of_boards = []
    for i in range(start, end, step):
        board = [remove_blank(x.split(' ')) for x in array[i:i + 5]]
        list_of_boards.append(Board(board))
    return list_of_boards


def get_final_score(sum_of_unmarked, winning_value):
    print(sum_of_unmarked, winning_value)
    return sum_of_unmarked * winning_value


def diff_between_arrays(array_1, array_2):
    return [x for x in array_1 if x not in array_2]


def board_win_remover(board_array, bingo_number):
    winning_boards = []
    for board_num, board in enumerate(board_array):
        board.mark_board(bingo_number)
        if board.check_win():
            winning_boards.append(board)
            if len(board_array) - len(winning_boards) == 0:
                print(get_final_score(board.sum_unmarked(), int(bingo_number)))
    return diff_between_arrays(board_array, winning_boards)


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        bingo_nums = lines[0].split(',')
        boards_with_no_wins = create_board_array(2, len(lines[2:]), 6, lines)
        for num in bingo_nums:
            boards_with_no_wins = board_win_remover(boards_with_no_wins, num)


if __name__ == '__main__':
    main()

#ans = 2817661

