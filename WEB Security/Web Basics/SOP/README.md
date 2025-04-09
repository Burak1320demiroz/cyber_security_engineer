# SOP (Same Origin Policy)

###### Tanım
- Tarayıcıların uyguladığı temel bir güvenlik mekanizmasıdır.
- SOP, tarayıcılar (browser) tarafından yüklenen kaynaklarının, birbirleriyle olan paylaşımlarını/ilişkilerini belirli kurallar çerçevesinde kısıtlayan bir politikadır.
- Farklı origin’e sahip kaynaklar birbirlerinin DOM’larına erişemez yani dönen cevabı okuyamaz!
- SOP politikasına göre, yüklenen her bir kaynak; 3 bilginin birleşimi ile origin olarak tanımlanmaktadır.
    - ORIGIN
        - Şema/Protokol
        - Domain
        - Port (Bağlantı Noktası)

-------------------------------------

###### Örnek olarak,
- https://test.com/ornek/index.html
- Şema/Protokol: https
- Domain: test.com
- Port: 443