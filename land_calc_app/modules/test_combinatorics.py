#standard
import unittest
import itertools
from collections import Counter
#this project
import combinatorics


class TestCombinatorics(unittest.TestCase):

    def test_dp_unique_combinations(self):
        deck = Counter({ "w": 5, "u": 5, "b": 5, "r": 5, "g": 5, "c": 5, "s": 5})

        comparison_deck = 5*["u", "g", "r", "b", "w", "c", "s"]

        def do_it_the_other_way(deck, cards_seen):
            return set([tuple(sorted(pair)) for pair in itertools.combinations(comparison_deck, cards_seen)])

        for x in range(1, 7):
            ours = combinatorics.dp_unique_combinations(deck, x)
            other_way = do_it_the_other_way(comparison_deck, x)

            self.assertEqual(len(ours), len(other_way))


if __name__ == "__main__":
    unittest.main(verbosity=3)