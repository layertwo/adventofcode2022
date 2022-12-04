import csv
from dataclasses import dataclass
from functools import cache
from typing import List, Set


@dataclass(frozen=True)
class Pairing:
    """Elf pairing"""

    first: Set[int]
    second: Set[int]

    @property
    def has_full_overlap(self) -> bool:
        """If each set is a subset of the other"""
        return self.first.issubset(self.second) or self.second.issubset(self.first)

    @property
    def has_partial_overlap(self) -> bool:
        """If each set contains at least 1 common value"""
        return len(self.first & self.second) > 0


@cache
def parse_range(val: str) -> Set[int]:
    """Calculate range from X-Y format"""
    start, end = val.split("-")
    return set(range(int(start), int(end) + 1))


def get_pairings_from_file(filename: str) -> List[Pairing]:
    """Read pairings from file"""
    output = []
    with open(filename) as fp:
        for line in csv.reader(fp):
            pairing = Pairing(first=parse_range(line[0]), second=parse_range(line[1]))
            output.append(pairing)
    return output


def main():
    """Main"""
    # filename = "test_data.txt"
    filename = "puzzle_input.txt"
    pairings = get_pairings_from_file(filename)
    overlap1 = len([p for p in pairings if p.has_full_overlap])
    print(f"number of full overlaps in pairings: {overlap1}")
    overlap2 = len([p for p in pairings if p.has_partial_overlap])
    print(f"number of partial overlaps in pairings: {overlap2}")


if __name__ == "__main__":
    main()
