#!/bin/python3

from globals import *
from getinput import read_input
from processfile import process_file
from processfunction import process_function
from processrun import process_run

import os
import sys

def process_command(command: str) -> bool or None:
    if command.startswith("@ "):
        process_file(command)
        return False
    if command.startswith("$ "):
        process_function(command)
        return False
    if command == "cls" or command == "clear" or command == "c":
        return nprint("\033[Hm\033[0J")
    if command == "leave" or command == "quit" or command == "q":
        return True
    if command == "run" or command == "test" or command == "r":
        process_run()
        return False
    warn("Command '{}' not found.".format(command))
    return False

def main_loop() -> int:
    while True:
        user_input = read_input()
        if user_input != False:
            print("\033[{}D".format(len(user_input) + 3), end=("" if not os.isatty(sys.stdin.fileno()) else "\n"))
            if (process_command(user_input)):
                break
            print(f"\033[10000D", end="")
        else:
            break
    return 0

if __name__ == "__main__":
    exit(main_loop())
