from unittest import TestCase

from driver import PriorityDict


class PriorityDictTest(TestCase):
    def test_min_pq(self):
        d = PriorityDict()

        d.insert(10, '10')
        self.assertEqual(1, len(d))
        self.assertTrue(d.contains('10'))
        self.assertEqual('10', d.peek())

        d.insert(5, '5')
        self.assertEqual(2, len(d))
        self.assertTrue(d.contains('5'))
        self.assertEqual('5', d.peek())

        d.insert(20, '20')
        self.assertEqual(3, len(d))
        self.assertTrue(d.contains('20'))
        self.assertEqual('5', d.peek())

        d.insert(15, '15')
        self.assertEqual(4, len(d))
        self.assertTrue(d.contains('15'))
        self.assertEqual('5', d.peek())

        d.insert(0, '0')
        self.assertEqual(5, len(d))
        self.assertTrue(d.contains('0'))
        self.assertEqual('0', d.peek())

        self.assertEqual('0', d.pop())
        self.assertEqual(4, len(d))
        self.assertFalse(d.contains('0'))
        self.assertEqual('5', d.peek())

        self.assertEqual('5', d.pop())
        self.assertEqual(3, len(d))
        self.assertFalse(d.contains('5'))
        self.assertEqual('10', d.peek())

        self.assertEqual('10', d.pop())
        self.assertEqual(2, len(d))
        self.assertFalse(d.contains('10'))
        self.assertEqual('15', d.peek())

        self.assertEqual('15', d.pop())
        self.assertEqual(1, len(d))
        self.assertFalse(d.contains('15'))
        self.assertEqual('20', d.peek())

        self.assertEqual('20', d.pop())
        self.assertEqual(0, len(d))
        self.assertFalse(d.contains('20'))

    def test_decrease_key(self):
        queue = PriorityDict()
        queue.insert(10, '10')
        queue.insert(20, '20')
        queue.insert(30, '30')
        queue.insert(40, '40')

        self.assertEqual('10', queue.peek())

        queue.decrease_key(5, '40')
        self.assertEqual('40', queue.peek())

        queue.decrease_key(4, '30')
        self.assertEqual('30', queue.peek())

        queue.decrease_key(3, '20')
        self.assertEqual('20', queue.peek())
