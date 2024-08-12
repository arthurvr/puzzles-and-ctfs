# findme

> Help us test the form by submiting the username as `test` and password as `test!` 

In the browser, everything looks deadly normal when logging in. However, when checking out the traffic a bit better, apparently there's a redirection in between the login process. I used `curl`:

![](https://i.imgur.com/swad3m9.png)

Hmm, how would this ID be generated? Let's see what's up with that `next-page/` link now: 

![](https://i.imgur.com/eM1Mk8m.png)

Another redirect, but the redirect happens using JavaScript on the client-side now.

The last `==` characters in that id looks suspicious... it looks like Base64. Let's try:

![](https://i.imgur.com/ibViR93.png)
