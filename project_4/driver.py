import sys

from board import Board
from solver import Solver


def write_solution(board, solver):
    assert board
    with open('output.txt', 'w') as f:
        f.write('{board} {solver}'.format(board=board, solver=solver))


if __name__ == '__main__':
    initial_board = Board.from_string(sys.argv[1])
    solved_board, solver = Solver().solve(initial_board)
    result = solved_board.to_string()
    write_solution(result, solver)
