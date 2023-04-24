# CUNIT Tests

## What is it ?

Cunit is a unit testing software for C.<br/>
You can test your functions with tests you wrote in real time, or from a file.

To launch it in real time, just type :
```
[root@user ~] ./cunit/run
```

But if you have a file, you can type :
```
[root@user ~] ./cunit/run < file.txt
```

<br/>

## Cool ! How can I get it ?

To get it, simply clone this repository by doing this command :
```
[root@user ~] git clone https://github.com/paulogarithm/cunit
```
in your repository.<br/>

You should have something like this
```
[root@user ~] ls
include/   lib/   Makefile   src/

[root@user ~] git clone https://github.com/paulogarithm/cunit
...

[root@user ~] ls
cunit/   include/   lib/   Makefile   src/
```

<br>

## Now that I have it, how does it work ?

### A Simple Explication

So basically, you need to add files that contains the functions. <br/>
For the example, we will take this max function :
```c
// my_file.c

int max_int(const int a, const int b)
{
    return ((a >= b) ? a : b);
}
```

<br>

Now that you have the function that you want to test, you will need to **include the file** by using the `@` character. <br>
Basically, It's working like this :
```python
> @ my_file.c
```

Once you have include the file, you can now on create a test by using the `$` character. <br> <br>

To write a test, you will need to follow this architecture `> $ <functionName> <arg1> <arg2> ... == <result>`<br><br>

Let's take back our example. So we want to check which number is bigger between `42` and `69`, so this is how to write a test :
```css
> $ max_int 42 69 == 69
```
And here is what it looks like in C :
```c
int max_int(42, 69)
```

Once your test is written, simply run it by typing `run` or `test` in the cunit console.
```css
> run
```

You should now have your test result

```lua
TEST [1]    Passed (69 == 69)
```

So the number in the box is the test's position (if it's the first one, or the second one...). <br>
You have the test's status just after, either Passed of Failed. <br>
And then you have the results : <br>
- At the left, the one you given.<br>
- At the right, the one your function returns.

Once you're finished, type `q` or `quit` to leave the program. You can also quit with CTRL + C.

### Can I use a file ?

If people requires a trace for your tests, or you want to repeat tests without rewrite them manually, you <br>
can simply write your instruction in a file in this way :

`Unit.txt`
```
@ my_file.c
$ $ max_int 42 69 == 69
run
```

Then, execute it by giving it to the program's input in this way :
```
[root@user ~] ./cunit/run < Unit.txt
```

Now, I'm going to explain you more in details, but basically you have pretty much everything.

## Some usefull commands

Here is a table for all commands you can use

| COMMAND            | ACTION               |
|--------------------|----------------------|
| `q, quit, leave`   | Leaves the program.  |
| `r, run, test`     | Tests your program.  |
| `c, cls, clear`    | Clears the terminal. |
| `?, v, view, omni` | ~View you tests.~    |
| `h, help`          | ~Display Help.~      |

Note: The last 2 dosent have been created yet.


## How does file importation works ?

### Add a file

In order to create tests, you will need to import files by using the `@` character before your file path. <br>
```
> @ a.c
:? a.c Added
```

### See the files

You can use `@ ?` to see which file you have imported so far. Here is a little example :

```
> @ src/a.c
:? a.c Added

> @ src/b.c
:? b.c Added

> @ ?
[2] file added :
1. a.c
2. b.c
```

### Remove a file

If you already imported a file, and you try to re-call the importation, the file will remove :
```
> @ a.c
:? a.c Added

> @ ?
[1] file added :
1. a.c

> @ a.c
:? a.c Removed

> @ ?
:? No file added
```

## Now for the functions part

### How can I see all the functions ?

You can see all the function by using the `$` character followed by `?`.

```
> $ ?
No function added yet.

> @ a.c
:? a.c Added

> $ ?
[3] functions added :
1. int first(int a);
2. int second(int a);
3. int third(int a);
```

### How can I write a test ?

Once you have imported your functions, you can test them by following this pattern :

```
> $ <functionName> <args...> == <compare>
```

This will write you a test that you can run by doing the `run` command.
