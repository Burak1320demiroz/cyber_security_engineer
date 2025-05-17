# NTP (Network Time Protocol)

NTP, ağ cihazlarının saatlerini senkronize etmek için kullanılan bir protokoldür. Tüm cihazların aynı zamanı göstermesini sağlar.

## NTP'nin Özellikleri
- Hassas zaman senkronizasyonu
- Hiyerarşik yapı
- UTC zaman standardı
- Otomatik zaman ayarı

## NTP Katmanları
### Stratum 0
- Atomik saatler
- GPS saatleri
- En hassas zaman kaynağı

### Stratum 1
- Birincil sunucular
- Stratum 0'a doğrudan bağlı
- Referans zaman sunucuları

### Stratum 2-15
- İkincil sunucular
- Üst katmandan zaman alır
- Diğer cihazlara zaman dağıtır

## NTP Yapılandırması
- NTP sunucu tanımı
- NTP istemci yapılandırması
- NTP kimlik doğrulama
- NTP erişim kontrolü

## NTP Komutları
- ntp server
- ntp peer
- show ntp status
- show ntp associations
- debug ntp 