# PPoE (Point-to-Point over Ethernet)

PPoE, Ethernet ağları üzerinden PPP bağlantısı kurmayı sağlayan bir protokoldür. DSL ve kablolu internet bağlantılarında yaygın olarak kullanılır.

## PPoE'nin Özellikleri
- Ethernet üzerinde PPP
- Kimlik doğrulama
- Şifreleme
- Oturum yönetimi

## PPoE Bileşenleri
### PPoE Client
- İstemci tarafı
- Bağlantı başlatma
- Kimlik doğrulama
- Oturum yönetimi

### PPoE Server
- Sunucu tarafı
- Bağlantı kabul
- Kimlik doğrulama
- Kaynak yönetimi

## PPoE Oturum Aşamaları
### Discovery
- PADI (Initiation)
- PADO (Offer)
- PADR (Request)
- PADS (Session)

### Session
- PPP bağlantısı
- LCP müzakere
- Authentication
- NCP müzakere

## PPoE Yapılandırması
- Virtual Template
- BBA Group
- Authentication
- Interface yapılandırması
- QoS ayarları

## PPoE Komutları
- interface virtual-template
- bba-group pppoe
- pppoe enable
- show pppoe session
- debug pppoe
- show pppoe 