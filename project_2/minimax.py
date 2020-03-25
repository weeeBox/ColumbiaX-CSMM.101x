from math import inf


class Minimax:
    def __init__(self, state, terminal_test, moves_func, eval_func):
        self._state = state
        self._terminal_test = terminal_test
        self._moves_func = moves_func
        self._eval_func = eval_func

    def decision(self):
        move, utility = self._solve(self._state, maximize=True, alpha=-inf, beta=inf)
        return move, utility

    def _solve(self, state, maximize, alpha, beta):
        if self._terminal_test(state):
            return state, self._eval_func(state)

        best_move = None
        moves = self._moves_func(state)
        if maximize:
            best_utility = -inf
            for move in moves:
                _, utility = self._solve(move, False, alpha, beta)
                if utility > best_utility:
                    best_utility = utility
                    best_move = move

                if utility > beta:
                    break

                alpha = max(alpha, utility)
        else:
            best_utility = inf
            for move in moves:
                _, utility = self._solve(move, True, alpha, beta)
                if utility < best_utility:
                    best_utility = utility
                    best_move = move

                if utility < alpha:
                    break

                beta = min(beta, utility)

        return best_move, best_utility
