import re

from globals import *
from colors import c
from processfunction import get_fullfunctions, get_functionsname
from os import walk
from os.path import join

def get_percentage(str: str) -> str or False:
    split = str.split("(")
    method = split[0]
    if "int" in method:
        return "%d"
    if ("double" in method) or ("float" in method):
        return "%f"
    if "char *" in method:
        return "%s"
    if "char" in method:
        return "%c"
    return False


def get_type(args: list[str]) -> list[str]:
    ret = []
    for a in args:
        if a.startswith("\"") and a.endswith("\""):
            ret.append(a)
            continue
        if a.startswith("\'") and a.endswith("\'") and len(a) == 3:
            ret.append('\'' + a[2:] + '\'')
            continue
        a_type = obtain_type(a)
        if a_type == Types.char:
            ret.append('\'' + a + '\'')
        elif a_type == Types.float or a_type == Types.int:
            ret.append(a)
        elif a_type == Types.string:
            ret.append('\"' + a + '\"')
    return ret

def write_functions() -> None:
    alreadywritten = []
    with open(p_cfile, "w") as f:
        f.truncate(0)
    with open(p_cfile, "w") as f:
        f.write("// Tests unipol\n\n")
        f.write("#include <stdio.h>\n\n")
        for t in my_tests:
            if t.func[0] in alreadywritten:
                continue
            alreadywritten.append(t.func[0])
            f.write(t.func[0] + ('\n' if t.func[0][-1] == ';' else ';\n'))

def write_main() -> None:
    with open(p_cfile, "a") as f:
        f.write("\nint main(void) {\n")
        for t in my_tests:
            percentage = get_percentage(t.func[0])
            func = t.func[1]
            args = get_type(t.args)
            f.write("\tprintf(\"{}\\n\", {}({}));\n".format(percentage, func, ", ".join(args)))
        f.write("}\n")

def compare_results(res: str) -> None:
    array = res.split('\n')
    for i in range(len(array)):
        yours = array[i]
        valid = my_tests[i].res
        print("TEST [{}]\t".format(c.pur + str(i) + c.r), end='')
        if valid == yours:
            print(c.grn + "Passed" + c.r, end=' ')
        else:
            print(c.red + "Failed" + c.r, end=' ')
        print("({} {} {})".format(yours, "==" if valid == yours else "!=", valid))

def get_functionfile(func: str) -> str:
    for dirpath, dirnames, filenames in walk(p_root):
        for file in filenames:
            if file.endswith('.c'):
                filepath = join(dirpath, file)
                with open(filepath, "r") as fstr:
                    content = fstr.read()
                    functions = []
                    pattern = r'(\w+)\s+(\w+)\s*\((.*?)\)\s*{([^{}]*)}'
                    for match in re.finditer(pattern, content, re.DOTALL):
                        functions.append(match.group(2))
                    if func in functions:
                        return filepath
    return False

def process_run() -> None:
    all_files = []
    all_Ffuncs = get_fullfunctions()
    all_funcs = get_functionsname(all_Ffuncs)
    for func in all_funcs:
        thefile = get_functionfile(func[1])
        if not thefile or thefile in all_files:
            continue
        all_files.append(thefile)
    write_functions()
    write_main()
    myfiles = " ".join(all_files)
    mybin = p_playground + "/a.out"
    execute(f"gcc {p_cfile} {myfiles} -o {mybin}")
    res = execute("{}/a.out".format(p_playground))
    compare_results(res)