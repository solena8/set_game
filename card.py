from dataclasses import dataclass


@dataclass
class Card:
    number: str
    shape: str
    color: str
    filling: str

    def __repr__(self) -> str:
        return f"{self.number}{self.shape}{self.color}{self.filling}"
