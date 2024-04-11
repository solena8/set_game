from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from card import Card
from selection import Selection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/cards/{cards}")
def read_item(cards: str):
    l_cards = cards.split(",")
    selection_instance = Selection()
    for param in l_cards:
        card = Card(param[0], param[1], param[2], param[3])
        selection_instance.selection_cards.append(card)
    print(selection_instance)
    found_set = selection_instance.find_set()
    print(found_set)
    if found_set:
        return [found_set.card1.to_str(), found_set.card2.to_str(), found_set.card3.to_str()]
    return {"not found"}
