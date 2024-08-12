# RPS

> Here's a program that plays rock, paper, scissors against you. I hear something good happens if you win 5 times in a row.

> The program's source code with the flag redacted can be downloaded.

* First thought: On average I'd need less than 3^5 attempts... could just brute force this one with a simple python script.

* Second thought: this could also be about random number generators!

* However, I feel like this challenge is probably about exploiting the call to `strstr` on line 100. The point of this function is usually finding a substring, but it's not really used in this way. (See `man strstr`.)

* I think you could trick the program with the an unexpected input... Would `rockpaperscissors` win all the time?

* It does!

![](https://imgur.com/QtDuFVO.png)
