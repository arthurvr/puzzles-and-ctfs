# Fruity Cipher

> I found this fruity message. Can you decrypt it?
>
> * lowercase only, no spaces
> * wrap into he2023{ and }
> * example: `he2023{exampleflagonly}`

I immediately thought about a cipher where every emoji represents a single letter. The longest word there, is 16 characters long and the 6th, 10th and 14th character are the same. I had no idea how much 16-character english words there were with this property... but I tried finding them quickly using a list of English words I found online. The script is in `search.php`.

Turns out, there's not that much:

```
electrodepositor
extrapatriarchal
fashion-fancying
hypervitaminosis
interferometries
noncorroboratory
nonprotractility
passion-kindling
protopatriarchal
radiotelemetries
roentgenometries
serosanguinolent
speckle-breasted
terrace-steepled
well-deliberated
```

This word `hypervitaminosis` looked interesting in this context... and indeed, the flag is `he2023/hypervitaminosis`.
