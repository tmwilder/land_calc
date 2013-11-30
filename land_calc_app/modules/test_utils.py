#standard
import unittest
from collections import Counter
#this project
import utils


class TesTUtils(unittest.TestCase):
    def test_hash_counter(self):
        counter = Counter({"w":1, "u":1})
        self.assertEqual(utils.hash_counter(counter), "u1w1")

        counter_2 = Counter({"w":10, "s":5})
        self.assertEqual(utils.hash_counter(counter_2), "s5w10")


if __name__ == "__main__":
    unittest.main(verbosity=3)
