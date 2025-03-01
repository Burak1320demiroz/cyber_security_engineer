# administrator'--

### Tanım
- SELECT * FROM users WHERE username = 'giris' AND password = 'sifre';

-------------------------------------

### administrator'--
- ==> SELECT * FROM users WHERE username = 'administrator'--' AND password = 'sifre';
    - -- SQL'de yorum satırı başlatır, yani AND password = 'sifre' kısmı çalışmaz.
    - Eğer "administrator" kullanıcısının şifresi kontrol edilmeden giriş yapılıyorsa, Zafiyettir.

-------------------------------------

### Nasıl Önlenir?
- Parametreli Sorgular (Prepared Statements) Kullanın
- Özel karakterleri engelleyin veya kaçış karakterleri (\) kullanın.
- Şifreleri hashleyin (bcrypt, argon2 gibi algoritmalarla).
- Web Application Firewall (WAF) gibi sistemlerle SQL enjeksiyon saldırılarını engelleyin.
