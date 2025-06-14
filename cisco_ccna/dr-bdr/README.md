# DR-BDR (Designated Router - Backup Designated Router)

DR-BDR, OSPF ağlarında broadcast ve non-broadcast çoklu erişim ağlarında (MA) kullanılan bir mekanizmadır. Ağ trafiğini optimize etmek, LSA dağıtımını yönetmek ve ağ kaynaklarını verimli kullanmak için tasarlanmıştır.

## DR-BDR Temel Kavramlar

### Protokol Özellikleri
- OSPF çoklu erişim ağlarında kullanılır
- Ağ trafiğini azaltır
- LSA dağıtımını optimize eder
- Topoloji değişikliklerini yönetir
- RFC 2328 standardına uygun

### DR-BDR Kullanım Alanları
1. **Broadcast Ağlar**
   - Ethernet
   - Token Ring
   - FDDI

2. **Non-Broadcast Ağlar**
   - Frame Relay
   - ATM
   - X.25

## DR-BDR Seçim Mekanizması

### 1. DR (Designated Router)
- **Seçim Kriterleri**
  - En yüksek öncelik değeri
  - En yüksek Router ID
  - Ağ için merkezi nokta
  - LSA'ları toplar ve dağıtır

- **Görevleri**
  - LSA'ları toplar
  - LSA'ları diğer router'lara dağıtır
  - Ağ için merkezi nokta oluşturur
  - Topoloji değişikliklerini yönetir

### 2. BDR (Backup Designated Router)
- **Seçim Kriterleri**
  - İkinci en yüksek öncelik
  - İkinci en yüksek Router ID
  - DR'nin yedeği
  - Hızlı geçiş yapabilme

- **Görevleri**
  - DR'yi izler
  - DR arızalandığında görevi devralır
  - LSA'ları alır ve saklar
  - Geçiş süresini minimize eder

## DR-BDR Yapılandırma ve Yönetim

### Öncelik Yapılandırması
```cisco
! Arayüz önceliği ayarlama
Router(config)# interface GigabitEthernet0/1
Router(config-if)# ip ospf priority 100

! Router ID yapılandırması
Router(config)# router ospf 1
Router(config-router)# router-id 1.1.1.1

! Hello/Dead interval ayarları
Router(config-if)# ip ospf hello-interval 10
Router(config-if)# ip ospf dead-interval 40
```

### DR-BDR Doğrulama ve İzleme
```cisco
! Arayüz OSPF durumunu görüntüleme
Router# show ip ospf interface GigabitEthernet0/1

! OSPF komşularını görüntüleme
Router# show ip ospf neighbor

! OSPF veritabanını görüntüleme
Router# show ip ospf database

! OSPF sürecini yeniden başlatma
Router# clear ip ospf process
```

## DR-BDR Güvenliği ve Best Practices

### 1. Güvenlik Önlemleri
- **OSPF Kimlik Doğrulama**
  - MD5 şifreleme
  - Alan bazlı kimlik doğrulama
  - Komşu doğrulama
  - Güvenli iletişim

- **Ağ Güvenliği**
  - Arayüz filtreleme
  - Komşu filtreleme
  - LSA filtreleme
  - Route filtreleme

### 2. Best Practices
- DR/BDR önceliklerini planlayın
- Router ID'leri manuel atayın
- Hello/Dead interval'leri optimize edin
- Kimlik doğrulama kullanın
- Yedekli yapılandırma yapın
- İzleme ve loglama yapın
- Düzenli kontrol yapın

## DR-BDR Sorun Giderme

### Yaygın Sorunlar
1. DR/BDR seçim sorunları
2. Komşuluk kurulamama
3. LSA dağıtım sorunları
4. Topoloji değişikliği sorunları
5. Kimlik doğrulama hataları

### Sorun Giderme Adımları
1. Arayüz durumunu kontrol et
2. Öncelik değerlerini doğrula
3. Komşuluk durumunu kontrol et
4. LSA dağıtımını analiz et
5. Debug çıktılarını incele

### Debug Komutları
```cisco
! OSPF debug
Router# debug ip ospf adj
Router# debug ip ospf events
Router# debug ip ospf packet
```

## Önemli Notlar
- DR/BDR seçimi önemlidir
- Öncelik değerleri planlanmalıdır
- Kimlik doğrulama kullanılmalıdır
- Hello/Dead interval'ler optimize edilmelidir
- Yedekli yapılandırma yapılmalıdır
- Düzenli kontrol yapılmalıdır
- Sorun giderme prosedürleri hazır olmalıdır 