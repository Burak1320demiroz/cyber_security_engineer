# Access control vulnerabilities

PortSwigger Web Security Academy'deki **Erişim Kontrolü** konusuyla ilgili önemli noktalar şunlardır:

**Erişim Kontrolü Nedir?**
Erişim kontrolü, web uygulamalarında kullanıcıların hangi kaynaklara ve işlevlere erişebileceğini belirleyen güvenlik mekanizmalarıdır. Doğru yapılandırılmadığında, kullanıcılar yetkisiz kaynaklara erişebilir veya kritik işlevleri kullanabilirler.

**Erişim Kontrolü Türleri:**
1. **Dikey Erişim Kontrolleri (Vertical Access Controls):**
   Farklı kullanıcı rollerinin farklı yetkilere sahip olmasını sağlar. Örneğin, bir yönetici tüm kullanıcı hesaplarını yönetebilirken, normal bir kullanıcı sadece kendi hesabını yönetebilir.

2. **Yatay Erişim Kontrolleri (Horizontal Access Controls):**
   Aynı yetkiye sahip kullanıcıların kendi verilerine erişimini sağlar. Örneğin, bir banka uygulamasında, kullanıcılar sadece kendi hesaplarındaki işlemleri görüntüleyebilir ve gerçekleştirebilir.

3. **Bağlama Dayalı Erişim Kontrolleri (Context-Dependent Access Controls):**
   Uygulamanın durumu veya kullanıcının etkileşimine bağlı olarak erişimi kısıtlar. Örneğin, bir alışveriş sitesinde, ödeme yapıldıktan sonra sepet içeriğinin değiştirilmesine izin verilmemesi.

