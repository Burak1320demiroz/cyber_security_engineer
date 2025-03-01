# UNION

### Tanım
- SELECT * FROM products WHERE category = 'Pets';

-------------------------------------

### UNION (Oracle)
- ==> SELECT * FROM products WHERE category = 'Pets' UNION SELECT 'abc', 'def' FROM dual--
### UNION (MySQL, MSSQL (Microsoft SQL Server), PostgreSQL, SQLite)
- ==> SELECT * FROM products WHERE category = 'Pets' UNION UNION SELECT 'abc', 'def';

-------------------------------------

### Nasıl Önlenir?
