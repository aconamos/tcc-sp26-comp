import sys


def main():
    lines = [line.rstrip() for line in sys.stdin.readlines()]

    number = int(lines[0])
    if number == 0:
        print("-1 1")
        return

    a = number // 2
    if number == -1:
        print("-2 1")
        return
    elif number == 1:
        print("2 -1")
        return
    if (a + a) == number:
        print(f"{a} {a}")
    else:
        print(f"{a} {a + 1}")


main()
