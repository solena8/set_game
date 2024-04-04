from dataclasses import dataclass
from typing import Optional

from card import Card
from set import Set


@dataclass
class Selection:
    selection_cards: list[Card]

    def __init__(self):
        self.selection_cards = []

    def len_selection(self) -> int:
        return len(self.selection_cards)

        # définition des règles de matching pour les 4 méthodes ci dessous :
        # chacun des 4 types de paramètre (nombre, couleur, forme et remplissage)
        # doit avoir 3 occurences complètement identiques (1, 1, 1 par ex.)
        # ou 3 occurences complètements différentes (1, 2, 3 par ex.)

    def find_set(self) -> Optional[Set]:
        # Trouver un set de 3 cartes dans la sélection
        for card_1 in self.selection_cards:
            for card_2 in self.selection_cards:
                for card_3 in self.selection_cards:
                    if card_1 != card_2 and card_2 != card_3 and card_1 != card_3:
                        search_set = Set(card1=card_1, card2=card_2, card3=card_3)
                        if search_set.check_if_set_is_valid():
                            return search_set
        return None
