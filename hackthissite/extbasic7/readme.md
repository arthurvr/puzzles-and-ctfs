# Extended basics 7

This is the given code:

```php
<?php
        if (!empty($_POST['data']))
        {
                $data = mysql_real_escape_string($_POST['data']);
                mysql_query("INSERT INTO tbl_data (data) VALUES ('$data')");
        }
?>
<form name="grezvahfvfnjuvavatovgpu" action="<?=$_SERVER['PHP_SELF']?>" method="get">
        <input type="text" name="data" />
        <input type="submit" />
</form>
```

The statement within `<?= ... ?>` makes the page vulnerable to cross-site scripting. Wrapping the variable in a call to `htmlspecialchars` would fix this.

```php
<form name="grezvahfvfnjuvavatovgpu" action="<?=htmlspecialchars($_SERVER['PHP_SELF'])?>" method="get">
```

This doesn't pass yet... But I think there is another mistake. Using `get` as method here seems strange, I think that should be `post`.

```php
<form name="grezvahfvfnjuvavatovgpu" action="<?=htmlspecialchars($_SERVER['PHP_SELF'])?>" method="post">
```