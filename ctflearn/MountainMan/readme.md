# MountainMan

> Don't be fooled by two `0xffd9` markers. XOR is your friend.

I had to google this too, but a `0xffd9` marker is the marker that ends an image. So you'd expect there to be one at the end of the file. Let's inspect the given image. I used the default `hexedit` tool in Kali Linux.

![](https://imgur.com/q9yyvwQ.png)

So indeed there are two of these markers. The first one is the one that counts, so I'm very interested in what's in between the two.

I did not immediately know what to do with these bytes, or what to XOR them with. But CyberChef has a "magic" function that can maybe help...

![](https://imgur.com/jZ9ZbBN.png)

Which is the correct flag! (I did have to insert the flag format, `CTFlearn{\w*}`, as a hint.)



