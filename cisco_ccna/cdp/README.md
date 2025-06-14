# CDP (Cisco Discovery Protocol)

CDP, Cisco cihazlarının birbirlerini otomatik olarak keşfetmesini ve ağ topolojisini oluşturmasını sağlayan katman 2 protokolüdür. Ağ yönetimi ve sorun giderme için önemli bir araçtır.

## CDP Temel Kavramlar

### Protokol Özellikleri
- Katman 2 (Data Link) protokolü
- Sadece Cisco cihazları arasında çalışır
- Varsayılan olarak etkindir
- Her 60 saniyede bir yayın yapar
- Multicast MAC adresi: 01:00:0C:CC:CC:CC
- TTL (Time To Live): 180 saniye

### CDP Versiyonları
1. **CDPv1**
   - Temel cihaz bilgileri
   - Sınırlı yetenek bilgisi
   - Eski cihazlarda kullanılır

2. **CDPv2**
   - Genişletilmiş cihaz bilgileri
   - Detaylı yetenek bilgisi
   - Modern cihazlarda kullanılır

## CDP Bilgileri ve Kullanımı

### CDP Bilgi Alanları
1. **Temel Bilgiler**
   - Cihaz adı
   - Arayüz bilgileri
   - Platform bilgisi
   - IP adresleri

2. **Detaylı Bilgiler**
   - Yetenekler (Router, Switch, Host)
   - VTP domain
   - Native VLAN
   - Duplex modu
   - Yönetim adresleri

### CDP Kullanım Alanları
1. **Ağ Keşfi**
   - Komşu cihazları bulma
   - Ağ topolojisi oluşturma
   - Bağlantı doğrulama

2. **Sorun Giderme**
   - Bağlantı sorunlarını tespit
   - Arayüz durumlarını kontrol
   - Yapılandırma doğrulama

## CDP Yapılandırma ve Yönetim

### Temel CDP Komutları
```cisco
! CDP'yi etkinleştirme/devre dışı bırakma
Router(config)# cdp run
Router(config)# no cdp run

! Arayüz bazında CDP yapılandırması
Router(config)# interface GigabitEthernet0/1
Router(config-if)# cdp enable
Router(config-if)# no cdp enable

! CDP zamanlama parametreleri
Router(config)# cdp timer 30
Router(config)# cdp holdtime 120
```

### CDP Bilgi Görüntüleme
```cisco
! Komşu cihazları listeleme
Router# show cdp neighbors

! Detaylı komşu bilgileri
Router# show cdp neighbors detail

! Arayüz CDP durumu
Router# show cdp interface

! CDP trafik istatistikleri
Router# show cdp traffic

! Belirli bir komşu hakkında bilgi
Router# show cdp entry *
```

## CDP Güvenliği ve Best Practices

### 1. CDP Güvenliği
- **CDP'yi Devre Dışı Bırakma**
  - Güvenlik gerektiren arayüzlerde
  - Dış ağ bağlantılarında
  - Kullanıcı portlarında

- **CDP Zamanlama Ayarları**
  - Yayın aralığını değiştirme
  - TTL süresini ayarlama
  - Holdtime değerini değiştirme

### 2. Best Practices
- CDP'yi sadece gerekli arayüzlerde etkinleştirin
- Dış ağ bağlantılarında CDP'yi devre dışı bırakın
- CDP zamanlama parametrelerini optimize edin
- CDP bilgilerini düzenli olarak kontrol edin
- CDP güvenlik politikalarını uygulayın

## CDP Sorun Giderme

### Yaygın Sorunlar
1. CDP komşuları görünmüyor
2. CDP mesajları alınamıyor
3. CDP zaman aşımı sorunları
4. CDP yapılandırma hataları

### Sorun Giderme Adımları
1. CDP'nin etkin olduğunu kontrol et
2. Arayüz durumlarını kontrol et
3. CDP zamanlama parametrelerini kontrol et
4. Debug çıktılarını analiz et
5. Komşu cihazları kontrol et

### Debug Komutları
```cisco
! CDP debug
Router# debug cdp packets
Router# debug cdp events
Router# debug cdp adjacency
```

## Önemli Notlar
- CDP sadece Cisco cihazları arasında çalışır
- CDP bilgileri güvenli değildir
- CDP trafiği ağ bant genişliğini etkiler
- CDP bilgileri yönetim amaçlıdır
- CDP güvenlik politikaları önemlidir
- CDP bilgileri düzenli olarak kontrol edilmelidir
- CDP, ağ yönetimi için kritik bir araçtır 