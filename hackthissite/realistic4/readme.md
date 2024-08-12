# Realistic missions: level 4

The `category` URL parameter of the products page is vulnerable to SQL injection. We could do this manually, but I chose to use [sqlmap](https://github.com/sqlmapproject/sqlmap) to exploit the vulnerability. We simply have to dump everything in the `emails` table.
