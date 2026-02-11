import sys


def main():
    lines = [line.rstrip() for line in sys.stdin.readlines()]
    if "kth" in str(lines[0]):
        print("yes")
    else:
        print("no")


main()