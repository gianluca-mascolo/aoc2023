#!/usr/bin/env python3
def main():
    with open("input", "r") as reader:
        line = reader.readline()
        while line != "":  # The EOF char is an empty string
            line = line.rstrip()
            print(line)
            line = reader.readline()


if __name__ == "__main__":
    main()
