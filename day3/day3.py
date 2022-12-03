from dataclasses import dataclass
from functools import cache, cached_property
from string import ascii_letters
from typing import List

from more_itertools import grouper

Item = str


@dataclass(frozen=True)
class Rucksack:
    """Elf Rucksack containing items"""

    items: List[Item]

    @property
    def half_len(self) -> int:
        return len(self.items) // 2

    @cached_property
    def first(self) -> List[Item]:
        return self.items[0 : self.half_len]

    @cached_property
    def second(self) -> List[Item]:
        return self.items[self.half_len :]

    @cached_property
    def common_item(self) -> Item:
        common = set(self.first) & set(self.second)
        return list(common)[0]

    @cached_property
    def common_item_val(self) -> int:
        return letter_score(self.common_item)


Rucksacks = List[Rucksack]
Group = Rucksacks
Groups = List[Rucksacks]


@cache
def letter_score(letter: str) -> int:
    """Calculate score based on index in ascii letters"""
    return ascii_letters.find(letter) + 1


def get_rucksack_from_file(filename: str) -> List[Rucksack]:
    """Read rucksack data from file"""
    output = []
    with open(filename) as fp:
        for line in fp.read().splitlines():
            rucksack = Rucksack(items=list(line))
            output.append(rucksack)
    return output


def make_elf_groups(rucksacks: Rucksacks, group_size: int = 3) -> Groups:
    return list(grouper(rucksacks, n=group_size))


def calculate_group_badge_val(group: Group) -> int:
    """Calculate badge between 3 group elves"""
    x, y, z = group
    common = set(x.items) & set(y.items) & set(z.items)
    letter = list(common)[0]
    return letter_score(letter)


def main():
    """Main"""
    # filename = "test_data.txt"
    filename = "puzzle_input.txt"
    rucksacks = get_rucksack_from_file(filename)
    total = sum(r.common_item_val for r in rucksacks)
    print(f"total for part one common item values: {total}")
    total2 = sum(calculate_group_badge_val(g) for g in make_elf_groups(rucksacks))
    print(f"total for part two sum of group badges: {total2}")


if __name__ == "__main__":
    main()
