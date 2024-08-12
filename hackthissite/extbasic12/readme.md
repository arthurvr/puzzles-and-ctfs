# Extended basic 12

```php
<?php
        $password = 'IWantToCow';
        foreach ($_GET as $key => $value)
        {
          $$key = $value;
        }
        if ($userpass == $password)
        {
                ok();
        }
        else
        {
                echo "&lt;form&gt;&lt;input type='text' name='usertext' /&gt;&lt;input type='submit'&gt;&lt;form&gt;";
        }
?>
```

You can not only control `$userpass` this way, but also `$password`:

```
http://moo.com?userpass=a&password=a
```