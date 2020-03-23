from unittest import TestCase

from project_1.driver import search


class Test(TestCase):
    def test_dfs1(self):
        result = search('bfs', (6, 1, 8, 4, 0, 2, 7, 3, 5))
        self.assertEqual(['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up'], result.path)
        self.assertEqual(20, result.cost_of_path)
        self.assertEqual(54094, result.nodes_expanded)
        self.assertEqual(20, result.search_depth)
        self.assertEqual(21, result.max_search_depth)

    def test_dfs2(self):
        result = search('bfs', (8, 6, 4, 2, 1, 3, 5, 7, 0))
        self.assertEqual(['Left', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Left', 'Up', 'Left'], result.path)
        self.assertEqual(26, result.cost_of_path)
        self.assertEqual(166786, result.nodes_expanded)
        self.assertEqual(26, result.search_depth)
        self.assertEqual(27, result.max_search_depth)