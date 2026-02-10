#!/usr/bin/env python3


def add_one(param):
    param += 1


def main():
    my_variable = 42
    print(my_variable)
    add_one(my_variable)
    print(my_variable)


if __name__ == "__main__":
    main()
