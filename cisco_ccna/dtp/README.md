# DTP (Dynamic Trunking Protocol)

DTP, Cisco switch'ler arasında trunk bağlantılarını otomatik olarak yapılandırmak için kullanılan bir protokoldür. Portların trunk moduna geçişini dinamik olarak yönetir.

## DTP'nin Özellikleri
- Otomatik trunk yapılandırması
- Sadece Cisco cihazları arasında çalışır
- ISL ve 802.1Q protokollerini destekler
- Varsayılan olarak etkindir

## DTP Modları
### Dynamic Auto
- Pasif bekleme durumu
- Karşı taraf istek gönderirse trunk olur
- Varsayılan mod

### Dynamic Desirable
- Aktif trunk isteği
- Dynamic Auto ve Desirable ile trunk olur
- Trunk oluşturmaya çalışır

### Trunk
- Sabit trunk modu
- DTP mesajları gönderir
- Her zaman trunk olarak çalışır

### Access
- Sabit access modu
- DTP mesajları göndermez
- Trunk oluşturmaz

## DTP Güvenliği
- DTP'yi devre dışı bırakma
- Manuel trunk yapılandırma
- Port güvenliği
- Native VLAN değiştirme 