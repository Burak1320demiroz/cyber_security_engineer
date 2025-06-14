# DHCP (Dynamic Host Configuration Protocol)

DHCP, ağ cihazlarına otomatik olarak IP adresi ve diğer ağ yapılandırma parametrelerini atayan bir protokoldür. Ağ yönetimini kolaylaştırır ve IP adresi yönetimini otomatize eder.

## DHCP Temel Kavramlar

### Protokol Özellikleri
- UDP port 67 (Server) ve 68 (Client) kullanır
- Otomatik IP adresi atama
- Dinamik ve statik adres havuzu
- Lease (kiralama) süresi yönetimi
- RFC 2131 standardına uygun

### DHCP Mesaj Tipleri
1. **DHCPDISCOVER**
   - İstemci tarafından gönderilir
   - Broadcast olarak yayınlanır
   - DHCP sunucularını arar

2. **DHCPOFFER**
   - Sunucu tarafından gönderilir
   - IP adresi teklifi içerir
   - Teklif süresi belirtir

3. **DHCPREQUEST**
   - İstemci tarafından gönderilir
   - Teklifi kabul eder
   - Diğer sunucuları bilgilendirir

4. **DHCPACK**
   - Sunucu tarafından gönderilir
   - IP adresi onayı
   - Yapılandırma parametreleri

5. **DHCPNAK**
   - Sunucu tarafından gönderilir
   - Teklif reddi
   - Hata durumu bildirimi

## DHCP Yapılandırma ve Yönetim

### DHCP Sunucu Yapılandırması
```cisco
! DHCP havuzu oluşturma
Router(config)# ip dhcp pool LAN-POOL
Router(dhcp-config)# network 192.168.1.0 255.255.255.0
Router(dhcp-config)# default-router 192.168.1.1
Router(dhcp-config)# dns-server 8.8.8.8
Router(dhcp-config)# lease 7

! Hariç tutulacak adresler
Router(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.10

! DHCP sunucu parametreleri
Router(config)# ip dhcp ping timeout 100
Router(config)# ip dhcp conflict logging
```

### DHCP İstemci Yapılandırması
```cisco
! Arayüz DHCP yapılandırması
Router(config)# interface GigabitEthernet0/1
Router(config-if)# ip address dhcp
```

### DHCP Doğrulama ve İzleme
```cisco
! DHCP havuzu bilgilerini görüntüleme
Router# show ip dhcp pool
Router# show ip dhcp binding

! DHCP sunucu istatistikleri
Router# show ip dhcp server statistics

! DHCP debug
Router# debug ip dhcp server events
Router# debug ip dhcp server packet
```

## DHCP Güvenliği ve Best Practices

### 1. Güvenlik Önlemleri
- **DHCP Snooping**
  - Yetkisiz DHCP sunucularını engeller
  - DHCP mesajlarını doğrular
  - Güvenilir portları belirler
  - Rate limiting uygular

- **IP Source Guard**
  - IP adresi doğrulaması yapar
  - MAC adresi doğrulaması yapar
  - Sahte IP adreslerini engeller
  - DHCP binding tablosunu kullanır

### 2. Best Practices
- DHCP havuzlarını planlayın
- Hariç tutulacak adresleri belirleyin
- Lease sürelerini optimize edin
- Yedek DHCP sunucu kullanın
- DHCP Snooping yapılandırın
- IP Source Guard kullanın
- Loglama ve izleme yapın

## DHCP Sorun Giderme

### Yaygın Sorunlar
1. IP adresi alınamıyor
2. DHCP sunucuya erişilemiyor
3. Lease süresi sorunları
4. IP çakışmaları
5. DHCP Snooping sorunları

### Sorun Giderme Adımları
1. DHCP sunucu durumunu kontrol et
2. Ağ bağlantısını doğrula
3. DHCP havuzunu kontrol et
4. Hariç tutulan adresleri kontrol et
5. Debug çıktılarını analiz et

### Debug Komutları
```cisco
! DHCP debug
Router# debug ip dhcp server events
Router# debug ip dhcp server packet
Router# debug ip dhcp server binding
```

## DHCP Relay Agent

### Yapılandırma
```cisco
! DHCP Relay Agent yapılandırması
Router(config)# interface GigabitEthernet0/1
Router(config-if)# ip helper-address 192.168.1.100
```

### Özellikler
- Farklı ağlardaki DHCP sunucularına erişim
- Broadcast mesajlarını yönlendirme
- DHCP mesajlarını doğru sunucuya iletme
- Ağ segmentasyonu desteği

## Önemli Notlar
- DHCP, ağ yönetimini kolaylaştırır
- Güvenlik önlemleri kritiktir
- Lease süreleri optimize edilmelidir
- Yedekleme önemlidir
- DHCP Snooping güvenlik sağlar
- IP Source Guard ek güvenlik sağlar
- DHCP Relay Agent farklı ağlara erişim sağlar 