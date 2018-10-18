import unittest
from rubylike import ri

class TestRi(unittest.TestCase):
    def test_ri(self):
        self.assertEqual(ri([1,2,3]).first(), 1)
        self.assertEqual(ri([1,2,3,4,5]).len(), 5)
        self.assertEqual(ri([1,2,3]).take(2).to_a(), [1,2])
        self.assertEqual(ri([1,2,3]).drop(2).to_a(), [3])
        self.assertEqual(ri([1,2,3]).map(lambda x: x * 10).to_a(), [10, 20, 30])
        self.assertEqual(ri([1,2,3]).filter(lambda x: x < 3).to_a(), [1,2])

        each_result = []
        self.assertEqual(ri([1,2,3]).each(lambda x: each_result.append(x)), None)
        self.assertEqual(each_result, [1,2,3])

        self.assertEqual(ri([1,3,2]).max(), 3)
        self.assertEqual(ri([1,3,2]).min(), 1)

        tuples = [(1,9), (2, 8), (3, 7)]
        self.assertEqual(ri(tuples).max_by(lambda t: t[1]), (1, 9))
        self.assertEqual(ri(tuples).min_by(lambda t: t[0]), (1, 9))

        self.assertEqual(ri([3,2,1]).sort().to_a(), [1,2,3])
        self.assertEqual(ri(tuples).sort_by(lambda t: t[1]).to_a(), list(reversed(tuples)))

        self.assertEqual(ri(['a', 'b', 'c']).reverse().to_a(), ['c', 'b', 'a'])

        original = ['a', 'b', 'c']
        shuffled = ri(original).shuffle().to_a()
        self.assertEqual(sorted(shuffled), sorted(original))

        original = ['a', 'b', 'c', 'd', 'e']
        self.assertIn(ri(original).sample(), original)
        self.assertIn(ri(original).sample(1).first(), original)
        for sampled in ri(original).sample(3):
            self.assertIn(sampled, original)

        self.assertTrue(ri([True, True, True]).all())
        self.assertTrue(ri([1,2,3]).all(lambda x: x < 5))
        self.assertTrue(ri([True, False, True]).any())
        self.assertTrue(ri([1,2,3]).any(lambda x: x > 2))

if __name__ == '__main__':
    unittest.main()