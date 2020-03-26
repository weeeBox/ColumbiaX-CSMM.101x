from BaseAI import BaseAI
from solver import Solver


class PlayerAI(BaseAI):
    def getMove(self, grid):
        return Solver(grid).get_move()
