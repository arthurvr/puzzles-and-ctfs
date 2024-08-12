# Extended basics 6

Setting `$user` or `$pass` doesn't matter, as `isAuthed()` always returns false anyway. I think you can set `$passed` immediately using the `$_GET` variables.

So I submitted `http://moo.com/moo.php?passed=true`, which worked.