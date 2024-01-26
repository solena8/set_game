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

    def card_param_number(self, card1: Card, card2: Card, card3: Card) -> bool:
        if card1.number != card2.number and card1.number != card3.number and card1.number != card3.number:
            return True
        if card1.number == card2.number and card1.number == card3.number and card1.number == card3.number:
            return True
        else:
            return False

    def card_param_color(card1: Card, card2: Card, card3: Card) -> bool:
        if card1.color != card2.color and card1.color != card3.color and card2.color != card3.color:
            return True
        if card1.color == card2.color and card1.color == card3.color and card2.color == card3.color:
            return True
        else:
            return False

    def card_param_shape(card1: Card, card2: Card, card3: Card) -> bool:
        if card1.shape != card2.shape and card1.shape != card3.shape and card2.shape != card3.shape:
            return True
        if card1.shape == card2.shape and card1.shape == card3.shape and card2.shape == card3.shape:
            return True
        else:
            return False

    def card_param_filling(card1: Card, card2: Card, card3: Card) -> bool:
        if card1.filling != card2.filling and card1.filling != card3.filling and card2.filling != card3.filling:
            return True
        if card1.filling == card2.filling and card1.filling == card3.filling and card2.filling == card3.filling:
            return True
        else:
            return False


    def check_if_set_is_valid(card1: Card, card2: Card, card3: Card) -> bool:
        return (card_param_number(card1, card2, card3) and
                card_param_color(card1, card2, card3) and
                card_param_shape(card1, card2, card3) and
                card_param_filling(card1, card2, card3))


    def find_set(self) -> (Card, Card, Card):
        for card_1 in self.selection:
            for card_2 in self.selection:
                for card_3 in self.selection:
                    if card_1 != card_2 and card_2 != card_3 and card_1 != card_3:
                        if check_if_set_is_valid(card_1, card_2, card_3) == 1:
                            return (card1, card2, card3)

                    # print(card1, card2, card3)

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

### Test init_selection ###
set_game_3: Game = init_game()

assert len(set_game_3.selection) == 0
assert len(set_game_3.pile) == 81
set_game_3.init_selection()  # == Game.init_selection(set_game_3)
assert len(set_game_3.selection) == 12
assert len(set_game_3.pile) == 81 - 12









card_1: Card = Card(number="1", shape="L", color="R", filling="H")
card_2: Card = Card(number="3", shape="O", color="V", filling="P")
card_3: Card = Card(number="2", shape="R", color="M", filling="V")
card_4: Card = Card(number="2", shape="O", color="M", filling="V")
card_5: Card = Card(number="3", shape="V", color="R", filling="P")
card_6: Card = Card(number="1", shape="V", color="M", filling="P")

# assert card_param_number(card_1, card_3, card_4) == False
# assert card_param_number(card_1, card_4, card_5) == True
# assert card_param_shape(card_1, card_2, card_4) == False
# assert card_param_shape(card_1, card_4, card_5) == True
# assert card_param_color(card_1, card_2, card_5) == False
# assert card_param_color(card_2, card_4, card_5) == True
# assert card_param_filling(card_1, card_2, card_6) == False
# assert card_param_filling(card_1, card_2, card_3) == True

assert check_if_set_is_valid(card_1, card_2, card_3) == True
assert check_if_set_is_valid(card_1, card_2, card_4) == False
