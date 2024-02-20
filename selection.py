from dataclasses import dataclass, field
from card import Card


@dataclass
class Selection:
    selection_cards: list[Card] = field(default_factory=list)

    def len_selection(self) -> int:
        return len(self.selection_cards)

        # définition des règles de matching pour les 4 méthodes ci dessous :
        # chacun des 4 types de paramètre (nombre, couleur, forme et remplissage)
        # doit avoir 3 occurences complètement identiques (1, 1, 1 par ex.)
        # ou 3 occurences complètements différentes (1, 2, 3 par ex.)

    @staticmethod
    def card_param_number(card1: Card, card2: Card, card3: Card) -> bool:
        return (card1.number == card2.number == card3.number) or (
                card1.number != card2.number != card3.number != card1.number)

    @staticmethod
    def card_param_color(card1: Card, card2: Card, card3: Card) -> bool:
        return (card1.color == card2.color == card3.color) or (card1.color != card2.color != card3.color != card1.color)

    @staticmethod
    def card_param_shape(card1: Card, card2: Card, card3: Card) -> bool:
        return (card1.shape == card2.shape == card3.shape) or (card1.shape != card2.shape != card3.shape != card1.shape)

    @staticmethod
    def card_param_filling(card1: Card, card2: Card, card3: Card) -> bool:
        return (card1.filling == card2.filling == card3.filling) or (
                card1.filling != card2.filling != card3.filling != card1.filling)

    @staticmethod
    def check_if_set_is_valid(card1: Card, card2: Card, card3: Card) -> bool:
        # vérification des 4 types de paramètres pour 3 cartes
        return (Selection.card_param_number(card1, card2, card3) and
                Selection.card_param_color(card1, card2, card3) and
                Selection.card_param_shape(card1, card2, card3) and
                Selection.card_param_filling(card1, card2, card3))
