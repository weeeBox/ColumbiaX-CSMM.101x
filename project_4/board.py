class Board(object):
    def __init__(self, variables):
        self._variables = variables

    def __getitem__(self, item):
        return self._variables[item]

    def __setitem__(self, key, value):
        self._variables[key] = value

    def __copy__(self):
        return Board(self._variables.copy())

    def keys(self):
        return self._variables.keys()

    def is_complete(self):
        for key in self._variables:
            if self._variables[key] == '0':
                return False

        return True

    def is_empty(self, key):
        return self[key] == '0'

    def clear(self, key):
        self[key] = '0'

    @staticmethod
    def from_string(value):
        variables = {}
        idx = 0
        for r in 'ABCDEFGHI':
            for c in '123456789':
                variables[r + c] = value[idx]
                idx += 1

        return Board(variables)

    def to_string(self):
        idx = 0
        values = []
        for r in 'ABCDEFGHI':
            for c in '123456789':
                values.append(self[r + c])
                idx += 1

        return ''.join(values)
