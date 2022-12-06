from typing import List


def find_marker_from_code(code: str, start=4) -> int:
    """Calculate marker from a code, starting at x"""
    val = 0
    for idx, _ in enumerate(code, start=start):
        marker = set(code[idx - start : idx])
        if len(marker) == start:
            val = idx
            break
    return val


def read_code_from_file(filename: str) -> List[str]:
    """Read lines from file"""
    output = []
    with open(filename) as fp:
        for code in fp.read().splitlines():
            output.append(code)
    return output


def main():
    """Main"""
    filename = "test_data.txt"
    filename = "puzzle_input.txt"
    codes = read_code_from_file(filename)
    print(f"part 1 characters processed {find_marker_from_code(codes[0])}")
    print(f"part 2 characters processed {find_marker_from_code(codes[0], start=14)}")


if __name__ == "__main__":
    main()
