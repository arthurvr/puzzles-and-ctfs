# Torrent analyze

> SOS, someone is torrenting on our network. One of your colleagues has been using torrent to download some files on the company’s network. Can you identify the file(s) that were downloaded? The file name will be the flag, like picoCTF{filename}. 

It's a pcap file, which I can open and analyze using Wireshark. What we're looking for is called an `info_hash`. It is used to uniquely identify a torrent. The hash that appears a lot of times in our pcap is the following one:

![](https://imgur.com/VZXqkHb.png)

Which we can Google for to identify what file this is about:

![](https://imgur.com/HwTGL0k.png)

The flag is:

```
picoCTF{ubuntu-19.10-desktop-amd64.iso}
```
