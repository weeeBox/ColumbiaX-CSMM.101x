from unittest import TestCase
from io import StringIO

from driver import search, write_to_output


class Test2(TestCase):
    def assert_result(self, result, path):
        with open(path, 'r') as f:
            expected = f.read()

        with StringIO('') as f:
            write_to_output(f, result)
            actual = f.getvalue()

        self.assertEqual(expected, actual)

    def test_dfs0(self):
        result = search('dfs', (6, 1, 8, 4, 0, 2, 7, 3, 5))
        with StringIO('') as f:
            write_to_output(f, result)
            actual = f.getvalue()

        self.assertEqual("f", actual)

    def test_bfs0(self):
        result = search('bfs', (6, 1, 8, 4, 0, 2, 7, 3, 5))
        self.assert_result(result, 'bfs0.txt')

    def test_bfs1(self):
        result = search('bfs', (8, 6, 4, 2, 1, 3, 5, 7, 0))
        self.assert_result(result, 'bfs1.txt')

    def test_ast1(self):
        result = search('ast', (8, 6, 4, 2, 1, 3, 5, 7, 0))
        self.assert_result(result, 'ast1.txt')
