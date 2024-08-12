# Extended basics 5

The given shell script is:

```sh
#!/bin/sh
rm OK
sed -E "s/eval/safeeval/" <exec.php >tmp && touch OK
if [ -f OK ]; then
        rm exec.php && mv tmp exec.php
fi
```

I think his search-and-replace operation won't replace all `eval()` calls, only the first one. This does what he wants:

```sh
sed -E "s/eval/safeeval/g" <exec.php >tmp && touch OK
```
