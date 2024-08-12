# scrambled-bytes

> I sent my secret flag over the wires, but the bytes got all mixed up!

The given script seems to do the following: the data is first shuffled, then sent one byte at a time as a UDP packet, XORed with a random number. I can find these UDP packets in the capture-file using Wireshark:

![](https://imgur.com/ZZDMUfv.png)

I think I should be able to filter for only these 1-byte UDP packets by checking the destination port, which seems to be 56742. However, I will also have to unshuffle and "decrypt" these bytes. There's one small detail I hadn't immediately noticed, this line:

```
random.seed(int(time()))
```

In the capture file, I can find this timestamp... so I can re-generate all random numbers :)

My script for reading the packets, filtering them, decrypting them and unshuffeling is in `solution.py`. I used `scapy` for easily working with the capture file. The output bytes were not anything readable, so I decided to write them to a binary file. Looks like it's a PNG:

![](https://i.imgur.com/gAraZfz.png)

And this image does indeed contain the flag:

![](https://i.imgur.com/iKThfyF.png)
