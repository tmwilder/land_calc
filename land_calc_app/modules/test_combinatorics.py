#standard
import unittest
import itertools
from collections import Counter
#land calc
import combinatorics


class TestCombinatorics(unittest.TestCase):

    def test_dp_unique_combinations(self):
        deck = Counter({ "w": 5, "u": 5, "b": 5, "r": 5, "g": 5, "c": 5, "s": 5})

        comparison_deck = 5*["u", "g", "r", "b", "w", "c", "s"]

        def do_it_the_other_way(deck, cards_seen):
            return set([tuple(sorted(pair)) for pair in itertools.combinations(comparison_deck, cards_seen)])

        for x in range(1, 6):
            ours = combinatorics.dp_unique_combinations(deck, x)
            other_way = do_it_the_other_way(comparison_deck, x)
            self.assertEqual(len(ours), len(other_way))


    def test_hash_counter(self):
        counter = Counter({"w":1, "u":1})
        self.assertEqual(combinatorics._hash_counter(counter), "u1w1")

        counter_2 = Counter({"w":10, "s":5})
        self.assertEqual(combinatorics._hash_counter(counter_2), "s5w10")


if __name__ == "__main__":
    unittest.main(verbosity=3)