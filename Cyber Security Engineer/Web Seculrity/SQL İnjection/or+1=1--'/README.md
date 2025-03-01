# or+1=1--'

### Tanım
- SELECT * FROM products WHERE category = 'Gifts' AND released = 1
    - SELECT: Hangi sütunları seçeceğimizi belirtir. * kullanılırsa, tüm sütunlar seçilir.
    - FROM: Hangi tablodan veri çekileceğini belirtir.
    - WHERE: Belirtilen koşullara uyan satırları filtreler.
    - products tablosundan (FROM products), category sütunu 'Gifts' olan (WHERE category = 'Gifts'), ve released sütunu 1 olan (AND released = 1), tüm sütunları (*) seçer.

-------------------------------------

### OR+1=1--'
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

### Nasıl Önlenir?
- Güvenli Sorgu Kullanımı ==> !! Bunu önlemek için hazırlıklı sorgular (prepared statements) kullanmalıyız !!
- Girdi Doğrulaması Yap (Input Validation) ==> Kullanıcıdan sadece beklenen değerleri al. 
    - kategori girişini sadece "Gifts", "Electronics", "Books" ile sınırla.
- DROP TABLE Yetkisini Kısıtla ==> 
    - Web uygulamasının bağlandığı veritabanı kullanıcısına sadece SELECT, INSERT, UPDATE yetkisi verilsin. 
    - DROP TABLE ve DELETE FROM gibi kritik komutları çalıştırma yetkisi olmasın.