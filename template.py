import sys


def readlines(type=int):
    return list(map(type, sys.stdin.readline().split()))


def read(type=int):
    return type(sys.stdin.readline().strip())


joint = lambda it, sep=" ": sep.join(
    [str(i) if type(i) != list else sep.join(map(str, i)) for i in it])


def solve(inp):
    return 0


def main():
    read()
    print(solve())


if __name__ == "__main__":
    main()
