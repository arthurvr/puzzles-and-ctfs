# Sequences

> I wrote this linear recurrence function, can you figure out how to make it run fast enough and get the flag?

Linear recurrences are solvable (*some are?*). I just let [StackOverflow](https://www.wolframalpha.com/input?i=%281612+%28-21%29%5En+%2B+30685+2%5E%285+%2B+2+n%29+3%5En+-+1082829+13%5En+%2B+8349+17%5E%281+%2B+n%29%29%2F42636+mod+10%5E10000+for+n+%3D+2*10%5E7) do the maths, and couldn't be bothered rewriting the Python.  Then I could paste the result in and not rewriting the calculation.

Small note: if you just paste the `sol` number from StackOverflow, Python will complain that the integer literal is too big. You can turn this warning off using `sys.set_int_max_str_digits(0)`. However, I went for an easier solution: just make `sol` a string - the program converts it to a string later anyway...

This gets us `picoCTF{b1g_numb3rs_3956e6c2}`.