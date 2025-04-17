# Basic SQL Injection

### Tanım
SQL Enjeksiyonu (SQL Injection), kullanıcıdan alınan verilerin doğrudan SQL sorgusuna dahil edilerek kötü niyetli bir kişinin veritabanına zarar vermesi veya hassas verilere erişmesi işlemidir.

### SQL Enjeksiyonunun Temel Yapısı
Örnek SQL sorgusu:
- `SELECT * FROM products WHERE category = 'Gifts' AND released = 1`

    - **SELECT**: Hangi sütunları seçeceğimizi belirtir. `*` kullanılırsa, tüm sütunlar seçilir.
    - **FROM**: Hangi tablodan veri çekileceğini belirtir. Bu örnekte `products` tablosu.
    - **WHERE**: Belirtilen koşullara uyan satırları filtreler. Bu örnekte:
        - `category = 'Gifts'` → `Gifts` kategorisindeki ürünler.
        - `released = 1` → Yayınlanmış (released = 1) ürünler.
  
    Bu sorgu yalnızca `Gifts` kategorisindeki yayınlanmış ürünleri döndürecektir.

### Basit SQL Enjeksiyon Örnekleri

#### 1. **' OR 1=1--**

Bu tip SQL enjeksiyonu, sorguya eklenen `OR 1=1` ifadesi ile her zaman doğru bir sonuç döndürür. `--` ise SQL'de yorum satırı başlatır ve geriye kalan kısmı geçersiz kılar. Bu tür bir enjeksiyonun örneği:

- Normal Sorgu:
    ```sql
    SELECT * FROM products WHERE category = 'Gifts' AND released = 1;
    ```

- Enjeksiyonlu Sorgu:
    ```sql
    SELECT * FROM products WHERE category = 'Gifts' OR 1=1-- AND released = 1;
    ```
    - **OR 1=1** her zaman doğru olduğu için, sorgu bütün ürünleri döndürür. 
    - **--** ise `AND released = 1` kısmını devre dışı bırakır ve sorgu tam olarak çalıştırılabilir.

Bu tip bir enjeksiyon saldırısı, saldırganın tüm ürünlere erişmesini sağlar.

#### 2. **' OR 1=1; DROP TABLE products; --**

Bu, daha tehlikeli bir saldırıdır. Burada saldırgan, SQL sorgusuna zarar verici bir komut ekler. `DROP TABLE` komutu bir tabloyu veritabanından tamamen siler.

- Normal Sorgu:
    ```sql
    SELECT * FROM products WHERE category = 'Gifts' AND released = 1;
    ```

- Enjeksiyonlu Sorgu:
    ```sql
    SELECT * FROM products WHERE category = '' OR 1=1; DROP TABLE products; --';
    ```
    - **OR 1=1** → Her zaman doğru döner ve bütün verileri döndürür.
    - **DROP TABLE products** → `products` tablosunu tamamen siler.
    - **--** → Sorgunun geri kalan kısmını yorum satırına dönüştürür, böylece diğer komutlar çalışmaz.

Bu saldırı veritabanı üzerinde ciddi zararlar verebilir.

#### 3. **' AND username = 'administrator' --**

Bu tür bir saldırı, kullanıcı adı gibi girdi alanlarında kullanılabilir. Saldırgan, SQL sorgusuna eklediği bir koşulla `administrator` kullanıcısına erişmeye çalışabilir.

- Normal Sorgu:
    ```sql
    SELECT * FROM users WHERE username = 'administrator' AND password = 'password';
    ```

- Enjeksiyonlu Sorgu:
    ```sql
    SELECT * FROM users WHERE username = 'administrator' AND password = 'password' --';
    ```
    - **--** → `password` kontrolünü geçersiz kılar ve şifre kontrolü yapılmadan giriş yapılmasına neden olur.
    - Eğer şifre kontrolü yapılmadan giriş yapılabiliyorsa, saldırgan hesabın şifresini öğrenebilir.

Bu tip SQL enjeksiyonları, özellikle şifre doğrulama işlemleri için kritik güvenlik açıkları yaratır.

-------------------------------------
