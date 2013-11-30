#standard
import unittest
from collections import Counter
#this project
import density


class TestDensity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deck_1 = Counter({"u": 60})
        cls.deck_2 = Counter({"g": 10, "w": 10, "s": 20})
        cls.exact_cards = Counter({"u": 20, "s": 40})
        cls.cost_1 = Counter({"u": 1, "b": 1, "r": 1, "g": 1, "w": 1, "c": 3})

    def test_get_odds_range(self):
        end_turn = 10
        deck = self.deck_2
        card_cost = Counter({"g":2, "w":1, "c":2})
        density.get_odds_range(end_turn=end_turn, deck=deck, card_cost=card_cost)

    def test_get_one_turn_odds(self):
        result = density._get_one_turn_odds(turns=1, deck=self.deck_1, card_cost=Counter({"u": 1}))
        self.assertEqual(result, 1.0)

        result_2 = density._get_one_turn_odds(turns=1, deck=self.deck_1, card_cost=Counter({"u": 8}))
        self.assertEqual(result_2, 0.0)

        result_3 = density._get_one_turn_odds(turns=1, deck=self.deck_2, card_cost=Counter({"g":1, "w":1}))
        self.assertTrue(.77 < result_3 < .79)


    def test_multivariate_hyper_geometric(self):
        result = density._multivariate_hyper_geometric(
            deck=self.deck_1,
            exact_cards=Counter({"u": 50})
        )
        expected_result = 1.0
        self.assertEqual(result, expected_result)

        result_2 = density._multivariate_hyper_geometric(
            deck=self.deck_2,
            exact_cards=Counter({"g": 1})
        )
        self.assertTrue(.24 < result_2 < .26)

    def test_n_choose_k(self):
        self.assertEqual(density._n_choose_k(10, 1), 10.0)
        self.assertEqual(density._n_choose_k(5, 2), 10.0)
        self.assertEqual(density._n_choose_k(6, 3), 20)

    def test_get_valid_combinations(self):
        uniques = [
            Counter({"u": 2, "c":1}),
            Counter({"u": 1}),
            Counter({"g": 1, "r": 1}),
            Counter({"g": 20})
        ]
        result = density._get_valid_combinations(
            card_cost=Counter({"u": 1}),
            cards_lists=uniques
        )
        expected_result = [Counter({'u': 2, 'c': 1}), Counter({'u': 1})]
        self.assertEqual(result, expected_result)

    def test_cards_seen(self):
        result = density._cards_seen(deck=self.deck_1, turns=2, on_the_play=True)
        expected_result = 8
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
