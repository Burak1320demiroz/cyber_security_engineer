# Etherchannel

Etherchannel, birden fazla fiziksel bağlantıyı mantıksal olarak tek bir bağlantı gibi kullanmayı sağlayan bir teknolojidir. Bant genişliğini artırır ve yedeklilik sağlar.

## Etherchannel Protokolleri
### PAgP (Port Aggregation Protocol)
- Cisco'ya özel protokol
- İki mod: Auto ve Desirable
- Otomatik yapılandırma
- Dinamik kanal oluşturma

### LACP (Link Aggregation Control Protocol)
- IEEE 802.3ad standardı
- İki mod: Active ve Passive
- Çoklu üretici desteği
- Endüstri standardı

## Etherchannel Modları
### PAgP Modları
- Auto: Pasif bekleme
- Desirable: Aktif istek

### LACP Modları
- Active: Aktif istek
- Passive: Pasif bekleme

## Etherchannel Yapılandırması
- Port kanalı oluşturma
- Protokol seçimi
- Mod belirleme
- Yük dengeleme
- Port ekleme

## Etherchannel Komutları
- channel-group
- channel-protocol
- show etherchannel
- show etherchannel summary
- show etherchannel port-channel 