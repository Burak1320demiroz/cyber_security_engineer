# **Authentication Vulnerabilities (Kimlik Doğrulama Güvenlik Açıkları)**

Kimlik doğrulama zafiyetleri, bir uygulamanın kimlik doğrulama mekanizmalarındaki güvenlik açıklarını ifade eder. Bu açıklar, kötü niyetli kişilerin sistemdeki kullanıcı hesaplarına yetkisiz erişim sağlamak için kullanılabilir. Aşağıda kimlik doğrulama zafiyetlerinin çeşitli türleri ve bunlarla nasıl başa çıkılabileceği detaylı bir şekilde açıklanmıştır.

## **Basic Authentication (Temel Kimlik Doğrulama)**

**Tanım:**  
Temel Kimlik Doğrulama, kullanıcı adı ve şifreyi HTTP isteği içerisinde gönderen basit bir kimlik doğrulama yöntemidir. Kullanıcı adı ve şifre Base64 ile kodlanarak "Authorization" başlığında sunucuya iletilir.

**Güvenlik Sorunu:**  
Bu yöntem güvenli değildir çünkü şifreler yalnızca Base64 ile kodlanır ve şifreleme yapılmaz. Bu nedenle, yalnızca HTTPS gibi güvenli bağlantılarla kullanılmalıdır. Temel kimlik doğrulama, düşük güvenlik gereksinimlerine sahip uygulamalar için uygun olsa da, şifrelerin sürekli açıkta olması nedeniyle yüksek güvenlik gereksinimlerine sahip sistemlerde önerilmez.

## **İki Faktörlü Kimlik Doğrulama (2FA)**

**Tanım:**  
İki faktörlü kimlik doğrulama, kullanıcı adı ve şifre ile giriş yapıldıktan sonra ek bir doğrulama kodunun (genellikle SMS veya bir uygulama üzerinden gönderilen) gerekliliğini sağlar.

**Güvenlik Sorunu:**  
2FA, yalnızca şifrelerle yapılan saldırıları engellese de, zaman zaman 2FA kodlarının brute-force edilmesi mümkün olabilir. Bu tür saldırılar, 2FA'nın zayıf yönlerini hedef alır.

**Saldırı Örneği:**  
Bir saldırgan, kullanıcı adı ve şifresine sahip olduktan sonra 2FA kodlarını brute-force yöntemiyle tahmin etmeye çalışabilir.

## **Broken Logic (Bozuk Mantık)**

**Tanım:**  
Bozuk mantık, uygulamalarda iş akışlarının hatalı bir şekilde işlenmesidir. Şifre sıfırlama işlemlerinde, örneğin token doğrulaması yapılmadığında, bu tür bir hata güvenlik açığına yol açabilir.

**Güvenlik Sorunu:**  
Eksik doğrulama veya yanlış mantık, kullanıcıların şifre sıfırlama işlemlerini başlatmalarına olanak tanır. Bu tür güvenlik açıkları, sistemin yanlış yapılandırılmasından kaynaklanır.

## **Şifre Sıfırlama Token'ı (temp-forgot-password-token)**

**Tanım:**  
Şifre sıfırlama işlemi sırasında kullanılan token, sistemin kimlik doğrulama mekanizmasında eksik kontrol edilirse, saldırganlar şifre sıfırlama işlemini gerçekleştirebilir.

**Güvenlik Sorunu:**  
Token’ın URL’de ve istek gövdesinde silinmesi durumunda bile, şifre sıfırlama işlemi yapılabiliyor. Bu da kötü niyetli kişilerin bu açığı kullanarak parolaları sıfırlamalarına yol açabilir.

## **Kullanıcı Adı Numaralandırması (Username Enumeration) via Response Timing**

**Tanım:**  
Yanıt sürelerindeki farklılıklar kullanılarak, geçerli bir kullanıcı adı tespit edilebilir. Geçersiz kullanıcı adı denemelerinde yanıt süresi sabitken, geçerli bir kullanıcı adı kullanıldığında yanıt süresi değişir.

**Güvenlik Sorunu:**  
Kullanıcı adları, doğru ya da yanlış olduklarına göre farklı zamanlarda yanıt dönebilir. Bu da saldırganların geçerli bir kullanıcı adı tespit etmelerine yol açar.

## **X-Forwarded-For Başlığı**

**Tanım:**  
X-Forwarded-For başlığı, istemcinin gerçek IP adresini saklamak için kullanılır. Bu başlık, IP tabanlı brute-force korumasını aşmak amacıyla manipüle edilebilir.

**Güvenlik Sorunu:**  
X-Forwarded-For başlığının doğru şekilde kontrol edilmemesi, saldırganların proxy sunucusu üzerinden şüpheli istekleri gizlemelerini sağlayarak, brute-force saldırılarına karşı savunmasız kalmalarına neden olabilir.

## **Pitchfork Attack**

**Tanım:**  
Pitchfork saldırısı, her iki parametre (kullanıcı adı ve şifre) için listelerin oluşturulup kombinasyonların denenmesidir. Bu saldırı türü, her iki parametreyi hedef alır.

**Güvenlik Sorunu:**  
Bu tür saldırılarda, her iki parametre de denenerek doğru kombinasyon bulunmaya çalışılır. Şifreleme ve karmaşık doğrulama yöntemleri kullanılarak bu tür saldırılar engellenebilir.

## **Resource Pool Ayarları**

**Tanım:**  
IP engellemeyi aşmak amacıyla, her seferinde yalnızca bir istek gönderilmesini sağlayan bir güvenlik özelliğidir. Bu, saldırıların izini kaybettirir.

**Güvenlik Sorunu:**  
Birden fazla istek göndermeyi engelleyen bu mekanizmalar, IP engellemelerini aşmak amacıyla kullanılır. Güçlü rate limiting ve zamanlama kontrolleri ile bu saldırı türü engellenebilir.

## **Cluster Bomb Attack**

**Tanım:**  
Cluster Bomb saldırısı, her kullanıcı adı için birden fazla şifre kombinasyonu denemek amacıyla yapılan saldırıdır. Her kullanıcı adı için farklı şifre kombinasyonları denenir.

**Güvenlik Sorunu:**  
Bu saldırı, çok sayıda şifre kombinasyonunu denemeyi amaçladığı için sistem kaynaklarını zorlayabilir. İyi yapılandırılmış rate limiting ve CAPTCHA gibi güvenlik önlemleriyle engellenebilir.

## **Grep Extraction Kuralı**

**Tanım:**  
Grep Extraction, hata mesajlarını analiz ederek doğru şifreyi tespit etmeye yarayan bir tekniktir. Yanıtlar arasında "Incorrect password" gibi mesajlar aranır.

**Güvenlik Sorunu:**  
Sistem, hatalı şifre girişlerinde çok fazla bilgi verirse, saldırganlar bu mesajlardan doğru şifreyi çıkarabilir. Bu nedenle, hata mesajlarının içeriklerinin sınırlı olması gereklidir.
