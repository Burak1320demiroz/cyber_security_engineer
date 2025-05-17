# NAT (Network Address Translation)

NAT, özel IP adreslerini genel IP adreslerine çeviren bir ağ protokolüdür. IPv4 adres kıtlığı sorununu çözmek ve ağ güvenliğini artırmak için kullanılır.

## NAT Türleri
### Statik NAT
- 1:1 eşleştirme
- Sabit IP adresi dönüşümü
- Sunucular için kullanılır
- Dışarıdan erişilebilir

### Dinamik NAT
- IP havuzu kullanır
- Otomatik adres ataması
- İç ağ cihazları için
- Kullanılabilir adresler sınırlı

### PAT (Port Address Translation)
- Tek IP ile çoklu bağlantı
- Port numaraları kullanır
- En yaygın NAT türü
- Ev ve küçük ofis ağları

## NAT Yapılandırma
- İç ve dış arayüzler
- ACL tanımları
- IP havuzu oluşturma
- Dönüşüm kuralları

## NAT Komutları
- ip nat inside source
- ip nat outside source
- show ip nat translations
- show ip nat statistics
- clear ip nat translation 