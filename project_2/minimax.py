from math import inf


class Minimax:
    def __init__(self, state, terminal_test_func, child_states_func, eval_func):
        self._state = state
        self._terminal_test_func = terminal_test_func
        self._child_states_func = child_states_func
        self._eval_func = eval_func

    def decision(self):
        return self._maximize(self._state, a=-inf, b=inf)

    def _minimize(self, state, a, b):
        if self._terminal_test_func(state):
            return None, self._eval_func(state)

        min_child, min_utility = None, inf
        for child in self._child_states_func(state):
            _, utility = self._maximize(child, a, b)
            if utility < min_utility:
                min_child, min_utility = child, utility

            if min_utility <= a:
                break

            if min_utility < b:
                b = min_utility

        return min_child, min_utility

    def _maximize(self, state, a, b):
        if self._terminal_test_func(state):
            return None, self._eval_func(state)

        max_child, max_utility = None, -inf
        for child in self._child_states_func(state):
            _, utility = self._minimize(child, a, b)
            if utility > max_utility:
                max_child, max_utility = child, utility

            if max_utility >= b:
                break

            if max_utility > a:
                a = max_utility

        return max_child, max_utility
