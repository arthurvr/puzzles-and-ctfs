# babygame01

> Get the flag and reach the exit.

I opened the given executable in IDA. After renaming some variables, the program became quite readable (I used *F5* to get the decompiled pseudo-code):

![](https://i.imgur.com/rUBk786.png)

Let's also have a close look at the `move_player` function:

![](https://i.imgur.com/q7U2N08.png)

The `w` / `s` / `a` / `d` gameplay is as expected. `p` to solve the game is new though! Also, have a close look at how the position variable is overwritten: we can overwrite the variables before the map buffer... I tried to overwrite `win_var`, which is 4 bytes before the map, by first navigating to (0, 0) and then moving back another 4 positions. This worked:

![](https://i.imgur.com/KxXmUFy.png)

(Notice the *"Player has flag"* message!)

Now let's just win the game using `p`.

![](https://i.imgur.com/KxXmUFy.png)
