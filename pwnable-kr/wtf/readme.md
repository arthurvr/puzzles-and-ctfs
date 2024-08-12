# Grotesque - wtf

> I don't understand why my exploit is not working.
>
> I need your help.

The dissasembled source code using IDA: [🔗](https://imgur.com/a/guWOBKL).

Some thoughts reading through the code:
	
 * The I/O queue only has 4096 bytes. That could have an effect on the first `scanf`: If more than 4096 are entered, the next ones will only be read by the next `read` calls.
* If I enter a size of `-1`, the for loop in `my_fgets` never reaches an end (as `size-- != 0`).
* There is also a [`win` function](https://i.imgur.com/qiLhDby.png) which executes `/bin/cat flag`, it's just not used anywhere. It is at address 0x4005F4, a perfect target to jump to!

I put that all together in a payload, see `exploit.py`.

