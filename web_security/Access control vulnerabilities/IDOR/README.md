# IDOR (Insecure Direct Object Reference)
**Güvenli Olmayan Doğrudan Nesne Referansları (IDOR) Nedir?**

IDOR, bir uygulamanın **doğrudan nesne referanslarını** (veritabanı ID'leri, dosya adları, API parametreleri) kontrol etmeden kullanıcıya göstermesi ve bu referansların manipüle edilerek yetkisiz verilere erişilmesine yol açan bir güvenlik açığıdır. 

Güvenli olmayan doğrudan nesne referansları (IDOR), bir web uygulamasında kullanıcı tarafından sağlanan girdilerin, uygulamanın içindeki nesnelere doğrudan erişim sağlamak için kullanılması sonucu ortaya çıkan bir güvenlik açığı türüdür. IDOR, bir erişim denetimi hatasından kaynaklanır ve genellikle yatay ayrıcalık yükseltmesiyle ilişkilidir. Ancak, dikey ayrıcalık yükseltmesi de mümkün olabilir.

-------------------------------------

### **Veritabanı Nesnelerine Doğrudan Referans**

Bir web sitesi, müşteri hesap sayfasına erişmek için şu şekilde bir URL kullanabilir:
```
https://insecure-website.com/customer_account?customer_number=132355
```
Burada, `customer_number` parametresi, arka uç veritabanından müşteri bilgilerini almak için kullanılır. Ancak, bu parametre doğrulama yapılmadan kullanıcı tarafından değiştirilebilir. Saldırgan, `customer_number` parametresinin değerini değiştirerek, başka bir müşterinin hesabına erişebilir. Bu, **yatay ayrıcalık yükseltmesi** (aynı seviyedeki bir başka kullanıcıya erişim) sağlar.

### **Statik Dosyalara Doğrudan Referans**

Bir web sitesi, kullanıcı sohbet mesajlarını bir dosya adıyla kaydedebilir ve kullanıcılara bu dosyaları erişebilmeleri için URL sağlar. Örneğin:
```
https://insecure-website.com/static/12144.txt
```
Burada, dosya adı sabit bir formatta olabilir ve bir kullanıcı bu URL'yi değiştirerek başka bir kullanıcıya ait sohbet mesajlarına erişebilir. Eğer bu dosyalar hassas veriler içeriyorsa (örneğin, kullanıcı kimlik bilgileri), saldırgan bu dosyayı değiştirerek başkasının verilerine ulaşabilir.
 
### **Kullanıcı Profil ID'si ile Yetkisiz Erişim (Yatay Ayrıcalık Yükseltme)**
- **Örnek Senaryo:**  
  Bir web sitesinde kullanıcı profilleri şu şekilde erişilebilir:  
  ```
  https://example.com/user/profile?id=123
  ```
  - Normalde kullanıcı sadece kendi profilini (`id=123`) görebilmelidir.  
  - Ancak, `id=124` yapılarak başka bir kullanıcının bilgileri görüntülenebilir.  
  - **Risk:** Kişisel veri sızıntısı (e-posta, adres, kredi kartı bilgileri).  

### **Dosya İndirme Sisteminde Tahmin Edilebilir Dosya Yolları**
- **Örnek Senaryo:**  
  Bir şirket içi portal, çalışan maaş bordrolarını şu şekilde saklıyor:  
  ```
  https://company.com/download/payroll?file=2023_employee123_salary.pdf
  ```
  - Saldırgan, `employee123` yerine `employee124` yazarak başka bir çalışanın maaş bilgilerini indirebilir.  
  - **Risk:** Hassas belgelerin sızması.  

### **API'da Rol ID Manipülasyonu (Dikey Ayrıcalık Yükseltme)**
- **Örnek Senaryo:**  
  Bir kullanıcı, kendi profilini güncellemek için şu API isteğini gönderiyor:  
  ```json
  PATCH /api/user/update
  {
    "user_id": 100,
    "role_id": 1  // Normal kullanıcı rolü
  }
  ```
  - Saldırgan, `role_id: 1` yerine `role_id: 5` (admin rolü) yaparak kendisini admin yapabilir.  
  - **Risk:** Yetkisiz yönetici erişimi.  

### **Sipariş ID'si ile Başka Kullanıcının Siparişine Erişim**
- **Örnek Senaryo:**  
  Bir e-ticaret sitesinde sipariş detayları:  
  ```
  https://shop.com/order/details?order_id=5001
  ```
  - Kullanıcı, `order_id=5001` yerine `order_id=5002` yaparak başkasının siparişini görüntüleyebilir.  
  - **Risk:** Adres, ürün ve ödeme bilgilerinin çalınması.  

### **PDF Raporlarında IDOR**
- **Örnek Senaryo:**  
  Bir banka, müşteri ekstrelerini şu şekilde sunuyor:  
  ```
  https://bank.com/statements/download?account=998877&year=2023
  ```
  - Saldırgan, `account=998877` yerine başka bir hesap numarası yazarak başkasının ekstresini indirebilir.  
  - **Risk:** Finansal dolandırıcılık.  

