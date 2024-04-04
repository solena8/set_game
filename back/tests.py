from card import Card
from game import Game
from selection import Selection
from set import Set

set_game_1 = Game()

assert len(set_game_1.pile) == 81

set_game_1.init_selection()
assert len(set_game_1.selection.selection_cards) == 12

set_game_1.add_3_cards()
assert len(set_game_1.pile) == 66
assert len(set_game_1.selection.selection_cards) == 15


set_game_1.add_3_cards()
assert len(set_game_1.pile) == 66
assert len(set_game_1.selection.selection_cards) == 15


# Create instances of Card with the desired parameters
card1 = Card(number='3', shape='L', color='M', filling='P')
card2 = Card(number='3', shape='O', color='V', filling='V')
card3 = Card(number='3', shape='V', color='R', filling='H')

# Create an instance of Set and pass the cards to the method
set_instance = Set(card1=card1, card2=card2, card3=card3)

# Assert that the set is valid
assert set_instance.check_if_set_is_valid()

set_game_1.selection.find_set()
assert len(set_game_1.pile) == 66
assert len(set_game_1.selection.selection_cards) == 15
# assert len(set_game_1.set) == 3

set_game_1.print_and_remove_from_selection()
assert len(set_game_1.pile) == 66
assert len(set_game_1.selection.selection_cards) == 12
# assert len(set_game_1.set) == 3

assert not set_game_1.game_over()

set_game_1.pile = []
set_game_1.selection = Selection()

set_game_1.selection.find_set()

assert set_game_1.game_over()
