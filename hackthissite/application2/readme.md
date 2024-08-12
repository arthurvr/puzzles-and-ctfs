# Application 2

Now, it looks like the application is checking the license code online:

![](https://i.imgur.com/o9hI72P.png)

I used the now-deprecated, official *Windows Network Monitor* to check out what network traffic the application is creating. I do these challenges on a clean VM, which is an advantage in this case, as almost no other network traffic is happening. It looks like the HTTP response from the `hackthissite.org` server contains a list of valid license keys...

![](https://i.imgur.com/40G3hBu.png)

I tried one of those keys and it worked.

![](https://i.imgur.com/4bUKo6h.png)