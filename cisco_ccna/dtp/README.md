# DTP (Dynamic Trunking Protocol)

DTP, Cisco switch'ler arasında trunk bağlantılarını otomatik olarak yapılandırmak için kullanılan bir protokoldür. Portların trunk moduna geçişini dinamik olarak yönetir ve VLAN yapılandırmasını kolaylaştırır.

## DTP Temel Kavramlar

### Protokol Özellikleri
- Otomatik trunk yapılandırması
- Sadece Cisco cihazları arasında çalışır
- ISL ve 802.1Q protokollerini destekler
- Varsayılan olarak etkindir
- Layer 2 protokolü
- Multicast MAC adresi kullanır (01-00-0C-CC-CC-CC)

### DTP Kullanım Alanları
1. **Switch-to-Switch Bağlantıları**
   - Core-Distribution bağlantıları
   - Distribution-Access bağlantıları
   - Stack ünitesi bağlantıları

2. **Switch-to-Router Bağlantıları**
   - Router-on-a-stick yapılandırması
   - Layer 3 switch bağlantıları
   - Gateway bağlantıları

## DTP Modları ve Yapılandırma

### 1. Dynamic Auto
- **Özellikler**
  - Pasif bekleme durumu
  - Karşı taraf istek gönderirse trunk olur
  - Varsayılan mod
  - En az müdahale gerektiren mod

- **Yapılandırma**
```cisco
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# switchport mode dynamic auto
```

### 2. Dynamic Desirable
- **Özellikler**
  - Aktif trunk isteği
  - Dynamic Auto ve Desirable ile trunk olur
  - Trunk oluşturmaya çalışır
  - Agresif trunk oluşturma

- **Yapılandırma**
```cisco
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# switchport mode dynamic desirable
```

### 3. Trunk
- **Özellikler**
  - Sabit trunk modu
  - DTP mesajları gönderir
  - Her zaman trunk olarak çalışır
  - En güvenli trunk modu

- **Yapılandırma**
```cisco
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk encapsulation dot1q
```

### 4. Access
- **Özellikler**
  - Sabit access modu
  - DTP mesajları göndermez
  - Trunk oluşturmaz
  - Tek VLAN kullanır

- **Yapılandırma**
```cisco
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```

## DTP Doğrulama ve İzleme

### Temel Komutlar
```cisco
! DTP durumunu görüntüleme
Switch# show dtp interface GigabitEthernet0/1

! Port durumunu görüntüleme
Switch# show interfaces GigabitEthernet0/1 switchport

! DTP detaylarını görüntüleme
Switch# show dtp

! DTP debug
Switch# debug dtp
```

## DTP Güvenliği ve Best Practices

### 1. Güvenlik Önlemleri
- **DTP Devre Dışı Bırakma**
  - Manuel trunk yapılandırma
  - DTP mesajlarını engelleme
  - Port güvenliği
  - Native VLAN değiştirme

- **Trunk Güvenliği**
  - İzin verilen VLAN'ları sınırlama
  - Native VLAN'ı değiştirme
  - DTP'yi devre dışı bırakma
  - Port güvenliği yapılandırma

### 2. Best Practices
- DTP'yi devre dışı bırakın
- Manuel trunk yapılandırın
- Native VLAN'ı değiştirin
- İzin verilen VLAN'ları sınırlayın
- Port güvenliği kullanın
- Düzenli kontrol yapın
- Loglama yapın

## DTP Sorun Giderme

### Yaygın Sorunlar
1. Trunk oluşturulamama
2. DTP uyumsuzlukları
3. VLAN taşıma sorunları
4. Native VLAN sorunları
5. Encapsulation sorunları

### Sorun Giderme Adımları
1. DTP durumunu kontrol et
2. Port modunu doğrula
3. Encapsulation tipini kontrol et
4. VLAN yapılandırmasını kontrol et
5. Debug çıktılarını incele

### Debug Komutları
```cisco
! DTP debug
Switch# debug dtp
Switch# debug dtp packets
Switch# debug dtp events
```

## Önemli Notlar
- DTP güvenlik riski oluşturabilir
- Manuel trunk yapılandırması önerilir
- Native VLAN değiştirilmelidir
- Port güvenliği kullanılmalıdır
- Düzenli kontrol yapılmalıdır
- Loglama yapılmalıdır
- Sorun giderme prosedürleri hazır olmalıdır 