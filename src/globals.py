from subprocess import run, PIPE
from os.path import realpath, dirname
from sys import stdin
from os import isatty
from colors import c

my_files = []
my_tests = []

p_this = realpath(__file__)
p_playground = realpath(f"{p_this}/../../playground/")
p_root = p_this
for i in range(3):
    p_root = dirname(p_root)
p_cfile = realpath("{}/a.c".format(p_playground))

class Types:
    unknown = -1
    int = 1
    float = 2
    char = 3
    string = 4

class Test:
    def __init__(self, a: list[str], b: list[str], c: str) -> None:
        self.func = a
        self.args = b
        self.res = c
    func: list[2:str]
    args: list[str]
    res: str

def toint(message: str) -> int or False:
    try: return int(message)
    except ValueError:
        return False

def tofloat(message: str) -> float or False:
    try: return float(message)
    except ValueError:
        return False

def obtain_type(str: str) -> Types:
    if tofloat(str):
        if toint(str) == tofloat(str):
            return Types.int
        return Types.float
    if len(str) == 1:
        return Types.char
    return Types.string if len(str) > 0 else Types.unknown

def nprint(stuff: str) -> None:
    array = stuff.split("\n")
    [print(array[x] + "{:s}\033[10000D".format("\n" if x != len(array) -1 else ""), end="") for x in range(len(array))]

def warn(message: str) -> None:
    if not isatty(stdin.fileno()):
        return
    print("{}warn{} {}".format(c.blora + "[" + c.r, c.blora + "]" + c.r, message))

def info(message: str) -> None:
    if not isatty(stdin.fileno()):
        return
    print(f"{c.info}:?{c.r} {message}")

def execute(command: str):
    result = run(command, stdout=PIPE, shell=True, text=True)
    return result.stdout.strip()