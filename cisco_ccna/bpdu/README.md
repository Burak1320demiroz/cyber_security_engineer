# BPDU (Bridge Protocol Data Unit)

BPDU, spanning tree protokolünün çalışması için switch'ler arasında gönderilen kontrol mesajlarıdır. Ağ topolojisini oluşturmak, yönetmek ve döngüleri önlemek için kullanılır.

## BPDU Temel Kavramlar

### Protokol Özellikleri
- IEEE 802.1D standardına uygun
- Multicast MAC adresi: 01:80:C2:00:00:00
- Düzenli aralıklarla gönderilir (default: 2 saniye)
- Topoloji değişikliklerini bildirir
- Spanning tree hesaplamaları için kullanılır

### BPDU Türleri

#### 1. Configuration BPDU
- **Özellikler**
  - Düzenli aralıklarla gönderilir
  - Topoloji bilgisini taşır
  - Root bridge seçiminde kullanılır
  - Port durumlarını belirler

- **Kullanım Alanları**
  - Spanning tree hesaplamaları
  - Root bridge seçimi
  - Port rolü belirleme
  - Topoloji bilgisi dağıtımı

#### 2. TCN (Topology Change Notification) BPDU
- **Özellikler**
  - Topoloji değişikliklerini bildirir
  - Anlık olarak gönderilir
  - Hızlı yeniden hesaplama tetikler
  - Acil durum bildirimi yapar

- **Kullanım Alanları**
  - Port durumu değişiklikleri
  - Bağlantı kopması
  - Yeni bağlantı eklenmesi
  - Spanning tree yeniden hesaplama

## BPDU Yapısı ve Alanları

### BPDU Header
```
+----------------+----------------+
| Protocol ID    | Version        |
+----------------+----------------+
| Message Type   | Flags          |
+----------------+----------------+
```

### BPDU Alanları ve Açıklamaları
1. **Protocol ID**: 0x0000 (IEEE 802.1D)
2. **Version**: 0x00 (STP), 0x02 (RSTP), 0x03 (MSTP)
3. **Message Type**: 0x00 (Config), 0x80 (TCN)
4. **Flags**: Topology Change, Topology Change Acknowledgment
5. **Root ID**: Root bridge'in Bridge ID'si
6. **Root Path Cost**: Root bridge'e olan maliyet
7. **Bridge ID**: Gönderen switch'in Bridge ID'si
8. **Port ID**: Gönderen port'un ID'si
9. **Message Age**: BPDU'nun yaşı
10. **Max Age**: BPDU'nun maksimum yaşı (default: 20 saniye)
11. **Hello Time**: BPDU gönderim aralığı (default: 2 saniye)
12. **Forward Delay**: Port durum geçiş süresi (default: 15 saniye)

## BPDU İşleme ve Yönetim

### BPDU İşleme Süreci
1. **BPDU Alımı**
   - Port üzerinden BPDU alınır
   - BPDU formatı doğrulanır
   - BPDU bilgileri işlenir

2. **BPDU İşleme**
   - Root bridge bilgisi güncellenir
   - Port durumları belirlenir
   - Topoloji değişikliği kontrol edilir

3. **BPDU Gönderimi**
   - Yeni BPDU oluşturulur
   - Port üzerinden gönderilir
   - TCN BPDU gerekirse gönderilir

### BPDU Yapılandırma
```cisco
! BPDU Guard yapılandırması
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# spanning-tree bpduguard enable

! BPDU Filter yapılandırması
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# spanning-tree bpdufilter enable

! Root Guard yapılandırması
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# spanning-tree guard root

! BPDU Tunneling yapılandırması
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# spanning-tree bpdu tunneling
```

## BPDU Güvenliği ve Best Practices

### 1. BPDU Guard
- Port üzerinden BPDU alındığında portu kapatır
- Yetkisiz switch bağlantılarını engeller
- Port security ile birlikte kullanılabilir
- Access port'larda önerilir

### 2. BPDU Filter
- BPDU'ları filtreler veya engeller
- Port üzerinden BPDU gönderimini engeller
- Dikkatli kullanılmalıdır
- Spanning tree hesaplamalarını etkileyebilir

### 3. Root Guard
- Root bridge rolünü korur
- Yetkisiz root bridge seçimini engeller
- Root port'larda kullanılır
- Topoloji kararlılığını sağlar

### 4. Loop Guard
- Unidirectional link sorunlarını tespit eder
- Port durumlarını korur
- Döngüleri önler
- Alternatif port'larda kullanılır

## BPDU Sorun Giderme

### Temel Komutlar
```cisco
! BPDU bilgilerini görüntüleme
Switch# show spanning-tree detail
Switch# show spanning-tree interface GigabitEthernet0/1

! BPDU istatistiklerini görüntüleme
Switch# show spanning-tree statistics

! BPDU debug
Switch# debug spanning-tree all
```

### Yaygın Sorunlar
1. BPDU Guard tetiklenmesi
2. BPDU Filter yanlış yapılandırması
3. Root Guard aktivasyonu
4. Loop Guard uyarıları

### Sorun Giderme Adımları
1. Port durumlarını kontrol et
2. BPDU yapılandırmalarını gözden geçir
3. Spanning tree hesaplamalarını analiz et
4. Debug çıktılarını incele
5. Topoloji değişikliklerini kontrol et

## Önemli Notlar
- BPDU'lar spanning tree protokolünün temelidir
- BPDU güvenliği kritik öneme sahiptir
- BPDU Guard ve Root Guard birlikte kullanılabilir
- BPDU Filter dikkatli kullanılmalıdır
- BPDU Tunneling özel durumlar için kullanılır
- BPDU zamanlama parametreleri önemlidir
- BPDU işleme performansı etkileyebilir 