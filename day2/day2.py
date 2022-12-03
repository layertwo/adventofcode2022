from dataclasses import dataclass
from enum import IntEnum
from functools import cache
from typing import Dict, List, Tuple


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(IntEnum):
    LOSE = 0
    TIE = 3
    WIN = 6


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
def get_shape(key: str) -> Shape:
    """Get the matching shape for a given key"""
    return SHAPE_MAP[key]


@cache
def get_outcome(key: str) -> Outcome:
    """Get the matching outcome for a given key"""
    return OUTCOME_MAP[key]


@dataclass
class Game:
    """Rock, Paper, Scissors game object"""

    left: Shape
    right: Shape
    outcome: Outcome

    @classmethod
    def from_part_1(cls, left: Shape, right: Shape) -> "Game":
        """Calculate game by left and right shapes"""
        outcome = cls._calculate_outcome(left=left, right=right)
        return cls(left=left, right=right, outcome=outcome)

    @classmethod
    def from_part_2(cls, left: Shape, outcome: Outcome) -> "Game":
        """Calculate game by left shape and outcome"""
        right = cls._calculate_shape(shape=left, outcome=outcome)
        return cls(left=left, right=right, outcome=outcome)

    @property
    def score(self) -> int:
        """Calculate the score right and outcome values"""
        return self.right.value + self.outcome.value

    @staticmethod
    @cache
    def _calculate_outcome(left: Shape, right: Shape) -> Outcome:
        """Given left and right shapes, what is the outcome"""
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

    @staticmethod
    @cache
    def _calculate_shape(shape: Shape, outcome: Outcome) -> Shape:
        """Given a shape, what is the outcome"""
        if shape == Shape.ROCK:
            if outcome == Outcome.WIN:
                return Shape.PAPER
            if outcome == Outcome.LOSE:
                return Shape.SCISSORS
        if shape == Shape.PAPER:
            if outcome == Outcome.WIN:
                return Shape.SCISSORS
            if outcome == Outcome.LOSE:
                return Shape.ROCK
        if shape == Shape.SCISSORS:
            if outcome == Outcome.WIN:
                return Shape.ROCK
            if outcome == Outcome.LOSE:
                return Shape.PAPER
        # for a tie, return the same shape
        return shape


Games = List[Game]
ValueSet = Tuple[str, str]
Values = List[ValueSet]


def get_games_from_file(filename: str) -> Values:
    """Read values from file and convert to tuple"""
    output = []
    with open(filename) as fp:
        for line in fp.read().splitlines():
            if line:
                left, right = line.split()
                output.append((left, right))
    return output


def load_games_part_1(game_data: Values) -> Games:
    """Read game data and use values to define Game object"""
    games = []
    for data in game_data:
        game = Game.from_part_1(left=get_shape(data[0]), right=get_shape(data[1]))
        games.append(game)
    return games


def load_games_part_2(game_data: Values) -> Games:
    """Read game data and use values to define Game object"""
    games = []
    for data in game_data:
        game = Game.from_part_2(left=get_shape(data[0]), outcome=get_outcome(data[1]))
        games.append(game)
    return games


def main():
    """Main"""
    filename = "puzzle_input.txt"
    game_data = get_games_from_file(filename)
    scores1 = [g.score for g in load_games_part_1(game_data)]
    print(f"total scores for all {len(scores1)} games: {sum(scores1)}")
    scores2 = [g.score for g in load_games_part_2(game_data)]
    print(f"total scores for all {len(scores2)} games: {sum(scores2)}")


if __name__ == "__main__":
    main()
