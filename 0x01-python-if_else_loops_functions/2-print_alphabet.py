#!/usr/bin/python3
def fullalpha():
    for letter in range(ord("a"), ord("z") + 1):
        print("{}".format(chr(letter)), end="")
