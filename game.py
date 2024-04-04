from dataclasses import dataclass
import random
from typing import Optional

from card import Card
from selection import Selection
from set import Set


@dataclass
class Game:
    pile: list[Card]
    selection: Selection  # "Selection()" create the object from the class
    opt_set: Optional[Set]

    def __init__(self):
        self.pile = []
        self.selection = Selection()
        self.opt_set = None

        # création de la pile de 81 cartes différentes
        for number in ["1", "2", "3"]:
            for shape in ["L", "O", "V"]:
                for color in ["V", "M", "R"]:
                    for filling in ["H", "P", "V"]:
                        self.pile.append(Card(number=number, shape=shape, color=color, filling=filling))

    def len_pile(self) -> int:
        return len(self.pile)

    def move_cards_from_pile_to_selection(self, nb_cards: int) -> None:
        # extraction d'un nb de cartes définit de la pile, de manière aléatoire
        # et ajout à la sélection
        random_selection = random.sample(self.pile, nb_cards)
        for card in random_selection:
            self.selection.selection_cards.append(card)
            self.pile.remove(card)

    def init_selection(self):
        # création de la sélection initiale de 12 cartes à partir de la pile
        self.move_cards_from_pile_to_selection(12)

    def add_3_cards(self):
        # ajout de 3 cartes de la pile vers la selection si 1)il reste des cartes dans la pile
        # et 2) si la selection comporte 9 cartes, ou 12 mais sans avoir trouvé de match avant
        # (comme ça lorsqu'on a atteint 15 cartes et trouvé ensuite un match, on redescend à 12 après)
        if (self.len_pile() >= 3) and ((self.selection.len_selection() == 12 and not self.opt_set) or
                                       (self.selection.len_selection() == 9)):
            self.move_cards_from_pile_to_selection(3)

    def print_and_remove_from_selection(self):
        # enlever les cartes du set trouvé précédemment de la sélection
        print(self.opt_set)
        self.selection.selection_cards.remove(self.opt_set.card1)
        self.selection.selection_cards.remove(self.opt_set.card2)
        self.selection.selection_cards.remove(self.opt_set.card3)

    def game_over(self) -> bool:
        # définition du game over : si on a pas trouvé de set à la dernière recherche et que
        # soit la pile est vide
        # soit la sélection comportait déja 15 cartes (on ne veut pas avoir une sélection de 18 cartes)
        return not self.opt_set and (
                self.selection.len_selection() > 15 or self.len_pile() < 3)

    def game_play(self):
        self.init_selection()
        while not self.game_over():
            self.opt_set = self.selection.find_set()
            if self.opt_set:
                self.print_and_remove_from_selection()
            self.add_3_cards()
        print("No more matches found.")
        print("Remaining cards are:", self.selection.selection_cards, self.pile)
        print(len(self.selection.selection_cards), "+", len(self.pile), "cards left")
