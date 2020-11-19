import unittest

from driver import Driver


class MyTestCase(unittest.TestCase):
    def test_solution(self):
        with open('sudokus_start.txt', 'r') as f:
            initial_boards = f.read().splitlines()

        with open('sudokus_finish.txt', 'r') as f:
            for initial_board in initial_boards:
                expected_board, expected_solver = f.readline().split()
                actual_board, actual_solver = Driver().solve(initial_board)
                self.assertEqual(expected_board, actual_board)
                self.assertEqual(expected_solver, actual_solver)
