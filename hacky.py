import sys
from typing import Annotated


tree = {}


def main():
    lines = [line.rstrip() for line in sys.stdin.readlines()]

    num_lines = int(lines[0])

    strings = lines[1:]

    print(num_lines)
    print(strings)

    for string in strings:
        for c in string:
            if tree[c] is None:
                c


main()
