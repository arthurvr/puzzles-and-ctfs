# Realistic missions: level 8

I start by creating a sample account: `davidrp` - `ddd888`. It seems to store the password as an MD5 hash: `4b8fc8f04b932c76948b1e6563f7b671`.

## 1. Find the username of Gary Hunter

There a simple SQL injection in the search field, which we easily discover by entering `' or '1'='1` in the search field. The username of Gary Hunter seems to be `GaryWilliamHunter`.

## 2. Move the money

We first change the `accountUsername` cookie. Then we can send a request to the `movemoney.php` page, with the following data:

```
TO=dropCash&AMOUNT=10000000
```

## 3. Remove the logs

Removing the logs is possible using `cleardir.php` where we set the `dir` value to `logFiles`.
