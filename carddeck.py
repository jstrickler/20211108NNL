import random


class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return f"{self.rank}-{self.suit}"

    def __repr__(self):  # representation Card('2', 'Diamonds')
        return f"Card('{self.rank}','{self.suit}')"

class CardDeck:   # inherits from 'object' by default
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        self.dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []  # list of cards
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    @property
    def cards(self):
        return self._cards


    @property
    def dealer(self):  # "getter" property
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):  # "setter" property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            bad_type = type(dealer).__name__
            message = f"Dealer must be str, not {bad_type}"
            raise TypeError(message)

    def __len__(self):
        return len(self._cards)

    def __str__(self):  # human friendly representation
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}: {self.dealer}, {len(self)} cards"

    def __repr__(self):
        my_name = type(self).__name__
        return f"{my_name}('{self.dealer}')"

class JokerDeck(CardDeck):  # inherit from CardDeck
    def _make_deck(self):
        super()._make_deck()  # call parent method
        for joker_number in '1', '2':
            c = Card(joker_number, 'JOKER')
            self._cards.append(c)


