from ac3_solver import AC3Solver
from board import Board
from bts_solver import BTSSolver
from csp_solver import CSP

DOMAIN = list('123456789')


class BoardCSP(CSP):
    def __init__(self, board):
        self.variables = {key: set(DOMAIN if board.is_empty(key) else [board[key]]) for key in board.keys()}

    def select_unassigned_variable(self, board):
        raise NotImplementedError('Implement in a subclass')

    def valid_inference(self, var, value):
        raise NotImplementedError('Implement in a subclass')

    def order_domain_values(self, var, board):
        raise NotImplementedError('Implement in a subclass')


class Solver:
    def solve(self, board):
        csp = BoardCSP()
        solver = AC3Solver()
        initial_board = Board.from_string(board)
        solved_board = solver.solve(initial_board, csp)
        if solved_board:
            return solved_board.to_string(), 'AC3'
        else:
            solver = BTSSolver()
            solved_board = solver.solve(initial_board, csp)
            return solved_board.to_string(), 'BTS'
