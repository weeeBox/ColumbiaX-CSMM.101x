from itertools import permutations
from unittest import TestCase

from minimax import Minimax


class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []

    def index(self, child):
        return self.children.index(child)

    @classmethod
    def from_list(cls, values, branch_factor=2):
        if len(values) % branch_factor != 0:
            raise ValueError(f"Invalid string: {values}")

        k = len(values) // branch_factor
        root = Node()
        if k == 1:
            for val in values:
                root.children.append(Node(val))
        else:
            for i in range(branch_factor):
                root.children.append(cls.from_list(values[i * k: (i + 1) * k]))

        return root

    def add(self, *values):
        nodes = []
        for val in values:
            node = Node(val)
            self.children.append(node)
            nodes.append(node)

        return nodes

    def is_leaf(self):
        return len(self.children) == 0

    def __repr__(self):
        if self.is_leaf():
            return str(self.val)

        return f"[{','.join(child.__repr__() for child in self.children)}]"


def terminal_test(node):
    return node.is_leaf()


def moves(node):
    return node.children


def eval(node):
    return node.val


def create_minimax(node, terminal_test_func=None, moves_func=None, eval_func=None):
    return Minimax(state=node,
                   terminal_test=terminal_test_func or terminal_test,
                   moves_func=moves_func or moves,
                   eval_func=eval_func or eval)


class Test(TestCase):
    def test_decision1(self):
        self._test_decision(child_index=1, utility=2, values=[1, 2], branch_factor=2)
        self._test_decision(child_index=0, utility=2, values=[2, 1], branch_factor=2)

    def test_decision2(self):
        """
           3
         1   3
        1 2 3 4
        """
        self._test_decision(child_index=1, utility=3, values=[1, 2, 3, 4], branch_factor=2)

        """
           2
         2   1
        4 2 3 1 
        """
        self._test_decision(child_index=0, utility=2, values=[4, 2, 3, 1], branch_factor=2)

    def test_decision3(self):
        """
           4
        1 2 3 4
        """
        self._test_decision(child_index=3, utility=4, values=[1, 2, 3, 4], branch_factor=4)

        """
           4
        1 4 2 3
        """
        self._test_decision(child_index=1, utility=4, values=[1, 4, 2, 3], branch_factor=4)

    def test_decision4(self):
        """
                 6             max
            2         6        min
         2    4    6    8      max
        1 2  3 4  5 6  7 8     min
        """
        self._test_decision(child_index=1, utility=6, values=[1, 2, 3, 4, 5, 6, 7, 8], branch_factor=2)

    def test_decision5(self):
        """
                 7             max
            3         7        min
         3    4    8    7      max
        1 3  2 4  5 8  7 6     min
        """
        self._test_decision(child_index=1, utility=7, values=[1, 3, 2, 4, 5, 8, 7, 6], branch_factor=2)

    def test_pruning1(self):
        """
                 3             max
            1         3        min
         1    2    3    4      max
        """
        self._test_pruning(expected=[1, 2, 3, 4], values=[1, 2, 3, 4], branch_factor=2)

    def test_pruning2(self):
        """
                 3             max
            3         1        min
         4    3    2    1      max
        """
        self._test_pruning(expected=[4, 3, 2], values=[4, 3, 2, 1], branch_factor=2)

    def test_pruning3(self):
        """
                      4                 max
                 2         4            min
            2         4         6       max
         1    2    3    4    5    6     min
        """
        self._test_pruning(expected=[1, 2, 3, 4, 5, 6], values=[1, 2, 3, 4, 5, 6], branch_factor=3)

    def test_pruning4(self):
        """
                      4                 max
                 4         2            min
            6         4         2       max
         6    5    4    3    2    1     min
        """
        self._test_pruning(expected=[6, 5, 4, 2], values=[6, 5, 4, 3, 2, 1], branch_factor=3)

    def _test_decision(self, child_index, utility, values, branch_factor):
        state = Node.from_list(values, branch_factor)
        minimax = create_minimax(state)
        actual_child, actual_utility = minimax.decision()
        self.assertEqual(utility, actual_utility)
        self.assertEqual(state.children[child_index], actual_child)

    def _test_pruning(self, expected, values, branch_factor):
        evaluated_states = []

        def eval_func(state):
            ans = eval(state)
            evaluated_states.append(ans)
            return ans

        state = Node.from_list(values, branch_factor=branch_factor)
        minimax = create_minimax(state, eval_func=eval_func)
        minimax.decision()
        self.assertEqual(expected, evaluated_states)
