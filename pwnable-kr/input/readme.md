# Toddler's Bottle - input

> Mom? how can I pass my input to a computer program?

Again, the right way to start is inspecting [the source code of `input.c`](https://imgur.com/OK4qagi.png) carefully. Looks like we have to clear several *"stages"*, all concerned with a different type of input we provide:

1. Stage one is about the command line arguments. `argc` and `argv` must be as expected. Specifically, `argc` should be 100, and `argv['A']` (= `argv[65]`) and `argv['B']` must be a specified value. 
2. Stage two is about stdio. The program reads 4 bytes from file descriptor `2` and 4 bytes from file descriptor `0`. That's `stdin` and `stderr`.
3. Stage three checks the value of an environment variable.
4. Stage four opens, reads and checks the contents of a file.
5. Stage five opens a socket on localhost, on a port set by `argv['C']`. It starts listening and expects to receive 4 specified bytes. 

The fastest way to run the `input` executable seemed to be to write a C program myself, that executes `input` using [`execve`](https://www.man7.org/linux/man-pages/man2/execve.2.html).
That provides fine-grained control over all these ways to input a program. I did that in `/tmp/arthur`. As there is a log in `login.c` after every stage, developing this program should be straightforward.
My program has the following to clear all stages:

1. I created an `arguments` array with 100 strings, to be passed as `argv` (which is an arugment of `execve`). Setting the correct values for `argv['A']` and the others is trivial on this array.
2. Programatically "piping" towards the program was actually the most challenging part for me. Turns out I had to fork the process, and `write()` on the file descriptors there. There's some good guides online. The child process is going to be useful for the networking stage too I think.
3. The environment is an array argument passed to `execve` too.
4. I created the file with the desired name & value and saved it before calling `input`.
5. Within the same child process used to pipe to `stdin` and `stderr`, I added a small `sleep()`-time and then started a socket on the same addr/port as the one `input` is listening on. Then I sent the expected bytes.

When all stages succeed, the given program starts a new shell and executes `/bin/cat flag`. My program does not work when executed from `/home/input2`, only from my directory `/tmp/arthur`, so this is a problem. The `flag` file isn't there. The easiest solution I could come up with is a symlink called `flag` in my temorary directory.

Looks like it works, this is the flag:

![](https://i.imgur.com/DsJaYAA.png)