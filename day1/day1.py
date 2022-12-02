from dataclasses import dataclass
from typing import List


@dataclass
class ElfItems:
    calories: List[int]

    @property
    def total_calories(self) -> int:
        return sum(self.calories)


def get_elf_calories(filename: str) -> List[ElfItems]:
    """Get each set of items per elf"""
    output = []
    with open(filename) as fp:
        calories: List[int] = []
        for val in fp.read().splitlines():
            try:
                val = int(val)
                calories.append(val)
            except ValueError:
                elf = ElfItems(calories=calories)
                output.append(elf)
                calories = []
        elf = ElfItems(calories=calories)
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
