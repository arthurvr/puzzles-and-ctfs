# Extended basics 13

The given program: 

```php
<?php
        if (isset($_GET['name']) && isset($_GET['email'])) {
                $user = mysql_real_escape_string($_GET['name']);
                $email = mysql_real_escape_string($_GET['email']);
                $result= mysql_fetch_assoc(mysql_query("SELECT `email` FROM `members` WHERE name = '$user'"));
                $reply = false;
                if ($email == $result['email'])
                {
                        $reply = true;
                }
        } else {
                $reply = false;
        }
        echo ($reply) ? 1 : 0;
?>
```

Think about what would happen if we pass two empty inputs: an empty `name` and an empty `email`. The `$user` will become `""` and the query will return false (as there are no results). That makes `$email == $result['email']` true, because in PHP `"" == false`.

So the input `vrfy.php?email=&name=` works.