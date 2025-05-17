# GRE (Generic Routing Encapsulation)

GRE, farklı protokolleri IP ağıları üzerinden tünellemek için kullanılan bir protokoldür. Çeşitli ağ protokollerini IP paketleri içinde taşır.

## GRE'nin Özellikleri
- Çoklu protokol desteği
- IP tünelleme
- Basit yapılandırma
- Düşük overhead

## GRE Kullanım Alanları
### VPN Tünelleri
- Site-to-site VPN
- Remote access
- Güvenli iletişim
- Özel ağ bağlantısı

### Protokol Tünelleme
- IPv6 over IPv4
- IPX over IP
- AppleTalk
- Legacy protokoller

## GRE Başlık Yapısı
- Flags
- Version
- Protocol Type
- Checksum
- Key
- Sequence Number
- Routing

## GRE Yapılandırması
- Tunnel interface
- Source IP
- Destination IP
- Tunnel mode
- Keepalive
- MTU ayarları

## GRE Komutları
- interface tunnel
- tunnel mode gre
- tunnel source
- tunnel destination
- show interface tunnel
- debug tunnel
- show ip interface tunnel 