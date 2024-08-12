# SOAP

> The web project was rushed and no security assessment was done. Can you read the `/etc/passwd` file?

This challenge had the label `XXE`, this might refer to [XML external entity injection](https://portswigger.net/web-security/xxe).

I inspected the network traffic using the browser dev tools. Apparently, when clicking one ofthe *Details* buttons a separate HTTP request happens. It's request is formatted as `application/xml`. Let's see if this request is indeed vulnerable to XXE.

![](https://imgur.com/aERdo3s.png)

Notice the flag on the last line. *Pro tip: you can use Firefox devtools to copy a request as a `cURL` command: this makes the request look exactly like it's coming from your brower.*
