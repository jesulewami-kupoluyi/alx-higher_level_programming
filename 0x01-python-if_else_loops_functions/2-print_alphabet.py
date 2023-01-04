#!/usr/bin/python3
def alpha():
    for letter in range(ord("a"), ord("z") + 1):
        print(f"{chr(letter)}".format(chr(letter)), end="")
alpha()
