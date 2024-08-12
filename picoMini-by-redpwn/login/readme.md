# login

> My dog-sitter's brother made this website but I can't get in; can you help?

The script attached to the web page looks minimised/obfuscated, but it's quite short so I cleaned it up manually. A clean, readable version is in [`script.js`](script.js). Looks like all verification happens on the client side.

To understand the script, you have to understand only little javascript and the meaning of the following functions:

* `btoa`: creates base64 from a string
* `atob`: converts base64 back to the original string

So the juicy part seems to be in the if-statement (`.. ? .. : ..`) in the return statement, and we have to decode the strings to understand them. I used cyberchef to decode base64, but you can use any tool.

* The decoding of `"YWRtaW4"` is `"admin"`
* The decoding of `"cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ"` is `"picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}"`

Which is the right login combination, and also immediately the right flag.