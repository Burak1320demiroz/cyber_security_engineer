# Server-Side Request Forgery (Sunucu Tarafı İstek Sahteciliği)

**1. Yerel sunucuya karşı Temel SSRF (Server-Side Request Forgery)**  
🔹 Hedef uygulama, kendi iç ağındaki (localhost, 127.0.0.1) servislerle iletişim kurmak üzere kandırılır.

**2. Başka bir arka uç sistemine karşı Temel SSRF**  
🔹 Sunucu, dış veya iç ağda başka bir hizmete (örneğin bir API, veri tabanı) istek göndermesi için kandırılır.

**3. Kör SSRF (Blind SSRF)**  
🔹 İsteğe ait yanıt kullanıcıya dönmez; ancak saldırgan gönderilen isteğin etkisini dolaylı yollarla (örneğin DNS, log'lar) gözlemler.

**4. Bant dışı algılama (Out-of-Band Detection)**  
🔹 SSRF gibi zafiyetlerin doğrulanması için doğrudan yanıt yerine, DNS sorguları ya da HTTP istekleri gibi dış kanallardan gelen sinyaller kullanılır.

**5. Kara liste tabanlı giriş filtresi ile SSRF**  
🔹 Uygulama, belirli IP veya domain'leri engellemek için kara liste kullanır; ancak bu filtreler genellikle atlatılabilir.

**6. Gizlenmiş dosya uzantısı aracılığıyla web kabuğu yükleme**  
🔹 Web kabukları, zararsız gibi görünen dosya uzantılarıyla (.jpg.php, .phtml) yüklenerek arka kapı sağlanabilir.

**7. Shellshock istismarı ile Kör SSRF**  
🔹 SSRF kullanılarak iç ağdaki bir Bash ortamına kötü amaçlı environment değişkenleri gönderilir ve komut çalıştırılır (örneğin CGI script'leri).

**8. Beyaz liste tabanlı giriş filtresi ile SSRF**  
🔹 Uygulama sadece izin verilen domain'lere istek gönderir; ancak DNS spoofing, redirect veya URL encoding ile bu filtre atlatılabilir.
