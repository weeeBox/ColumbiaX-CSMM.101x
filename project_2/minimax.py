class Minimax:
    def __init__(self, state, terminal_test, moves_func, eval_func):
        self._state = state
        self._terminal_test = terminal_test
        self._moves_func = moves_func
        self._eval_func = eval_func

    def decision(self):
        move, utility = self._solve(self._state, maximize=True)
        return move, utility

    def _solve(self, state, maximize):
        if self._terminal_test(state):
            return state, self._eval_func(state)

        best_move = None
        best_utility = float('-inf') if maximize else float('+inf')
        moves = self._moves_func(state)
        for move in moves:
            _, utility = self._solve(move, not maximize)
            if maximize and utility > best_utility or not maximize and utility < best_utility:
                best_utility = utility
                best_move = move

        return best_move, best_utility
