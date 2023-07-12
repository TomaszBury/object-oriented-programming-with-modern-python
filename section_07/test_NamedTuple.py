import collections

Card = collections.namedtuple('Card', ['rank', 'suit', 'value'])
suits = "spades clubs hearts diamonds".split()

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    cards = [Card(rank, suit, value) for value, rank in enumerate(ranks) for suit in suits]

print(FrenchDeck.cards)
