from math import inf


class Minimax:
    def __init__(self, state, terminal_test_func, child_states_func, eval_func):
        self._state = state
        self._terminal_test_func = terminal_test_func
        self._child_states_func = child_states_func
        self._eval_func = eval_func

    def decision(self):
        move, utility = self._solve(self._state, maximize=True, alpha=-inf, beta=inf)
        return move, utility

    def _solve(self, state, maximize, alpha, beta):
        if self._terminal_test_func(state):
            return state, self._eval_func(state)

        best_child = None
        child_states = self._child_states_func(state)
        if maximize:
            best_utility = -inf
            for child in child_states:
                _, utility = self._solve(child, False, alpha, beta)
                if utility > best_utility:
                    best_utility = utility
                    best_child = child

                if utility >= beta:
                    break

                alpha = max(alpha, utility)
        else:
            best_utility = inf
            for child in child_states:
                _, utility = self._solve(child, True, alpha, beta)
                if utility < best_utility:
                    best_utility = utility
                    best_child = child

                if utility <= alpha:
                    break

                beta = min(beta, utility)

        return best_child, best_utility
