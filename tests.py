
set_game_1: Game = init_game()

# Test move_cards_from_pile_to_selection
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

# Test
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
