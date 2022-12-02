from dataclasses import dataclass
from enum import IntEnum
from functools import cache
from typing import Dict, List, Optional, Set


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(IntEnum):
    LOSE = 0
    TIE = 3
    WIN = 6


@dataclass
class Game:
    left: Shape
    right: Optional[Shape]

    @property
    def outcome(self) -> Outcome:
        return calculate_outcome(self.left, self.right)

    @property
    def score(self) -> int:
        return self.right.value + self.outcome.value


Games = List[Game]


SHAPE_MAP: Dict[str, Shape] = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS,
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSORS,
}


OUTCOME_MAP: Dict[str, Outcome] = {
    "X": Outcome.LOSE,
    "Y": Outcome.TIE,
    "Z": Outcome.WIN,
}


@cache
def get_shape(key):
    return SHAPE_MAP[key]


@cache
def calculate_outcome(left, right) -> Outcome:
    if left == Shape.ROCK:
        if right == Shape.PAPER:
            return Outcome.WIN
        if right == Shape.SCISSORS:
            return Outcome.LOSE
    if left == Shape.PAPER:
        if right == Shape.SCISSORS:
            return Outcome.WIN
        if right == Shape.ROCK:
            return Outcome.LOSE
    if left == Shape.SCISSORS:
        if right == Shape.ROCK:
            return Outcome.WIN
        if right == Shape.PAPER:
            return Outcome.LOSE
    return Outcome.TIE


def get_games_from_file(filename) -> List[Set]:
    output = []
    with open(filename) as fp:
        for line in fp.read().splitlines():
            if line:
                left, right = line.split()
                output.append((left, right))
    return output


def load_games_part_1(game_data) -> Games:
    games = []
    for data in game_data:
        left = get_shape(data[0])
        right = get_shape(data[1])
        games.append(Game(left=left, right=right))
    return games


def main():
    """Main"""
    filename = "puzzle_input.txt"
    game_data = get_games_from_file(filename)
    games1 = load_games_part_1(game_data)
    scores = [g.score for g in games1]
    print(f"total scores for all {len(scores)} games: {sum(scores)}")


if __name__ == "__main__":
    main()
