# ARP (Address Resolution Protocol)

ARP, IP adreslerini MAC adreslerine çeviren temel bir ağ protokolüdür. Aynı ağ içindeki cihazların birbirleriyle iletişim kurabilmesi için kullanılır ve OSI modelinin 2. ve 3. katmanları arasında köprü görevi görür.

## ARP'nin Temel Kavramları

### Protokol Özellikleri
- Katman 2 (Data Link) ve Katman 3 (Network) arasında köprü
- Yerel ağ (broadcast domain) içinde çalışır
- Dinamik ve statik ARP tabloları kullanır
- ARP önbelleği (cache) ile performans optimizasyonu
- Broadcast ve unicast mesajlar kullanır

### ARP Mesaj Tipleri
1. **ARP Request (İstek)**
   - Broadcast olarak gönderilir
   - Hedef IP adresine sahip cihazı arar
   - Tüm ağ cihazları tarafından alınır

2. **ARP Reply (Yanıt)**
   - Unicast olarak gönderilir
   - MAC adresi bilgisini içerir
   - Sadece istek yapan cihaza gönderilir

## ARP İşleyişi ve Örnek Senaryo

### Temel ARP İşlemi
1. Host A, Host B ile iletişim kurmak ister
2. Host A, ARP tablosunda Host B'nin MAC adresini kontrol eder
3. MAC adresi bulunamazsa ARP Request gönderilir
4. Host B, ARP Reply ile MAC adresini gönderir
5. Host A, MAC adresini ARP tablosuna kaydeder

### ARP Tablosu Yapısı
```
IP Address        MAC Address        Interface    Type    Age
192.168.1.1      00:11:22:33:44:55  Gi0/1       Dynamic  120
192.168.1.2      00:11:22:33:44:56  Gi0/1       Static   -
```

## ARP Yönetimi ve Komutlar

### Cisco Cihazlarda ARP Komutları
```cisco
! ARP tablosunu görüntüleme
Router# show arp
Router# show ip arp

! ARP önbelleğini temizleme
Router# clear arp-cache

! Statik ARP girişi ekleme
Router(config)# arp 192.168.1.100 0000.1111.2222 arpa

! ARP timeout süresini ayarlama
Router(config)# interface GigabitEthernet0/1
Router(config-if)# arp timeout 300
```

### İşletim Sistemlerinde ARP Komutları
```bash
# Windows
arp -a              # ARP tablosunu görüntüleme
arp -d *            # Tüm ARP girişlerini silme
arp -s IP MAC       # Statik ARP girişi ekleme

# Linux
arp -n              # ARP tablosunu görüntüleme
arp -d IP           # Belirli bir IP için ARP girişini silme
arp -s IP MAC       # Statik ARP girişi ekleme
```

## ARP Güvenliği ve Best Practices

### Güvenlik Tehditleri
1. **ARP Spoofing (Zehirlenmesi)**
   - Sahte MAC adresleri ile ARP tablosunun manipülasyonu
   - Man-in-the-middle saldırılarına zemin hazırlar
   - Ağ trafiğinin yönlendirilmesi

2. **ARP Flooding**
   - Ağın ARP tablolarını doldurma
   - Servis dışı bırakma saldırıları
   - Ağ performansını düşürme

### Güvenlik Önlemleri
1. **Statik ARP Tabloları**
   - Kritik cihazlar için statik ARP girişleri
   - ARP tablosunun manipülasyonunu önleme
   - Güvenilir MAC adreslerinin korunması

2. **Port Güvenliği**
   - MAC adresi filtreleme
   - Port bazlı MAC adresi sınırlaması
   - Yetkisiz cihazların engellenmesi

3. **ARP Doğrulama**
   - ARP mesajlarının doğrulanması
   - DHCP Snooping ile entegrasyon
   - Dynamic ARP Inspection (DAI)

## ARP Sorun Giderme

### Yaygın Sorunlar
1. ARP tablosu dolu
2. Yanlış MAC adresleri
3. ARP timeout sorunları
4. Duplicate IP adresleri

### Sorun Giderme Adımları
1. ARP tablosunu kontrol et
2. ARP önbelleğini temizle
3. Ağ bağlantılarını doğrula
4. Statik ARP girişlerini kontrol et
5. Port güvenliği ayarlarını gözden geçir

## Önemli Notlar
- ARP tablosu sınırlı boyuttadır
- ARP girişleri belirli bir süre sonra silinir
- Statik ARP girişleri manuel silinene kadar kalır
- ARP mesajları güvenli değildir
- ARP sadece IPv4'te kullanılır (IPv6'da NDP kullanılır) 