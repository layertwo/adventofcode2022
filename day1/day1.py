from dataclasses import dataclass, field
from typing import List


@dataclass
class Elf:
    items: List[int] = field(default_factory=list)

    @property
    def total_calories(self) -> int:
        return sum(self.items)


def get_elf_calories(filename: str) -> List[Elf]:
    """Get each set of items per elf"""
    output = []
    with open(filename) as fp:
        elf = Elf()
        for val in fp.read().splitlines():
            try:
                val = int(val)
                elf.items.append(val)
            except ValueError:
                elf = Elf()
                output.append(elf)
        output.append(elf)
    return output


def main():
    """Main"""
    filename = "puzzle_input.txt"
    elf_items = get_elf_calories(filename)
    total_cals = sorted([e.total_calories for e in elf_items], reverse=True)
    max_cals = max(total_cals)
    print(f"elf with the max total calories carried: {max_cals}")
    top_three = total_cals[0:3]
    print(f"elves with top 3 total calories {top_three}: {sum(top_three)}")


if __name__ == "__main__":
    main()
