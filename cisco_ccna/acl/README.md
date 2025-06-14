# ACL (Access Control List)

ACL, ağ trafiğini filtrelemek ve kontrol etmek için kullanılan temel bir güvenlik mekanizmasıdır. Ağ kaynaklarına erişimi yönetmek ve trafik akışını kontrol etmek için kullanılır.

## ACL Temel Kavramlar
- ACL'ler bir dizi izin verme (permit) veya reddetme (deny) ifadesinden oluşur
- Her ifade bir koşul ve bir eylem içerir
- ACL'ler sıralı olarak değerlendirilir (top-down)
- İlk eşleşen kural uygulanır ve değerlendirme sonlandırılır
- Her ACL'nin sonunda gizli bir "deny any" kuralı vardır

## ACL Türleri

### 1. Standart ACL
- Sadece kaynak IP adresine göre filtreleme yapar
- Numaralandırma aralıkları:
  - 1-99: Standart IP ACL
  - 1300-1999: Genişletilmiş standart IP ACL
- Basit filtreleme işlemleri için idealdir
- Genellikle hedef arayüze en yakın noktada uygulanır

### 2. Genişletilmiş ACL
- Daha detaylı filtreleme imkanı sağlar
- Filtreleme kriterleri:
  - Kaynak IP adresi
  - Hedef IP adresi
  - Protokol türü (TCP, UDP, ICMP, vb.)
  - Port numaraları
  - Servis türleri
- Numaralandırma aralıkları:
  - 100-199: Genişletilmiş IP ACL
  - 2000-2699: Genişletilmiş IP ACL

## ACL Yapılandırma ve Yönetim

### Temel ACL Komutları
```cisco
! Standart ACL oluşturma
Router(config)# access-list 10 permit 192.168.1.0 0.0.0.255

! Genişletilmiş ACL oluşturma
Router(config)# access-list 101 permit tcp 192.168.1.0 0.0.0.255 any eq 80

! ACL'yi arayüze uygulama
Router(config-if)# ip access-group 10 in
Router(config-if)# ip access-group 101 out

! ACL'leri görüntüleme
Router# show access-lists
Router# show ip access-lists
Router# show running-config | include access-list
```

### ACL İsimlendirme
```cisco
! İsimlendirilmiş ACL oluşturma
Router(config)# ip access-list standard BLOCK_TRAFFIC
Router(config-std-nacl)# deny 192.168.1.0 0.0.0.255
Router(config-std-nacl)# permit any
```

## ACL Kullanım Alanları ve Best Practices

### 1. Trafik Filtreleme
- Gelen ve giden trafiği kontrol etme
- Belirli protokollere izin verme/reddetme
- Port bazlı erişim kontrolü

### 2. Yönlendirme Kontrolü
- Belirli rotaların reklamını kontrol etme
- Yönlendirme protokollerini filtreleme
- Trafik yönlendirmesini yönetme

### 3. Güvenlik Uygulamaları
- Firewall görevi görme
- Servis erişimini kısıtlama
- Ağ segmentasyonu

### 4. QoS ve NAT
- Trafik sınıflandırma
- NAT kuralları için trafik tanımlama
- Bandwidth yönetimi

## ACL Best Practices
1. ACL'leri planlamadan önce ihtiyaçları belirleyin
2. En spesifik kuralları en üste yerleştirin
3. ACL'leri düzenli olarak gözden geçirin ve güncelleyin
4. ACL'leri test edin ve doğrulayın
5. ACL'leri dokümante edin
6. Gereksiz ACL'leri kaldırın
7. ACL'leri mantıksal gruplar halinde organize edin

## ACL Sorun Giderme
```cisco
! ACL sayaçlarını temizleme
Router# clear access-list counters

! ACL'lerin etkisini kontrol etme
Router# show ip interface
Router# show access-lists
Router# debug ip packet
```

## Önemli Notlar
- ACL'ler stateful değildir (oturum takibi yapmazlar)
- ACL'ler performansı etkileyebilir
- ACL'ler yanlış yapılandırıldığında ağ erişimini engelleyebilir
- ACL'leri test ortamında doğrulayın
- ACL'leri düzenli olarak yedekleyin 