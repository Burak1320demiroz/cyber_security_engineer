# order+by +1--

### Tanım
- SELECT * FROM products WHERE category = 'Pets';

-------------------------------------

### administrator'--
- ==> SELECT * FROM products WHERE category = 'Pets' ORDER BY 1--';
    - ' → Stringi kapatır.
    - ORDER BY 1 → Sonuçları ilk sütuna göre sıralar.
    - -- → Geri kalan kısmı yorum satırına çevirerek sorgunun orijinal yapısını bozar.

-------------------------------------

### Nasıl Önlenir?
- Parametreli Sorgular (Prepared Statements) Kullanın
- Gelen parametreleri doğrulayın ==> Örneğin, sadece belirli kategorilere izin verin.
- Hata mesajlarını gizleyin ==> Hata döndürmek yerine, 500 Internal Server Error verin.
- Web Application Firewall (WAF) gibi sistemlerle SQL enjeksiyon saldırılarını engelleyin.
