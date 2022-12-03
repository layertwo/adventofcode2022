from dataclasses import dataclass
from functools import cached_property
from string import ascii_letters
from typing import List

Item = str


@dataclass
class Rucksack:
    first: List[Item]
    second: List[Item]

    @classmethod
    def from_items(cls, items: str) -> "Rucksack":
        half_len = int(len(items) / 2)
        return cls(first=items[0:half_len], second=items[half_len:])

    @cached_property
    def common_item(self) -> Item:
        common = set(self.first) & set(self.second)
        return list(common)[0]

    @cached_property
    def common_item_val(self) -> str:
        return self._letter_val(self.common_item)

    def _letter_val(self, letter: str) -> int:
        return ascii_letters.find(letter) + 1


Rucksacks = List[Rucksack]


def get_rucksack_from_file(filename: str) -> List[Rucksack]:
    """Read rucksack data from file"""
    output = []
    with open(filename) as fp:
        for line in fp.read().splitlines():
            rucksack = Rucksack.from_items(items=list(line))
            output.append(rucksack)
    return output


def main():
    """Main"""
    # filename = "test_data.txt"
    filename = "puzzle_input.txt"
    rucksacks = get_rucksack_from_file(filename)
    total = sum(r.common_item_val for r in rucksacks)
    print(f"total for part one common item values: {total}")


if __name__ == "__main__":
    main()
