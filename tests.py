from game import Game
from selection import Selection
from card import Card

set_game_1 = Game()

assert len(set_game_1.pile) == 81

set_game_1.init_selection()
assert len(set_game_1.selection.selection_cards) == 12

set_game_1.add_3_cards()
assert len(set_game_1.pile) == 66
assert len(set_game_1.selection.selection_cards) == 15
assert len(set_game_1.set) == 0

set_game_1.add_3_cards()
assert len(set_game_1.pile) == 66
assert len(set_game_1.selection.selection_cards) == 15
assert len(set_game_1.set) == 0

assert Selection.check_if_set_is_valid(Card(number='3', shape='L', color='M', filling='P'),
                                       Card(number='3', shape='O', color='V', filling='V'),
                                       Card(number='3', shape='V', color='R', filling='H'))

set_game_1.find_set()
assert len(set_game_1.pile) == 66
assert len(set_game_1.selection.selection_cards) == 15
assert len(set_game_1.set) == 3

set_game_1.print_and_remove_from_selection()
assert len(set_game_1.pile) == 66
assert len(set_game_1.selection.selection_cards) == 12
assert len(set_game_1.set) == 3

assert not set_game_1.game_over()

set_game_1.pile = []
set_game_1.selection = Selection()

set_game_1.find_set()

assert set_game_1.game_over()
