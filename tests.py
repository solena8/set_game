from game import Game
from game import Card

set_game_1 = Game()

assert len(set_game_1.pile) == 81

# set_game_1.move_cards_from_pile_to_selection(10)
# assert len(set_game_1.pile) == 71

set_game_1.init_selection()
assert len(set_game_1.selection) == 12

set_game_1.add_3_cards()
assert len(set_game_1.pile) == 66
assert len(set_game_1.selection) == 15
assert len(set_game_1.set) == 0

set_game_1.add_3_cards()
assert len(set_game_1.pile) == 66
assert len(set_game_1.selection) == 15
assert len(set_game_1.set) == 0

assert set_game_1.check_if_set_is_valid(Card(number='3', shape='L', color='M', filling='P'),
                                        Card(number='3', shape='O', color='V', filling='V'),
                                        Card(number='3', shape='V', color='R', filling='H')) == 1

set_game_1.find_set()
assert len(set_game_1.pile) == 66
assert len(set_game_1.selection) == 15
assert len(set_game_1.set) == 3

set_game_1.print_and_remove_from_selection()
assert len(set_game_1.pile) == 66
assert len(set_game_1.selection) == 12
assert len(set_game_1.set) == 3

assert set_game_1.game_over() == 0

set_game_1.pile = []
set_game_1.selection = []

set_game_1.find_set()

assert set_game_1.game_over() == 1
