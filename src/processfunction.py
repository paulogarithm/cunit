import re

from globals import *

def get_fullfunctions() -> list[str]:
    regex = r"\b\w+\b(?:\s*(\*)*\w+)+\s*\((void|(?:\w+(?:\s+\**\w+(\[\])*)+(?:,\s*\w+(?:\s+\**\w+(\[\])*)+)*))*\)(;)*"
    results = []
    for e in my_files:
        with open(e, "r") as f:
            for line in f:
                if re.search(regex, line):
                    results.append(line.strip())
    return results


def get_functionsname(elements: list[str]) -> list[str]:
    res = []
    for e in elements:
        subres = []
        subres.append(e)
        subres.append(re.search(r"\b(\w+)\(", e).group(1))
        res.append(subres)
    return res


def show_functions(array: list[str]):
    res = ""
    if len(array) == 0:
        return info("No function added yet.")
    res += "[{}{}{}] functions added :\n".format(c.lgrn, len(array), c.r)
    for i in range(len(array)):
        res += "{}{}{}. ".format(c.unde, i + 1, c.r) + array[i] + "\n"
    return nprint(res)


def count_args(fullfunc: str):
    args_str = re.search(r'\((.*)\)', fullfunc).group(1)
    return args_str.count(',') + 1 if args_str else 0


def splitarray(array: list[str]) -> tuple[list[str], list[str]] or False:
    a = []
    b = []
    cur = "a"
    for i in array:
        if i == "==":
            cur = "b"
            continue
        a.append(i) if cur == "a" else b.append(i)
    return a, (b if len(b) > 0 else False)


def save_test(func: list[2:str], split: list[str]) -> None:
    nbargs = count_args(func[0])
    args, res = splitarray(split)
    if not res:
        return warn("Nothing to compare.")
    if len(args) < nbargs:
        return warn("Not enough arguments (this function takes {}, you gave {}).".format(nbargs, len(args)))
    if len(args) > nbargs:
        return warn("Too much arguments (this function takes {}, you gave {}).".format(nbargs, len(args)))
    if len(res) != 1:
        return warn("Too much compares (expected 1).")
    ret = Test(func, args, res[0])
    my_tests.append(ret)

def parse_command(command: str):
    parts = re.findall(r'\'[^\']*\'|\"[^\"]*\"|\S+', command)
    return parts

def process_function(command: str):
    command = command[2:]
    split = parse_command(command)
    my_func = split[0]
    all_Ffunc = get_fullfunctions()
    all_func = get_functionsname(all_Ffunc)

    if my_func == command == "?":
        return show_functions(all_Ffunc)
    func = False
    for i in range(len(all_func)):
        if my_func == all_func[i][1]:
            func = all_func[i]
            break
    if not func:
        return warn("Function '{}' do not exist".format(my_func))
    split.pop(0)
    save_test(func, split)