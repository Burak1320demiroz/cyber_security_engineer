# Asymmetric Encryption

##### Asimetrik Şifreleme (Asymmetric Encryption), bir çift anahtar kullanarak veri şifreleyen bir kriptografi yöntemidir. Bu anahtar çifti şunlardan oluşur ==> 
- Genel Anahtar (Public Key): Şifreleme için kullanılır ve herkesle paylaşılabilir.
- Özel Anahtar (Private Key): Şifrelenmiş verinin çözülmesi (decryption) için kullanılır ve gizli tutulmalıdır.

-------------------------------------

##### Asimetrik Şifreleme Nasıl Çalışır?
- Gönderen kişi, alıcının genel anahtarını kullanarak mesajı şifreler.
- Şifrelenmiş mesaj yalnızca alıcının özel anahtarıyla çözülebilir.
- Böylece, şifrelenmiş veri sadece yetkili kişi tarafından okunabilir.

- Bu yöntem özellikle TLS, PGP, SSH, Bitcoin, dijital imzalar ve sertifika sistemleri gibi güvenlik uygulamalarında yaygın olarak kullanılır.

-------------------------------------

- RSA (Rivest–Shamir–Adleman) 
    - 1024 bit → Günümüzde güvensiz kabul ediliyor, kırılabilir.
    - 2048 bit → Standart güvenlik seviyesi (çoğu sistemde kullanılıyor).
    - 3072 bit → Uzun vadede daha güvenli.
    - 4096 bit → En güvenli ancak performansı düşürüyor.
    - NIST (ABD Ulusal Standartlar ve Teknoloji Enstitüsü), 2048 bit ve üstünü öneriyor. 
- ECC (Elliptic Curve Cryptography)
- DSA (Digital Signature Algorithm)
