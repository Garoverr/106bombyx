#!/usr/bin/env python3

import sys

def bombyx(n, args):
    if len(args) == 1:
        try:
            k = float(args[0])
            for i in range(1, 101):
                print(f"{i} {n:.2f}")
                n = k * n * (1000 - n) / 1000
        except ValueError:
            return 84

    elif len(args) == 2:
        try:
            i0 = int(args[0])
            i1 = int(args[1])
            if i0 < 1 or i0 > i1:
                raise ValueError
            rate = 1.0
            while rate < 4:
                bound = 1
                result = float(n)
                while bound < i0:
                    result = rate * result * ((1000 - result) / 1000)
                    bound += 1

                while bound <= i1:
                    print(f"{rate:.2f} {result:.2f}")
                    result = rate * result * ((1000 - result) / 1000)
                    bound += 1

                rate += 0.01
        except ValueError:
            return 84

    else:
        return 84

    return 0

def usage() -> int:
    print("""USAGE
./106bombyx n [k | i0 i1]
DESCRIPTION
    n number of first generation individuals
    k growth rate from 1 to 4
    i0 initial generation (included)
    i1 final generation (included)""")
    return 0


def main() -> int:
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        args = [sys.argv[2]]
        return bombyx(n, args)

    elif len(sys.argv) == 4:
        n = int(sys.argv[1])
        args = [sys.argv[2], sys.argv[3]]
        return bombyx(n, args)

    else:
        return usage()


if __name__ == "__main__":
    sys.exit(main())
