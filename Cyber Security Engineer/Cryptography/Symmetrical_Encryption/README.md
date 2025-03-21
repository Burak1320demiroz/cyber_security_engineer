# Symmetrical Encryption

### Aynı anahtar, hem şifreleme hem de şifre çözme işlemleri için kullanılır.

- Hızlıdır: Asimetrik şifrelemeye göre daha hızlı çalışır.
- Tek Anahtar Kullanılır: Veriyi şifrelemek ve çözmek için aynı anahtar gerekir.
- Güvenli Anahtar Paylaşımı Zorunludur: Anahtarın güvenli bir şekilde paylaşılması gerekir.
- Blok ve Akış Şifreleri Vardır: Blok şifreleri veriyi belirli boyutlarda işlerken, akış şifreleri veriyi bit/byte bazlı işler.

-------------------------------------

- AES (Advanced Encryption Standard) (Gelişmiş Şifreleme Standardı)
    - AES-128 ==> 128 bit anahtar
    - AES-192 ==> 192 bit anahtar
    - AES-256 ==> 256 bit anahtar

- DES (Data Encryption Standard) (Veri Şifreleme Standardı) !Günümüzde zayıf kabul edilir!
    - 56 bit anahtar uzunluğu kullanır.

- 3DES (Triple DES) → Daha güvenli ama yavaş, yerine AES kullanılır.
- Blowfish / Twofish → AES’e alternatif, esnek yapıya sahip.
- RC4 → Akış şifreleme algoritması, artık önerilmiyor.

-------------------------------------

- Dosya ve disk şifreleme (BitLocker, VeraCrypt), VPN bağlantıları (IPsec, SSL/TLS), Kablosuz ağ güvenliği (WPA2, WPA3), Veri tabanı şifreleme kullanılır.
