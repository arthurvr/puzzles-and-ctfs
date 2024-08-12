# The Keymaker

> Jpeg comments can be very interesting.

As always I first called `strings`. It contains a fake flag first, but then there's a few base64 encoded strings:

```
b3BlbnNzbCBlbmMgLWQgLWFlcy0yNTYtY2JjIC1pdiBTT0YwIC1LIFNPUyAtaW4gZmxhZy5lbmMg
LW91dCBmbGFnIC1iYXNlNjQKCml2IGRvZXMgbm90IGluY2x1ZGUgdGhlIG1hcmtlciBvciBsZW5n
dGggb2YgU09GMAoKa2V5IGRvZXMgbm90IGluY2x1ZGUgdGhlIFMwUyBtYXJrZXIKCg==
CmmtaSHhAsK9pLMepyFDl37UTXQT0CMltZk7+4Kaa1svo5vqb6JuczUqQGFJYiycY
```

* I decoded this using cyberchef:

```
openssl enc -d -aes-256-cbc -iv SOF0 -K SOS -in flag.enc -out flag -base64

iv does not include the marker or length of SOF0

key does not include the S0S marker
```

* The last part doesn't seem like text, but rather the ciphertext. I saved it (in base64) in `flag.enc`.

* Use a hex editor to find SOF0 (and some knowledge from the JPG spec). We find SOF0 with `0xff` `0xc0`, and the length of SOF0 is `0x00` `0x11`. I found the IV to be `0800be00c803011100021101031101ff`.

* In the commands, S0S is for `0xff` `0xda` (see the JPEG spec), the key is: `000c03010002110311003f00f9766bfc44beda8f3f5c031b92cb0e92d6bdc952`.

* Now use the given command, but make it do decryption:

```
openssl enc -d -aes-256-cbc -iv 0800be00c803011100021101031101ff -K 000c03010002110311003f00f9766bfc44beda8f3f5c031b92cb0e92d6bdc952 -in flag.enc -out flag -base64
```

* This created a new `flag` file, containing the flag:

```
CTFlearn{Ne0.TheMatrix}
```
