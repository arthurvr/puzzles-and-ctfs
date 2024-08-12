# FindAndOpen

> Someone might have hidden the password in the trace file. Find the key to unlock *this file*. This *tracefile* might be good to analyze.

I opened the pcap file in Wireshark. There was some plaintext communication in the Ethernet packages, so I focused on these. This one suspiciously looked like base64:

![](https://i.imgur.com/IUNViWG.png)

Seems like it is base64:

![](https://i.imgur.com/xXtsiQL.png)

Now I tried finding another part of the flag in the pcap file without luck 😢 After a long time I just tried the beginning of the flag as password to the zip file... this worked. The flag is in there:

```
picoCTF{R34DING_LOKd_fil56_succ3ss_5ed3a878}
```
