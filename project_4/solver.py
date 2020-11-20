from ac3_solver import AC3Solver
from board import Board
from bts_solver import BTSSolver
from csp_solver import CSP


class Solver:
    def __init__(self):
        self._csp = CSP(
            select_unassigned_variable=self._select_unassigned_variable,
            order_domain_values=self._order_domain_values,
            valid_inference=self._valid_inference
        )

    def solve(self, board):
        solver = AC3Solver()
        initial_board = Board.from_string(board)
        solved_board = solver.solve(initial_board, self._csp)
        if solved_board:
            return solved_board.to_string(), 'AC3'
        else:
            solver = BTSSolver()
            solved_board = solver.solve(initial_board, self._csp)
            return solved_board.to_string(), 'BTS'

    @staticmethod
    def _select_unassigned_variable(board):
        raise NotImplementedError()

    @staticmethod
    def _order_domain_values(var, board):
        raise NotImplementedError()

    @staticmethod
    def _valid_inference(var, value):
        raise NotImplementedError()
