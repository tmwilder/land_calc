#standard
import collections
import copy
#this project
import utils


def dp_unique_combinations(deck, cards_seen):
    """
    Uses dynamic programming to get all unique combinations of cards.

    deck: counter representing an mtg deck.
          Keys are w u b r g for lands, c for colorless lands, s for spells.
    cards_seen: Number of cards to get combinations for.

    """
    unique_combos = []
    hashed_unique_combos = set()
    visited_states = set()

    def recursion(deck, cards, cards_seen):
        if sum(cards.values()) == cards_seen:
            hashed = utils.hash_counter(cards)
            if hashed not in hashed_unique_combos:
                unique_combos.append(cards)
                hashed_unique_combos.add(hashed)
            return
        elif len(deck.keys()) == 0:
            return

        for key in deck:
            #Add one card for each different remaining card in the deck.
            if deck[key] == 0:
                continue
            new_cards = copy.deepcopy(cards)
            new_deck = copy.deepcopy(deck)
            new_cards[key] += 1
            new_deck[key] -= 1
            hashed = utils.hash_counter(new_cards)
            if hashed not in visited_states:
                visited_states.add(hashed)
                recursion(new_deck, new_cards, cards_seen)

    #Used to represent one combination of cards.
    cards = collections.Counter()
    recursion(deck, cards, cards_seen=cards_seen)

    return unique_combos
