# A CAPture of a Flag

> This isn't what I had in mind, when I asked someone to capture a flag... can you help? You should check out WireShark. 

I first added the `pcap` extension to the file and opened it in wireshark.

When doing challenges like these I always check the http traffic first: it's usually the most interesting. Following request catched my attention:

```
GET /?msg=ZmxhZ3tBRmxhZ0luUENBUH0= HTTP/1.1
Host: www.hazzy.co.uk
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en;q=0.8
Cookie: language=en-gb; currency=USD
```

The `msg` in there is base 64 encoding:

```
$ echo "ZmxhZ3tBRmxhZ0luUENBUH0=" | base64 -D
flag{AFlagInPCAP}
```
