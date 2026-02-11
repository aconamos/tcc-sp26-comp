import sys


def main():
    lines = [line.rstrip() for line in sys.stdin.readlines()]
    totoroSize = int(lines[0].split(" ")[1])
    acorns = [int(x) for x in lines[1].split(" ")]
    acorns.sort()
    sortedAcorns = [[],[],[],[]]
    for acorn in acorns:
        sortedAcorns[acorn%4].append(acorn)

    while(len(sortedAcorns[totoroSize%4])>0):
        totoroSize += sortedAcorns[totoroSize%4].pop()
    print(totoroSize)

main()