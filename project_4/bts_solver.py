import copy

from csp_solver import CSPSolver


class BTSSolver(CSPSolver):
    def solve(self, board, csp):
        tmp = copy.copy(board)
        return self._backtrack(tmp, csp)

    def _backtrack(self, board, csp):
        if board.is_complete():
            return board

        var = csp.select_unassigned_variable(board)
        for value in csp.order_domain_values(var, board):
            board[var] = value
            if csp.valid_inference(var, value):
                result = self._backtrack(board, csp)
                if result:
                    return result
            board.clear(var)

        return None
