# SSL-TLS 

- SSL (Secure Sockets Layer): Güvenli Yuva Katmanı
- TLS (Transport Layer Security): Taşıma Katmanı Güvenliği

- Not = TLS, SSL'in daha güvenli ve geliştirilmiş bir sürümüdür. Günümüzde SSL yerine TLS kullanılır, çünkü SSL'in eski sürümleri güvenlik açıkları nedeniyle artık önerilmemektedir.

- El Sıkışma (Handshake) : Bu işlem, istemci ve sunucu arasında güvenli bir bağlantı kurmak için gerekli olan parametrelerin değiştirildiği bir süreçtir.
    - İstemci (genellikle web tarayıcısı) sunucuya bağlanır ve SSL/TLS bağlantısını başlatır.
    - Sunucu, dijital sertifikasını (public key) istemciye gönderir. Bu sertifika, sunucunun kimliğini doğrulamak ve güvenilir bir sertifika otoritesine ait olduğunu belgelemek için kullanılır.
    - İstemci, sunucunun sertifikasını doğrular. Eğer sertifika geçerli ve doğrulanmışsa, istemci sunucunun kimliğine güvenebilir ve iletişimi devam ettirir.
    - İstemci, sunucuya göndermek için bir oturum anahtarı oluşturur ve sunucunun açık anahtarı ile şifreler. Bu şifrelenmiş veri, sunucu tarafından özel anahtar ile çözülebilir.
    - Sunucu, istemciden aldığı şifrelenmiş oturum anahtarını çözer ve kendi oturum anahtarını oluşturur.

- Veri Şifreleme ve İletimi : Handshake işlemi tamamlandıktan sonra, istemci ve sunucu artık bir simetrik anahtarı (oturum anahtarı) kullanarak verileri şifreleyip çözebilirler.

- Veri Bütünlüğü Kontrolü : SSL/TLS, veri bütünlüğünü sağlamak için hash algoritmalarını kullanır. Gönderen tarafından hesaplanan bir hash değeri, alıcı tarafından alınan verilerin bütünlüğünü doğrulamak için kullanılır. Eğer veriler transfer sırasında değiştirildiyse, alıcı tarafından hesaplanan hash değeri gönderilen hash değeriyle uyuşmayacaktır, bu durumda veriler güvenilmez kabul edilir ve iletişim kesilir.

-------------------------------------

- 1️⃣ İlk aşamada asimetrik şifreleme (RSA, Diffie-Hellman) ile gizli bir anahtar değişimi yapılır.
- 2️⃣ Sonrasında, simetrik şifreleme (AES, ChaCha20) ile veriler korunur.
- 3️⃣ Bütünlük kontrolü için karma fonksiyonları (HMAC, SHA-256) kullanılır.

-------------------------------------

![...](/Cyber Security Engineer/Cryptography/Public_Key_Infrastructure/SSL-TLS/image/2.png)
![...](Cyber Security Engineer/Cryptography/Public_Key_Infrastructure/SSL-TLS//image/1.png)
