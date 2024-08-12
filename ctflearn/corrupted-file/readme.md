# Corrupted file

> Help! I can't open this file. Something to do with the file header… Whatever that is. 

Opening it up in a hex exitor, the file header is indeed the problem. (*the ["file signature"](https://en.wikipedia.org/wiki/List_of_file_signatures)*). Some bytes of the normal GIF89 header are missing. When I add the missing bytes and save, I get a valid gif file with multiple frames:

![](https://i.imgur.com/CEVchpM.png)

The text to decode inside is base64. It's the flag: `flag{g1f_or_j1f}`.
