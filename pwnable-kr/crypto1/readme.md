# Rookiss - crypto1

> We have isolated the authentication procedure to another box using RPC. 
>
> The credential information between RPC is encrypted with AES-CBC, so it will be secure enough from sniffing.
>
> I believe no one can login as admin but me :p

These two sample inputs already show the beginning of a flaw in the encryption system. Notice how, for different input data, a big chunk at the start of these ciphertexts is the same. The length of the ciphertexts is also the same, even thought the length of the plaintexts is different.

```
arthur@A-PC:~$ nc pwnable.kr 9006
---------------------------------------------------
-       PWNABLE.KR secure RPC login system        -
---------------------------------------------------

Input your ID
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Input your PW
password
sending encrypted data (166827d3124ce5db2b36e803b9115a4973ea815d3dba21c8f2b6960ca5c2bccef4f98604660a15a6e0fea75b355a14b4dc40b6e216df8c88271af064a0fb9bd78205d4db0deb402315141bae4a5ec3d344353989732d136286736306ad240765)
you are not authenticated user

arthur@A-PC:~$ nc pwnable.kr 9006
---------------------------------------------------
-       PWNABLE.KR secure RPC login system        -
---------------------------------------------------

Input your ID
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Input your PW
admin
sending encrypted data (166827d3124ce5db2b36e803b9115a4973ea815d3dba21c8f2b6960ca5c2bcce0f7f86a7402b235fe7f4da6e791c8d83931502a91a0cf13f68354b7b585b1a0b7d64ec958c84f33384d513a59f4723c0913713ca758c829d87c78c1355fce3c1)
you are not authenticated user
```

These are signs of a [CBC block cipher](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation), one that doesn't seem to use unique IV-values.

I wanted to quickly show this, but actually, the source code for the encryption process is given :) Let's have a look at `client.py` and `server.py` now:

* Indeed, the key and the IV (!) are hardcoded in the program too.
* Indeed, AES in CBC mode.
* Only characters from `"1234567890abcdefghijklmnopqrstuvwxyz-_"` are allowed. No capital letters, no special symbols, ... this makes the encryption system significantly weaker!
* The encrypted plaintext is equal to `username-password-cookie`, with cookie a hard coded value.
* The flag is given when logging in as the admin user. His password is compared to `hashlib.sha256(id+cookie).hexdigest()`.
* Block size is 16 and padding happens using null bytes.
* There is no serious test to check if requests are coming from `client.py`, so I could make requests directly to the server started in `server.py`: the one at port 9100.

Using this knowledge, let's first figure out the length of the cookie. If we enter an empty username and empty password, the encrypted packet is 64 bytes (that's 128 bytes after the hex encoding). It's still 64 bytes when the length of our username is 1, 2, 3, ... characters, until 12 characters. When the username becomes 13 characters, the result is 80 bytes long (= one 16-byte block more). That means:

```
13 characters + '-' + '-' + cookie + 16 null bytes = 80 bytes
```

Meaning cookie should be 49 bytes long.

Given the length of the cookie and quirks of CBC mode with a fixed IV, I think we can base our attack on the following.

* Say we use a 13-byte username, empty password. We can calculate what the encryption of `"-"*15+cookie` is supposed to be.
* We can try different `x` values and let the service encrypt `"-"*15+cookie`. The range of possible `x` values is not that high, and we can leave some time in between requests if we want. I don't consider this *excessive* brute-forcing or harmful to their server, but always be careful when using this technique!
* We can compare the results (specifically, compare the block that's supposed to be equal).

I implemented this in `exploit.py`. It found the following cookie:

```
you_will_never_guess_this_sugar_honey_salt_cookie
```

Which makes for the following admin password:

```
fcf00f6fc7f66ffcfec02eaf69d30398b773fa9b2bc398f960784d60048cc503
```

Let's try:

![](https://i.imgur.com/3Rr8hhL.png)
