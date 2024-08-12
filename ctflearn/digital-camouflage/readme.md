# Digital Camouflage 

> We need to gain access to some routers. Let's try and see if we can find the password in the captured network data.

As always I use Wireshark to inspect `.pcap` files, and I usually look at HTTP traffic first. There's one http request extra interesting, because wireshark immediately indicates it contains `x-www-form-urlencoded` data (the `POST /pages/main.html` one).

The value of the password field is base64 encoded. Decoding it gave me the right flag.


