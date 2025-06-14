# BGP (Border Gateway Protocol)

BGP, internet üzerinde AS'ler (Autonomous Systems) arası yönlendirme yapan bir dış yönlendirme protokolüdür. Path vector protokolü olarak çalışır ve internet omurgasının temel yönlendirme protokolüdür.

## BGP Temel Kavramlar

### Protokol Özellikleri
- Path vector protokolü
- TCP port 179 üzerinden çalışır
- Incremental güncellemeler
- Policy-based routing
- Loop prevention mekanizmaları
- Yüksek ölçeklenebilirlik

### BGP Türleri

#### 1. IBGP (Internal BGP)
- Aynı AS içinde çalışır
- Full mesh topoloji gerektirir
- Route reflector kullanılabilir
- Confederation yapılandırılabilir
- AS içi yönlendirme için kullanılır

#### 2. EBGP (External BGP)
- Farklı AS'ler arası çalışır
- Doğrudan bağlantı gerektirir
- AS path kontrolü yapar
- Route filtering uygulanır
- AS'ler arası yönlendirme için kullanılır

## BGP Bileşenleri ve Özellikleri

### BGP Attributes (Özellikler)
1. **Well-known Mandatory**
   - AS Path: Rota üzerindeki AS'lerin listesi
   - Next Hop: Bir sonraki hop'un IP adresi
   - Origin: Rotanın kaynağı (IGP, EGP, Incomplete)

2. **Well-known Discretionary**
   - Local Preference: AS içi rota seçimi
   - Atomic Aggregate: Rota özetleme bilgisi

3. **Optional Transitive**
   - Community: Rota gruplandırma
   - Aggregator: Özetleme bilgisi

4. **Optional Non-transitive**
   - MED (Multi-Exit Discriminator): AS'ler arası rota seçimi
   - Originator ID: Route reflector bilgisi

### BGP Neighbor States (Komşu Durumları)
1. **Idle**: Başlangıç durumu
2. **Connect**: TCP bağlantısı kuruluyor
3. **Active**: Bağlantı kurma denemesi
4. **OpenSent**: OPEN mesajı gönderildi
5. **OpenConfirm**: OPEN mesajı alındı
6. **Established**: BGP oturumu kuruldu

## BGP Yapılandırma ve Yönetim

### Temel BGP Yapılandırması
```cisco
! BGP router yapılandırması
Router(config)# router bgp 65000
Router(config-router)# bgp router-id 1.1.1.1

! IBGP komşu yapılandırması
Router(config-router)# neighbor 192.168.1.1 remote-as 65000
Router(config-router)# neighbor 192.168.1.1 update-source Loopback0

! EBGP komşu yapılandırması
Router(config-router)# neighbor 10.1.1.2 remote-as 65001
Router(config-router)# neighbor 10.1.1.2 ebgp-multihop 2

! Network tanımlama
Router(config-router)# network 192.168.1.0 mask 255.255.255.0
```

### BGP Route Filtering
```cisco
! Prefix-list oluşturma
Router(config)# ip prefix-list FILTER permit 192.168.0.0/16

! Route-map yapılandırması
Router(config)# route-map SET-LOCAL-PREF permit 10
Router(config-route-map)# set local-preference 200

! Komşuya filtre uygulama
Router(config-router)# neighbor 192.168.1.1 prefix-list FILTER in
Router(config-router)# neighbor 192.168.1.1 route-map SET-LOCAL-PREF in
```

## BGP Best Practices

### 1. Route Reflector Kullanımı
- Full mesh gerekliliğini azaltır
- Ölçeklenebilirliği artırır
- Yapılandırma karmaşıklığını azaltır

### 2. Route Filtering
- Prefix-list kullanımı
- Route-map ile policy uygulama
- AS-path filtreleme
- Community değerleri ile filtreleme

### 3. BGP Security
- MD5 authentication
- TTL security
- Route filtering
- Prefix-list kullanımı

## BGP Sorun Giderme

### Temel Komutlar
```cisco
! BGP durumunu kontrol etme
Router# show ip bgp summary
Router# show ip bgp neighbors

! BGP rotalarını görüntüleme
Router# show ip bgp
Router# show ip bgp 192.168.1.0/24

! BGP debug
Router# debug ip bgp updates
Router# debug ip bgp events
```

### Yaygın Sorunlar
1. BGP komşuluk kurulamıyor
2. Rotalar alınıp gönderilemiyor
3. Policy uygulamaları çalışmıyor
4. Route reflector sorunları

### Sorun Giderme Adımları
1. Komşuluk durumunu kontrol et
2. TCP bağlantısını doğrula
3. Route filtrelerini kontrol et
4. BGP policy'lerini gözden geçir
5. Debug çıktılarını analiz et

## Önemli Notlar
- BGP, internet omurgasının temel protokolüdür
- Policy-based routing için idealdir
- Yüksek ölçeklenebilirlik sunar
- Güvenlik önlemleri önemlidir
- Route filtering kritik öneme sahiptir
- BGP, yavaş yakınsama özelliğine sahiptir
- AS path manipülasyonu ile trafik yönetimi yapılabilir 