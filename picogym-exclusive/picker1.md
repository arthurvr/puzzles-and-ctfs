# Picker I

> This service can provide you with a random number, but can it do anything else?

Have a look at the given source code: the script passes the given function name to an `eval`-call:

```
  try:
    print('Try entering "getRandomNumber" without the double quotes...')
    user_input = input('==> ')
    eval(user_input + '()')
```

We're asked to enter `getRandomNumber`: the name of the function that's supposed to generate the random number. However, there's also a function `win` in the source code that prints the flag. Let's try:


![](https://i.imgur.com/vs4mUNg.png)


Now, I just need to convert the hexadecimal ASCII representation to something readable. [CyberChef](http://cyberchef.org) to the rescue!

![](https://i.imgur.com/WX0Y0Ls.png)
