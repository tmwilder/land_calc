#standard
import unittest
from collections import Counter
#land calc
import can_cast


class TestCanCast(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.bribery = Counter({"u": 2, "c": 3})
        cls.cromat = Counter({"w": 1, "u": 1, "b": 1, "r": 1, "g": 1})

    def test_can_cast(self):
        cards = Counter({"ub": 1, "ur":1, "ug": 1, "uw":1, "c": 1})

        self.assertEqual(can_cast.can_cast(self.bribery, cards), True)
        self.assertEqual(can_cast.can_cast(self.bribery, self.cromat), False)
        self.assertEqual(can_cast.can_cast(self.cromat, self.cromat), True)
        self.assertEqual(can_cast.can_cast(self.cromat, cards), False)
        self.assertEqual(can_cast.can_cast(self.cromat, Counter({})), False)

    def test_enough_mana(self):
        cards = Counter({"u":1 , "b": 1})
        self.assertEqual(can_cast._enough_mana(self.bribery, cards), False)
        cards_2 = Counter({"u":5})
        self.assertEqual(can_cast._enough_mana(self.bribery, cards_2), True)

    def test_lands_that_can_provide_color(self):
        cards = Counter({"rg": 1, "wg": 1, "ug": 1, "ru": 1, "r": 1})
        self.assertEqual(can_cast._lands_that_can_provide_color("r", cards), ["ru", "rg", "r"])

    def test_get_relevant_cards(self):
        cards = Counter({"g": 5, "wu": 1, "ub": 1, "ur": 1})
        relevant_cards = can_cast._get_relevant_cards(spell_cost=self.bribery,
                                                      cards=cards)
        self.assertEqual(relevant_cards, Counter({'c': 5, 'wu': 1, 'ub': 1, 'ur': 1, 'g': 0}))
        self.assertEqual(can_cast._get_relevant_cards(self.cromat, self.cromat), self.cromat)
        self.assertEqual(can_cast._get_relevant_cards(self.bribery, self.bribery), self.bribery)


    def test_reduce_problem(self):
        pass


if __name__ == "__main__":
    unittest.main()