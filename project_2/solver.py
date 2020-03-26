import time
from typing import List, Tuple

from eval_function import EvalFunction
from Grid import Grid, vecIndex as MOVE_DIRS
from minimax import Minimax


class TimeLimitError(Exception):
    pass


class State:
    def __init__(self, grid: Grid, move: int = -1, depth: int = 0):
        self.depth = depth
        self.move = move
        self._grid = grid

    def get_grid(self):
        return self._grid

    def get_available_states(self) -> List['State']:
        return [State(grid, move, self.depth + 1) for grid, move in self._get_available_moves(self._grid)]

    @staticmethod
    def _get_available_moves(grid) -> List[Tuple[Grid, int]]:
        availableMoves = []

        for move in MOVE_DIRS:
            clone = grid.clone()
            if clone.move(move):
                availableMoves.append((clone, move))

        return availableMoves


class Solver:
    def __init__(self, grid: Grid, eval_func: EvalFunction, time_limit: float = 0.2):
        self._grid = grid
        self._eval_func = eval_func
        self._end_time = time.clock() + time_limit

    def get_move(self):
        depth = 4
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

    def _child_states(self, state: State) -> List[State]:
        return sorted(state.get_available_states(), key=self._eval)

    def _eval(self, state: State) -> float:
        return self._eval_func.calculate(state.get_grid())
