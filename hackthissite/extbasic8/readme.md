# Extended Basics 8

This is the given program:

```perl
#!/usr/bin/perl
 
chomp(my $User = `/usr/bin/whoami`);
 
print "Checking your access level...\n";
 
if ($User == 'BillGates')
{
    print "Authorized! Here are the company records:\n" . `cat /home/BillGates/CompanyRecords.db`;
    die("Closing...\n");
}
 
die("You're not authorized!\n");
```

The if-check doesn't check what the author thinks it does. The operator `==` in perl checks if two values are numerically equal. What we need is a check if they are *"stringwise"* equal, using the `eq` operator. So the line we need is:

```perl
if ($User eq 'BillGates')
```