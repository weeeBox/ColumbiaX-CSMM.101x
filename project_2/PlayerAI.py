from math import log2

from BaseAI import BaseAI
from eval_function import CompositeEvalFunction, EvalFunction
from Grid import Grid
from solver import Solver


class MaxTileEvalFunction(EvalFunction):
    def calculate(self, grid: Grid) -> float:
        return log2(grid.getMaxTile())


class AvailableCellsEvalFunction(EvalFunction):
    def calculate(self, grid: Grid) -> float:
        return len(grid.getAvailableCells())


class PlayerAI(BaseAI):
    def __init__(self):
        self._eval_func = CompositeEvalFunction()
        self._eval_func.register(1.0, MaxTileEvalFunction())
        self._eval_func.register(1.0, AvailableCellsEvalFunction())

    def getMove(self, grid):
        return Solver(grid, self._eval_func).get_move()
