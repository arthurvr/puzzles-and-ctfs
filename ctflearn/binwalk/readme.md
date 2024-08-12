# binwalk

> Here is a file with another file hidden inside it. Can you extract it?

At first, the given file looks like a simple image. However, the title is a huge hint: binwalk is a tool for searching binary images for embedded files and executable code.

Let's explore:

![](https://i.imgur.com/RBx2oUr.png)

Extracting the files is done using the command

```bash
binwalk -D='.*' PurpleThing.jpeg
```

(for extracting all extensions)

Using `file` we can now find out one of the files in the `.extracted` folder is in fact a PNG. Opening it as a PNG reveals the flag.