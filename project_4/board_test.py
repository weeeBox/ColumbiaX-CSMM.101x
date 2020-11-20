from unittest import TestCase

from board import Board


class BoardTest(TestCase):
    def test_getter_setter(self):
        values = '000000000' \
                 '302540000' \
                 '050301070' \
                 '000000004' \
                 '409006005' \
                 '023054790' \
                 '000000050' \
                 '700810000' \
                 '080060009'
        board = Board.from_string(values)
        self.assertEqual('3', board['B1'])

        board['B1'] = '5'
        self.assertEqual('5', board['B1'])

    def test_serialization(self):
        expected = '000000000302540000050301070000000004409006005023054790000000050700810000080060009'
        board = Board.from_string(expected)
        actual = board.to_string()
        self.assertEqual(expected, actual)

    def test_complete(self):
        values = '148697523372548961956321478567983214419276385823154796691432857735819642284765139'
        board = Board.from_string(values)
        self.assertTrue(board.is_complete())

    def test_incomplete(self):
        values = '000000000302540000050301070000000004409006005023054790000000050700810000080060009'
        board = Board.from_string(values)
        self.assertFalse(board.is_complete())
