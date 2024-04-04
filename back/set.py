from dataclasses import dataclass
from card import Card


@dataclass
class Set:
    card1: Card
    card2: Card
    card3: Card

    def is_valid(self, param) -> bool:
        value1 = getattr(self.card1, param)
        value2 = getattr(self.card2, param)
        value3 = getattr(self.card3, param)
        return (value1 == value2 == value3) or ((value1 != value2) and (value2 != value3) and (value1 != value3))

    def card_param_number(self) -> bool:
        # return self.is_valid(Card.number)
        return self.is_valid('number')

    def card_param_color(self) -> bool:
        # return self.is_valid(Card.color)
        return self.is_valid('color')

    def card_param_shape(self) -> bool:
        # return self.is_valid(Card.shape)
        return self.is_valid('shape')

    def card_param_filling(self) -> bool:
        # return self.is_valid(Card.filling)
        return self.is_valid('filling')

    def check_if_set_is_valid(self) -> bool:
        # vérification des 4 types de paramètres pour 3 cartes
        return (self.card_param_number() and
                self.card_param_color() and
                self.card_param_shape() and
                self.card_param_filling())
