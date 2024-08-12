# Naughty Cat

This challenge is a combination of lots of forensics techniques I've used for ctflearn before:

1. First use `binwalk` to detect hidden files. Besides the image itself, there's a zip file and a rar archive in there.
2. Use `unrar` to open the archive at 28E4B: it contains `y0u_4r3_cl0s3.rar` and `purrr_2.mp3`.
3. Using `file` the `y0u_4r3_cl0s3.rar` file looks corrupted: it just shows up as `data`, not as a rar archive.
4. Use hexedit (or similar software) to correct the corrupt file's [magic number](https://en.wikipedia.org/wiki/List_of_file_signatures): the first bytes should be `52 61 72 21 1A 07 01 00`
5. `unrar` asks for a password when opening this rar file, so we're stuck here for now :/
6. The MP3 file sounded like nothing, but a visualizer showed this:

![](https://i.imgur.com/KKG1UxO.png)

This was clever!!

7. I can now unrar the last rar file using the password `sp3ctrum_1s_y0ur_fr13nd`.
8. It contains a text file, containing the base64 string `ZjByM241MWNzX21hNXQzcg==`.
9. Decode this to get the flag:

```
echo "ZjByM241MWNzX21hNXQzcg==" | base64 -D
```
