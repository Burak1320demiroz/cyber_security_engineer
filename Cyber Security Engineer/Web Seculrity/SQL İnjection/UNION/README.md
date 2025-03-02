# UNION

### Tanım
- SELECT * FROM products WHERE category = 'Pets';

-------------------------------------

### order+by +1--
- ==> SELECT * FROM products WHERE category = 'Pets' ORDER BY 1--';
    - ' → Stringi kapatır.
    - ORDER BY 1 → Sonuçları ilk sütuna göre sıralar. 
        - 1,2,3,... hata alana kadar yaz sütün sayısını öğren.
    - -- → Geri kalan kısmı yorum satırına çevirerek sorgunun orijinal yapısını bozar.

-------------------------------------

### UNION (Oracle)
- ==> SELECT * FROM products WHERE category = 'Pets' UNION SELECT 'abc', 'def' FROM dual--
### UNION (MySQL, MSSQL (Microsoft SQL Server), PostgreSQL, SQLite)
- ==> SELECT * FROM products WHERE category = 'Pets' UNION UNION SELECT 'abc', 'def';

-------------------------------------

### Nasıl Önlenir?
- Parametreli Sorgular (Prepared Statements) Kullanın
- Gelen parametreleri doğrulayın ==> Örneğin, sadece belirli kategorilere izin verin.
- Hata mesajlarını gizleyin ==> Hata döndürmek yerine, 500 Internal Server Error verin.
- Web Application Firewall (WAF) gibi sistemlerle SQL enjeksiyon saldırılarını engelleyin.
