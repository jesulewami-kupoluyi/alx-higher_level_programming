#!/usr/bin/python3
def fullalpha():
    for letter in range(ord("a"), ord("z") + 1):
        if chr(letter) != "q" and chr(letter) != "e":
            print("{}".format(chr(letter)), end="")
