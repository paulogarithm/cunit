import sys
import tty
import termios
import os

from colors import c

def replace_text(text) -> str:
    text = text.replace("@", "@ ")
    text = text.replace("$", "$ ")
    return text

def replace_color(text) -> str:
    text = "\033[m" + text
    text = text.replace("@ ", "\033[m\033[95m@ \033[4;94m")
    text = text.replace("$ ", "\033[m\033[38;5;205m$ \033[m")
    text = text.replace("?", "\033[m\033[1m?\033[m")
    text = text.replace("==", "{}{}=={}".format(c.r, c.red, c.r))
    return text


def input_loop():
    input_str = ""
    tty.setraw(sys.stdin.fileno())
    sys.stdout.write(f"\033[{len(input_str) + 3}D\033[K\033[m> ")
    sys.stdout.flush()
    while True:
        ch = sys.stdin.read(1)
        if ch == '\r' or ch == '\n':
            break
        elif ch == '[':
            sys.stdin.read(2)
            continue
        elif ch == '\t':
            continue
        elif ch == '\x03':
            return False
        elif ch == '\x7f':
            if len(input_str) > 0:
                input_str = input_str[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()
        else:
            input_str += replace_text(ch)
            sys.stdout.write(f"\033[{len(input_str) + 3}D\033[K\033[m> ")
            sys.stdout.write(replace_color(input_str))
            sys.stdout.flush()
    sys.stdout.write("\033[m")
    return input_str
    

def read_input():
    if not os.isatty(sys.stdin.fileno()):
        line = sys.stdin.readline()
        if (len(line) == 0):
            return False
        line = line[:-1] if line[-1] == '\n' else line
        return line

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    input_str = ""

    try:
        input_str = input_loop()
        if input_str == False:
            return False
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return input_str
