from dataclasses import dataclass, field
import random

from card import Card
from selection import Selection


@dataclass
class Game:
    pile: list[Card] = field(default_factory=list)
    selection: Selection = field(default_factory=Selection)
    set: list[Card] = field(default_factory=list)

    def __post_init__(self):
        for number in ["1", "2", "3"]:
            for shape in ["L", "O", "V"]:
                for color in ["V", "M", "R"]:
                    for filling in ["H", "P", "V"]:
                        self.pile.append(Card(number=number, shape=shape, color=color, filling=filling))

        # création de la pile de 81 cartes différentes
        # Return the new Game

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
        if (self.len_pile() >= 3) and ((self.selection.len_selection() == 12 and not self.set) or
                                       (self.selection.len_selection() == 9)):
            self.move_cards_from_pile_to_selection(3)

    def find_set(self) -> list[Card]:
        # Trouver un set de 3 cartes dans la sélection
        self.set = []
        for card_1 in self.selection.selection_cards:
            for card_2 in self.selection.selection_cards:
                for card_3 in self.selection.selection_cards:
                    if card_1 != card_2 and card_2 != card_3 and card_1 != card_3:
                        if Selection.check_if_set_is_valid(card_1, card_2, card_3):
                            self.set = [card_1, card_2, card_3]
                            return self.set

    def print_and_remove_from_selection(self):
        # enlever les cartes du set trouvé précédemment de la sélection
        print(self.set)
        for card in self.set:
            self.selection.selection_cards.remove(card)

    def game_over(self):
        # définition du game over : si on a pas trouvé de set à la dernière recherche et que
        # soit la pile est vide
        # soit la sélection comportait déja 15 cartes (on ne veut pas avoir une sélection de 18 cartes)
        return not self.find_set() and (
                    self.selection.len_selection() >= 15 or self.len_pile() < 3)

    def game_play(self):
        self.init_selection()
        while not self.game_over():
            self.find_set()
            if self.set:
                self.print_and_remove_from_selection()
            self.add_3_cards()
        print("No more matches found.")
        print("Remaining cards are:", self.selection.selection_cards, self.pile)
        print(len(self.selection.selection_cards), "+", len(self.pile), "cards left")
