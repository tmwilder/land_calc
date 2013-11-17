#standard
from math import factorial as fact
#local
import combinatorics


def get_odds_range(end_turn, deck, card_cost, on_the_play=True):
    """
    Gets the odds of being able to cast a given card by a given turn.

    end_turn: Turn by which we want to cast the card.
    deck: collections.Counter with keys 'u' 'g' 'r' 'b' 'w' for mana colors,
          and 'c', 's' for colorless and spell respectively.
    card_cost: Counter describing the cost of the card to be cast. Same format as deck.
    on_the_play: True | False. Describes whether you're on the play or not.

    """
    all_odds = []
    for index, turns in enumerate(range(1, end_turn + 1)):
        odds = _get_one_turn_odds(turns, deck, card_cost, on_the_play)
        all_odds.append((index, odds))
    return all_odds


def _get_one_turn_odds(turns, deck, card_cost, on_the_play=True):
    cards_seen = _cards_seen(deck=deck, turns=turns, on_the_play=on_the_play)

    unique_combos = combinatorics.dp_unique_combinations(deck=deck, cards_seen=cards_seen)

    valid_unique_combos = _get_valid_combinations(card_cost=card_cost, cards_lists=unique_combos)

    total_odds = 0.0

    for combination in valid_unique_combos:
        total_odds += _multivariate_hyper_geometric(deck=deck, exact_cards=combination)

    return total_odds


def _multivariate_hyper_geometric(deck, exact_cards):
    """
    Gets the odds of drawing a particular hand from a deck when drawing cards equal to the hands length.

    deck: deck Counter.
    exact_cards: Card cobination Counter.

    """
    numerator_terms = []
    for card_type, card_number in exact_cards.items():
        deck_number = deck[card_type]
        if card_number > deck_number:
            return 0.0
        term = _n_choose_k(deck_number, card_number)
        numerator_terms.append(term)
    total = 1.0
    for term in numerator_terms:
        total *= term
    total /= _n_choose_k(sum(deck.values()), sum(exact_cards.values()))
    return total


def _n_choose_k(n, k):
    """ Gets combination count when choosing k cards from a deck of n cards. """
    return float(fact(n)) / (float(fact(n - k)) * fact(k))


def _get_valid_combinations(card_cost, cards_lists):
    """
    Takes a list of card Counters and a cost Counter, returns a list containing
    the counters that contain lands sufficient to cast the card described by card
    cost.

    """
    valid_uniques = []
    for combination in cards_lists:
        enough_lands = _has_enough_lands(combination, card_cost)
        if enough_lands:
            has_colors = _has_right_colors(combination, card_cost)
            if has_colors:
                valid_uniques.append(combination)
    return valid_uniques


def _has_enough_lands(cards, card_cost):
    mana_keys = set(["w", "u", "b", "r", "g", "c"])
    total_mana = 0
    for card in cards:
        if card in mana_keys:
            total_mana += cards[card]

    colorless_cost = sum(card_cost.values())
    if total_mana >= colorless_cost:
        return True
    else:
        return False


def _has_right_colors(cards, mana_cost):
    colored_mana_keys = set(["w", "u", "b", "r", "g"])
    for color, number in mana_cost.items():
        if (color in colored_mana_keys) and (cards[color] < number):
            return False
    return True


def _cards_seen(deck, turns, on_the_play=True):
    total = 6 + turns
    if on_the_play is False:
        total += 1
    if total > sum(deck.values()):
        total = sum(deck.values())
    return total
