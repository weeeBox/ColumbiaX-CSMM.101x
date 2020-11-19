import sys

from ac3_solver import AC3Solver
from bts_solver import BTSSolver


class Driver:
    def solve(self, initial_board):
        solver = AC3Solver()
        solved_board = solver.solve(initial_board)
        if solved_board:
            return solved_board, 'AC3'
        else:
            solver = BTSSolver()
            solved_board = solver.solve(initial_board)
            return solved_board, 'BTS'


def write_solution(board, solver):
    assert board
    with open('output.txt', 'w') as f:
        f.write('{board} {solver}'.format(board=board, solver=solver))


if __name__ == '__main__':
    initial_board = sys.argv[1]
    solved_board, solver = Driver().solve(initial_board)
    write_solution(solved_board, solver)
