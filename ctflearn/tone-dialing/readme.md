# Tone dialing 

> At 1pm I called my uncle who was 64 years old 10 months ago, but I heard only that. Later I started thinking about the 24 hour clock.

> I hope you will help me solve this problem

I used [this tool](https://github.com/ribt/dtmf-decoder) to decode dual-tone multi-frequency signaling. The result looked like ASCII:

```
67 84 70 108 101 97 110 123 67 82 89 80 84 79 71 82 65 80 72 89 125
```

CyberChef helped me figure out this means `CTFlean{CRYPTOGRAPHY}` (note the missing `r`). This flag is correct. One thing I don't get: what was this clock-thing in the challenge text about?

