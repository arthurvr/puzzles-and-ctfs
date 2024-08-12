# hijacking

> Getting root access can allow you to read the flag. Luckily there is a python file that you might like to play with.

> Additional details will be available after launching your challenge instance.

There's this `.server.py` in the home folder that does nothing but throwing an error:

![](https://i.imgur.com/k4jClcX.png)

The challenge is about root access to let's check out what I can do as root using `sudo -l`:

![](https://i.imgur.com/uVtOZTS.png)

Ah, interesting! However, it seems like the `.server.py` file doesn't do anything different when executing it as root :/ Maybe I should have a look if something strange is going on with the `python` installation itself (which I can apparently run as root!). I found a file in there which has strange (more permitting) permissions:

![](https://i.imgur.com/7Tps0h4.png)

Let's edit this file and see if it executes. Seems like it does:

![](https://i.imgur.com/5HJlBn5.png)
![](https://i.imgur.com/YpaBcmZ.png)

I can now execute any command as root :)) In the other challenges the flag was in a folder in the root directory, let's try to find it there again.

![](https://i.imgur.com/3cHgsF5.png)
![](https://i.imgur.com/hrFnWll.png)
![](https://i.imgur.com/I7B4W0c.png)

There we go:

![](https://i.imgur.com/3DlvqZi.png)
