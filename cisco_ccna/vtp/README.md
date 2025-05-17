# VTP (VLAN Trunking Protocol)

VTP, Cisco switch'ler arasında VLAN bilgilerinin senkronizasyonunu sağlayan bir protokoldür. VLAN yapılandırmasını merkezi olarak yönetmeyi sağlar.

## VTP'nin Özellikleri
- VLAN bilgilerini senkronize eder
- Merkezi VLAN yönetimi
- Otomatik VLAN dağıtımı
- Yapılandırma tutarlılığı

## VTP Modları
### Server
- VLAN oluşturabilir
- VLAN silebilir
- Değişiklikleri diğer switch'lere iletir
- Varsayılan mod

### Client
- VLAN oluşturamaz
- VLAN silemez
- Server'dan gelen değişiklikleri alır
- Yerel VLAN yapılandırması yapamaz

### Transparent
- Yerel VLAN yapılandırması yapabilir
- VTP mesajlarını iletir
- VTP veritabanını saklamaz
- Bağımsız çalışır

## VTP Yapılandırması
- Domain adı
- Şifre
- Sürüm
- Pruning

## VTP Güvenliği
- VTP şifreleme
- VTP sürüm kontrolü
- VTP domain kontrolü
- VTP pruning 