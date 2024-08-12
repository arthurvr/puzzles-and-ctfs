# Who is it?

> Someone just sent you an email claiming to be Google's co-founder Larry Page but you suspect a scam.
Can you help us identify whose mail server the email actually originated from?

> Download the email file here. Flag: `picoCTF{FirstnameLastname}`

I opened the email in a text editor, and checked the `Received` field. It read `173.249.33.206`. I then called `whois` on this IP address, and found a name:

```
$ whois 173.249.33.206
...
person:         Wilhelm Zwalina
...
```
