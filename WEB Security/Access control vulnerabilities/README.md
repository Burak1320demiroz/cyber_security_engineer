# Access control vulnerabilities
Erişim Kontrolü, bir sistemde kullanıcıların ya da diğer nesnelerin hangi kaynaklara erişebileceğini belirleyen güvenlik mekanizmalarını ifade eder. Web uygulamalarında, bu genellikle kimlik doğrulama (kullanıcıyı doğrulama) ve oturum yönetimi (kullanıcı oturumunun takibi) ile bağlantılıdır. Ayrıca, erişim denetimi, kullanıcının hangi işlemleri yapabileceğini belirler.

**Dikey Erişim Kontrolleri:**  
Hassas işlevlere erişimi belirli kullanıcı tipleriyle sınırlayan bir mekanizmadır. Örneğin, bir yönetici diğer kullanıcıların hesaplarını değiştirebilirken, normal bir kullanıcı bunu yapamaz.

**Yatay Erişim Kontrolleri:**  
Farklı kullanıcıların, aynı türdeki kaynaklara erişim haklarını belirler. Örneğin, bir bankacılık uygulaması bir kullanıcının kendi hesaplarına erişmesini sağlarken, başka bir kullanıcının hesaplarına erişmesine engel olur.

**Bağlam Bağımlı Erişim Denetimleri:**  
Uygulamanın durumu ya da kullanıcının etkileşimlerine bağlı olarak erişimi kısıtlar. Örneğin, bir kullanıcı alışveriş sepeti içeriğini sadece ödeme yapılmadan değiştirebilir.

**Bozuk Erişim Kontrolleri:**  
Erişim kontrolü mekanizmaları düzgün çalışmadığında ortaya çıkar. Bu, bir kullanıcının yetkisi olmayan kaynaklara erişmesi ya da işlemler yapabilmesi anlamına gelir. Örneğin:
- **Dikey Ayrıcalık Yükseltmesi:** Yönetici olmayan bir kullanıcının yönetici işlevlerine erişmesi.
- **Yatay Ayrıcalık Yükseltmesi:** Bir kullanıcının başkasına ait verilere erişmesi.

-------------------------------------

### **`/admin-roles?username=carlos&action=upgrade`**
   - Bu, bir kullanıcının (`carlos`) admin rolüne yükseltilmesi için yapılan bir istek gibi görünüyor.
   - Eğer bu endpoint doğrulama yapmıyorsa, herhangi bir kullanıcı başka bir kullanıcıyı admin yapabilir.

### **`/robots.txt`**
   - Bu dosya, arama motorlarına hangi sayfaları tarayıp taramayacağını söyler. Bazen geliştiriciler hassas dizinleri burada açıkça belirtir (örneğin `/admin`, `/backup` gibi).
   - Bu dosya incelenerek hassas endpointler keşfedilebilir.

### **Çerez (Cookie) Manipülasyonu (`Admin=false` → `Admin=true`)**
   - Sunucu, kullanıcının admin olup olmadığını kontrol etmek için bir çerez kullanıyor (`Admin=false`).
   - Bu çerezi `Admin=true` olarak değiştirerek yetki yükseltme denemesi yapılıyor.
   - Eğer sunucu bu değeri doğrulamıyorsa, basit bir çerez değişikliğiyle admin yetkileri kazanılabilir.

### **Burp Repeater ile İstek Manipülasyonu**
   - Bir e-posta gönderme isteği yakalanıyor (örneğin bir form submission).
   - Bu istek **Burp Repeater**’a gönderilerek manipüle ediliyor.
   - İstek gövdesindeki JSON’a `"roleid":2` ekleniyor (muhtemelen `2`, admin rolünün ID’si).
   - Eğer sunucu rol değişikliğini doğrulamıyorsa, bu şekilde yetki yükseltilebilir.

### **API Anahtarı**
   - Bazı API’ler, yetkilendirme için bir API anahtarı kullanır.
   - Eğer bu anahtar ele geçirilirse (örneğin bir JavaScript dosyasında veya bir istekte), yetkisiz API çağrıları yapılabilir.

### **`X-Original-URL: /invalid`**
   - Bu header, bazen uygulamanın orijinal URL’ini override etmek için kullanılır.
   - Örneğin, bir WAF (Web Application Firewall) veya reverse proxy, bu header’a bakarak routing yapıyor olabilir.
   - `/invalid` gibi geçersiz bir URL verilerek uygulamanın hata mesajlarından bilgi toplanabilir veya bypass denemeleri yapılabilir.