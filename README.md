# CUNIT Tests

## What is it ?

Cunit is a unit testing software for C.<br/>
You can test your functions with tests you wrote in real time, or from a file.

To launch it in real time, just type :
```php
$ ./cunit/run
```

But if you have a file, you can type :
```php
$ ./cunit/run < file.txt
```

<br/>

## Cool ! How can I get it ?

To get it, simply clone this repository by doing this command :
```
$ git clone https://github.com/paulogarithm/cunit
```
in your repository.<br/>

You should have something like this
```
$ ls
include/   lib/   Makefile   src/

$ git clone https://github.com/paulogarithm/cunit
...

$ ls
cunit/   include/   lib/   Makefile   src/
```

<br/>

## Now that I have it, how does it work ?

### General

So basically, you need to add files that contains the functions. <br/>
For the example, we will take this max function :
```c
// max_int_file.c

int max_int(const int a, const int b)
{
    return ((a >= b) ? a : b);
}
```

<br/>

So you will need to add the file, and 


