# Hash_Function
##### Hash fonksiyonu, girdiyi (veriyi) alıp sabit uzunlukta bir çıktıya (hash değeri) dönüştüren matematiksel bir fonksiyondur.

- Deterministik Olmalı: Aynı giriş her zaman aynı çıkışı üretmelidir.
- Hızlı Çalışmalı: Büyük veri setleri için verimli olmalıdır.
- Çıktı Sabit Uzunlukta Olmalı: Giriş ne kadar büyük olursa olsun, çıktı belirlenen uzunluktadır.
- Çarpışma Direnci: Farklı girdilerin aynı hash değerini üretme olasılığı çok düşük olmalıdır.
- Özetleme (Avalanche Effect): Girdide küçük bir değişiklik büyük bir değişikliğe yol açmalıdır.
- Tersine Çevrilemezlik: Hash değerinden orijinal veriye ulaşmak pratik olarak imkansız olmalıdır.

- Kullanım alanları: Şifreleme, veri bütünlüğü kontrolü, dijital imzalar, blok zincirleri (örn: Bitcoin - SHA-256).

-------------------------------------

- MD5 (Message Digest 5) ==> Artık güvenli değil.
- SHA-1 (Secure Hash Algorithm 1) ==> Kırıldı, önerilmez.
- SHA-256 / SHA-512 ==> Güvenli ve yaygın kullanılanlar.
- BLAKE2, BLAKE3 ==> Daha hızlı ve güvenli alternatifler.
- Argon2, bcrypt, scrypt ==> Şifre saklama için uygun.
- BHA-1 (SHA-1 üstünde kendimce değişiklik yaptım)