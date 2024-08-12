# Chalkboard

> Solve the equations embedded in the jpeg to find the flag. Solve this problem before solving my Scope challenge which is worth 100 points.

It's not about the equations visible in the image! (Obviously, as none of them is on there completely...) However, there are also equations embedded in the image in another way:


```
~/c/c/chalkboard ❯❯❯ strings math.jpg | grep -C 5 flag  
JFIF
The flag for this challenge is of the form:
CTFlearn{I_Like_Math_x_y}
where x and y are the solution to these equations:
3x + 5y = 31
7x + 9y = 59
A#BQR
```

I just used WolframAlpha to solve those.
