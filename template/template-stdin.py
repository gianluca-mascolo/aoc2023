#!/usr/bin/env python3
import sys


def main():
    while line := sys.stdin.readline():
        line = line.rstrip()
        print(line)


if __name__ == "__main__":
    main()
