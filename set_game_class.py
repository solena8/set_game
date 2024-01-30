# This is a comment to test commit
from dataclasses import dataclass
import random


@dataclass
class Card:
    number: str
    shape: str
    color: str
    filling: str


@dataclass
class Game:
    pile: list[Card]
    selection: list[Card]
    set: list[Card]

    def number_of_cards(self) -> int:
        return len(self.pile)

    def move_cards_from_pile_to_selection(self, nb_cards: int):
        random_selection = random.sample(self.pile, nb_cards)
        for card in random_selection:
            self.selection.append(card)
            self.pile.remove(card)

    def init_selection(self):
        self.move_cards_from_pile_to_selection(12)

    def fill_selection(self):
        self.move_cards_from_pile_to_selection(3)

    def card_param_number(self, card1: Card, card2: Card, card3: Card) -> bool:
        if card1.number != card2.number and card1.number != card3.number and card1.number != card3.number:
            return True
        if card1.number == card2.number and card1.number == card3.number and card1.number == card3.number:
            return True
        else:
            return False

    def card_param_color(self, card1: Card, card2: Card, card3: Card) -> bool:
        if card1.color != card2.color and card1.color != card3.color and card2.color != card3.color:
            return True
        if card1.color == card2.color and card1.color == card3.color and card2.color == card3.color:
            return True
        else:
            return False

    def card_param_shape(self, card1: Card, card2: Card, card3: Card) -> bool:
        if card1.shape != card2.shape and card1.shape != card3.shape and card2.shape != card3.shape:
            return True
        if card1.shape == card2.shape and card1.shape == card3.shape and card2.shape == card3.shape:
            return True
        else:
            return False

    def card_param_filling(self, card1: Card, card2: Card, card3: Card) -> bool:
        if card1.filling != card2.filling and card1.filling != card3.filling and card2.filling != card3.filling:
            return True
        if card1.filling == card2.filling and card1.filling == card3.filling and card2.filling == card3.filling:
            return True
        else:
            return False


    def check_if_set_is_valid(self, card1: Card, card2: Card, card3: Card) -> bool:
        return (self.card_param_number(card1, card2, card3) and
                self.card_param_color(card1, card2, card3) and
                self.card_param_shape(card1, card2, card3) and
                self.card_param_filling(card1, card2, card3))


    def find_set(self) -> (Card, Card, Card):
        found_set_list = []
        for card_1 in self.selection:
            for card_2 in self.selection:
                for card_3 in self.selection:
                    if card_1 != card_2 and card_2 != card_3 and card_1 != card_3:
                        if self.check_if_set_is_valid(card_1, card_2, card_3) == 1:
                            found_set_list.append([card_1, card_2, card_3])
                            self.set = [item for sublist in found_set_list for item in sublist]
                            return self.set

    def remove_cards_from_selection_and_set(self):
        for card in list(self.set):
            self.set.remove(card)
            self.selection.remove(card)


# A faire :
# remove set from selection

def init_game() -> Game:
    # Create all_cards
    all_cards = []
    for number in ["1", "2", "3"]:
        for shape in ["L", "O", "V"]:
            for color in ["V", "M", "R"]:
                for filling in ["H", "P", "V"]:
                    all_cards.append(Card(number=number, shape=shape, color=color, filling=filling))
    # Init a new Game object with all cards
    game = Game(pile=all_cards, selection=[], set=[])
    # Return the new Game
    return game


set_game_1: Game = init_game()

### Test move_cards_from_pile_to_selection ###
assert len(set_game_1.pile) == 81
assert len(set_game_1.selection) == 0

set_game_1.move_cards_from_pile_to_selection(1)
assert len(set_game_1.pile) == 80
assert len(set_game_1.selection) == 1

set_game_2: Game = init_game()
assert len(set_game_2.pile) == 81
assert len(set_game_2.selection) == 0
set_game_2.move_cards_from_pile_to_selection(5)
assert len(set_game_2.pile) == 76
assert len(set_game_2.selection) == 5

### Test ###

set_game_4: Game = init_game()
set_game_4.init_selection()
set_game_4.find_set()
assert len(set_game_4.pile) == 69
assert len(set_game_4.set) == 3
assert len(set_game_4.selection) == 12
print(set_game_4.find_set())

set_game_4.remove_cards_from_selection_and_set()
assert len(set_game_4.selection) == 9
assert len(set_game_4.set) == 0
print("this should be empty:", set_game_4.set)

set_game_4.fill_selection()
assert len(set_game_4.pile) == 66
assert len(set_game_4.selection) == 12
assert len(set_game_4.set) == 0








