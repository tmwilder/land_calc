#standard
import copy
from collections import Counter
#this project
import utils


def can_cast(spell_cost, cards):
    """
    Determines if a set of cards are capable of casting a spell.

    spell_cost: Counter with keys for mana types.
        Valid keys - ['w', 'u', 'b', 'r', 'g', 'c']
    cards: Counter with keys for land types, and s for irrelevant spells.
        Valid keys - ['w', 'u', 'b', 'r', 'g', 'c', "wu", "wb", "wr" ...]

    """
    cards = _get_relevant_cards(spell_cost, cards)
    spell_cost, cards = _reduce_problem(spell_cost, cards)
    visited_states = set()

    def recursion(cost, cards):
        if sum(cost.values()) == 0:
            return True
        elif not _enough_mana(cost, cards):
            return False

        for color in cost:
            for land_type in _lands_that_can_provide_color(color, cards):
                if cards[land_type] == 0 or cost[color] == 0:
                    continue
                new_cost = copy.deepcopy(cost)
                new_cards = copy.deepcopy(cards)
                new_cost[color] -= 1
                new_cards[land_type] -= 1
                hashed = utils.hash_counter(new_cards)
                if hashed not in visited_states:
                    visited_states.add(hashed)
                    if recursion(new_cost, new_cards) is True:
                        return True

    if recursion(spell_cost, cards) is True:
        return True
    else:
        return False


def _lands_that_can_provide_color(color, cards):
    if color != "c":
        return [land for land in cards if color in land]
    else:
        return cards.keys()


def _enough_mana(spell_cost, cards):
    if sum(spell_cost.values()) > sum(cards.values()):
        return False
    return True


def _get_relevant_cards(spell_cost, cards):
    """ Converts cards whose colored mana is irrelevant to colorless mana sources. """
    cards = copy.deepcopy(cards)
    relevant_mana_colors = set(''.join(spell_cost.keys()))
    for land_type in cards.keys():
        relevant = False
        for mana_color in land_type:
            if mana_color in relevant_mana_colors:
                relevant = True
        if relevant is not True:
            cards["c"] += cards[land_type]
            cards[land_type] = 0
    return cards


def _reduce_problem(spell_cost, cards):
    """
    Performs operations on the cards/spell cost pair to remove automatic steps,
    I.E. using colorless mana to provide the colorless cost.

    """
    #TODO provide optimizations.    
    return spell_cost, cards
