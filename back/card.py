from dataclasses import dataclass


@dataclass
class Card:
    number: str
    shape: str
    color: str
    filling: str

    def to_str(self) -> str:
        return f"{self.number}{self.shape}{self.color}{self.filling}"

    def __repr__(self) -> str:
        return self.to_str()

