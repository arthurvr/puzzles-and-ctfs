# SSH keys

> Extract the modulus n as a decimal integer from Bruce's SSH public key.

First we can extract the public key using

```
$ ssh-keygen -f ~/Downloads/bruce_rsa_6e7ecd53b443a97 013397b1a1ea30e14.pub -e -m pem
```

Then we can decode the ASN.1 public key using [this online decoder](https://lapo.it/asn1js). The modulus is the 3072 bit integer in there.
