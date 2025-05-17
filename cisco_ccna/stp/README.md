# STP (Spanning Tree Protocol)

STP, ağdaki döngüleri önlemek ve yedekli bağlantıları yönetmek için kullanılan bir protokoldür. IEEE 802.1D standardına dayanır.

## STP'nin Özellikleri
- Döngü önleme
- Yedekli bağlantı yönetimi
- Otomatik topoloji değişimi
- Yük dengeleme

## STP Port Durumları
### Blocking
- BPDU'ları dinler
- Veri iletmez
- 20 saniye süre

### Listening
- BPDU'ları işler
- Veri iletmez
- 15 saniye süre

### Learning
- MAC adreslerini öğrenir
- Veri iletmez
- 15 saniye süre

### Forwarding
- Veri iletir
- BPDU'ları işler
- Normal çalışma

### Disabled
- Port kapalı
- Hiçbir işlem yapmaz

## STP Bileşenleri
- Root Bridge
- Root Port
- Designated Port
- BPDU
- Port Cost
- Bridge ID 