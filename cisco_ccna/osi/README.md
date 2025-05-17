# OSI Modeli (Açık Sistemler Bağlantısı)

OSI modeli, ağ iletişimini anlamak ve uygulamak için kullanılan kavramsal bir çerçevedir. Ağ iletişimini, her biri belirli işlevlere ve sorumluluklara sahip yedi farklı katmana böler.

## Yedi Katman

1. **Fiziksel Katman (Katman 1)**
   - Cihazlar arasındaki fiziksel bağlantıyı sağlar
   - Fiziksel ortam üzerinden ham bit akışını iletir
   - Kablolar, konektörler ve ağ arayüz kartlarını içerir

2. **Veri Bağlantı Katmanı (Katman 2)**
   - Veri çerçevelerinin hatasız transferini sağlar
   - Fiziksel adreslemeyi (MAC adresleri) yönetir
   - Anahtarlar ve köprüleri içerir

3. **Ağ Katmanı (Katman 3)**
   - Mantıksal adreslemeyi (IP adresleri) yönetir
   - Farklı ağlar arasında veri yönlendirmesi yapar
   - Yönlendiricileri içerir

4. **Taşıma Katmanı (Katman 4)**
   - Güvenilir veri teslimini sağlar
   - Akış kontrolü ve hata kontrolü yapar
   - TCP ve UDP protokollerini içerir

5. **Oturum Katmanı (Katman 5)**
   - İletişim oturumlarını yönetir
   - Bağlantıları kurar, sürdürür ve sonlandırır

6. **Sunum Katmanı (Katman 6)**
   - Veri biçimlendirme ve şifrelemeyi yönetir
   - Uygulamalar arasında veri çevirisi yapar

7. **Uygulama Katmanı (Katman 7)**
   - Uygulamalara ağ hizmetleri sağlar
   - HTTP, FTP, SMTP gibi protokolleri içerir 