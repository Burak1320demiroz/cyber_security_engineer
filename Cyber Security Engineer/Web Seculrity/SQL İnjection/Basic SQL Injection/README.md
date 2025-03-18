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