import unittest
from codes import task


class MyTestCase(unittest.TestCase):
    def test_merge_positive(self):
        self.assertEqual(list(task.merge([1, 5, 9], [2, 5], [1, 6, 10, 11])),
                         [1, 1, 2, 5, 5, 6, 9, 10, 11])
        self.assertEqual(list(task.merge([9, 8, 7], [3, 5, 4])), [3, 4, 5, 7, 8, 9])
        self.assertEqual(list(task.merge([-1, -2, -4, 1, 2], [-5, 0, 1])), [-5, -4, -2, -1, 0, 1, 1, 2])

    def test_merge_negative(self):
        self.assertNotEqual(list(task.merge([1, 5, 9], [2, 5], [1, 6, 10, 11])),
                            [1, 1, 2, 5, 5, 6, 9, 11, 10])
        self.assertNotEqual(list(task.merge([9, 8, 7], [3, 5, 4])), [9, 8, 7, 3, 5, 4])


if __name__ == '__main__':
    unittest.main()
