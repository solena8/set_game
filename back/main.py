from typing import List

from game import Game
from selection import Selection

# set_game_1 = Game()
# set_game_1.game_play()

def my_api(params: List[str]) -> List[str]:
    # params: input (from front) = full selection
    # output -> Set
    params = ["1ORH", "2VVP", "3ORV"]

    selection_instance = Selection()
    for param in params:
        card = Card(param)
        selection_instance.selection_cards.append(card)
    selection_instance.find_set()

