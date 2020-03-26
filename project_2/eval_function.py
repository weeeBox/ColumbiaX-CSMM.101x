from typing import List, Tuple

from Grid import Grid


class EvalFunction:
    def calculate(self, grid: Grid) -> float:
        raise NotImplementedError


class CompositeEvalFunction(EvalFunction):
    def __init__(self):
        self._functions: List[Tuple[float, EvalFunction]] = []

    def register(self, weight: float, function: EvalFunction):
        self._functions.append((weight, function))

    def calculate(self, grid: Grid) -> float:
        score = 0
        for w, f in self._functions:
            score += w * f.calculate(grid) if w != 0 else 0

        return score
