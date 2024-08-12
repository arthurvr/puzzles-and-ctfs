# Reverse

> Try reversing this file? Can ya?
> I forgot the password to this file. Please find it for me?

No need to execute the file... actually, it's a good habit not to execute files before very thoroughly inspecting them! I opened the given file up in IDA. Right after the `strcmp` call (that checks the password), there is a message printed to the screen in a conditional branch:

![](https://i.imgur.com/9sqj11O.png)

Just check out the complete flag in the memory view:

![](https://i.imgur.com/GPxxw7g.png)
