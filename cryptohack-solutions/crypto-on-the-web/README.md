# Crypto on the web

## JSON Web Tokens

- *Token Appreciation*: Decode a JWT cookie using the PyJWT library. [Solution ↗️](token-appreciation.py)

- *JWT Session*: The answer here is the name of the HTTP header used by the browser to send JWTs to the server. That's `Authorization`.

- *No Way JOSE*: This demo shows how to bypass authorization when the algorithm is set to `none`. Just use [token.dev](https://token.dev) to modify both the algorithm and the `admin` flag.

- *JWT Secrets*: Again, we need to generate a new cookie, now using HS256 signing. We need to use the default secret in the PyJWT readme: `"secret"`. [Solution ↗️](jwt-secrets.py)

## TLS part 1: the protocol

- *Secure Protocols*: Easy first challenge - just read it! It's a simple introduction to TLS. Then you're asked to inspect a given certificate and extract the name of the CA that issued it. Luckily modern browsers all have a feature to [inspect](https://imgur.com/a/Kjo9mvU) a site's certificate.

- *Sharks on the wire*: Given a `.pcapng` file we're asked how many packets were received by `cryptohack.org`. First, I can hit `View > Name Resolution > Resolve Network Addresses` to see domain names instead of IP addresses. This makes it clear which address `cryptohack.org` is. Then I apply a `ip.dst == 178.62.74.206` filter. 15 packets are shown.

- *TLS Handshake*: Question on the `.pcapng` file. The challenge walks us through which packets are sent, so once you read through the challenge, it's pretty obvious that you have to check out packets 12-17 (where the *ServerHello* is sent). Then, [Wireshark makes it really obvious which data we're looking for.](https://imgur.com/a/BcXHT5c)

## Cloud

