# Eavesdrop

> Download this packet capture and find the flag.

I opened the pcap-file in Wireshark. The TCP packets seemed like the most
interesting, and wireshark makes it really easy to follow the conversation using
*Follow > TCP stream*:

![](https://i.imgur.com/r8HfORN.png)

In particular, the decryption command there looks useful. Let's go looking for the file too. Let's look at the traffic for port 9002 now: Indeed an encrypted file!

![](https://i.imgur.com/s4GhMyd.png)

Which we can save the raw bytes of, and try if the decryption instructions work:

![](https://i.imgur.com/UYD7ZPg.png)





