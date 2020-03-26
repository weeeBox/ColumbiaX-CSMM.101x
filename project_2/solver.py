import time
from math import log2
from typing import List, Tuple

from Grid import Grid, vecIndex as MOVE_DIRS
from minimax import Minimax


class TimeLimitError(Exception):
    pass


class State:
    def __init__(self, grid: Grid, move: int = -1, depth: int = 0):
        self.depth = depth
        self.move = move
        self._grid = grid
        self._score = self._calc_score(grid)

    def get_available_states(self) -> List['State']:
        children = [State(grid, move, self.depth + 1) for grid, move in self._get_available_moves(self._grid)]
        return sorted(children, key=lambda x: x.get_score())

    @staticmethod
    def _get_available_moves(grid) -> List[Tuple[Grid, int]]:
        availableMoves = []

        for move in MOVE_DIRS:
            clone = grid.clone()
            if clone.move(move):
                availableMoves.append((clone, move))

        return availableMoves

    def get_score(self):
        return self._score

    @staticmethod
    def _calc_score(grid) -> float:
        return log2(grid.getMaxTile()) + len(grid.getAvailableCells()) / 16


class Solver:
    def __init__(self, grid, time_limit=0.2):
        self._grid = grid
        self._end_time = time.clock() + time_limit

    def get_move(self):
        depth = 2
        best_child = self._run_minimax(depth)
        while True:
            try:
                depth += 1
                best_child = self._run_minimax(depth)
            except TimeLimitError:
                break

        return best_child.move

    def _run_minimax(self, max_depth) -> State:
        minimax = Minimax(State(self._grid),
                          terminal_test_func=self._create_terminal_test(max_depth),
                          child_states_func=self._child_states,
                          eval_func=self._eval)
        best_child, _ = minimax.decision()
        return best_child

    def _create_terminal_test(self, max_depth):
        end_time = self._end_time

        def terminal_test(state):
            if time.clock() >= end_time:
                raise TimeLimitError

            return state.depth >= max_depth

        return terminal_test

    @staticmethod
    def _child_states(state):
        return state.get_available_states()

    @staticmethod
    def _eval(state):
        return state.get_score()
