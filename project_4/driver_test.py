import unittest

from board import Board
from driver import Solver
from solver import BoardCSP


class DriverTest(unittest.TestCase):
    def test_csp(self):
        board = Board.from_string(
            '000260701'
            '680070090'
            '190004500'
            '820100040'
            '004602900'
            '050003028'
            '009300074'
            '040050036'
            '703018000'
        )

        csp = BoardCSP(board)


    def test_solution(self):
        with open('sudokus_start.txt', 'r') as f:
            initial_boards = f.read().splitlines()

        with open('sudokus_finish.txt', 'r') as f:
            for initial_board in initial_boards:
                expected_board, expected_solver = f.readline().split()
                actual_board, actual_solver = Solver().solve(initial_board)
                self.assertEqual(expected_board, actual_board)
                self.assertEqual(expected_solver, actual_solver)
