# APIC-EM (Application Policy Infrastructure Controller - Enterprise Module)

APIC-EM, Cisco'nun kurumsal ağlar için geliştirdiği SDN (Software-Defined Networking) kontrolcüsüdür. Ağ yönetimini otomatize eder, merkezi kontrol sağlar ve ağ operasyonlarını basitleştirir.

## APIC-EM Temel Kavramlar
- SDN mimarisinin kurumsal uygulaması
- Merkezi ağ yönetimi ve otomasyonu
- REST API tabanlı programlanabilirlik
- Ağ politikalarının merkezi yönetimi
- Ağ servislerinin otomatik dağıtımı

## APIC-EM Bileşenleri ve Özellikleri

### 1. Network Control
- **Topoloji Yönetimi**
  - Otomatik ağ keşfi
  - Gerçek zamanlı topoloji görüntüleme
  - Cihaz ve bağlantı envanteri
  - Ağ haritası oluşturma

- **Path Hesaplama**
  - En iyi yol analizi
  - Yük dengeleme
  - Trafik optimizasyonu
  - Path doğrulama

- **QoS Yönetimi**
  - Policy tabanlı QoS
  - Otomatik QoS yapılandırması
  - Bandwidth yönetimi
  - Servis kalitesi izleme

### 2. Network Services

#### EasyQoS
- **Özellikler**
  - Otomatik QoS politikaları
  - Uygulama tanıma ve sınıflandırma
  - Bandwidth optimizasyonu
  - Policy uygulama ve yönetimi

- **Kullanım Alanları**
  - VoIP ve video konferans
  - Kritik iş uygulamaları
  - Bulk veri transferi
  - Web trafiği yönetimi

#### IWAN (Intelligent WAN)
- **Özellikler**
  - WAN optimizasyonu
  - Akıllı path seçimi
  - Performance monitoring
  - Policy tabanlı yönlendirme

- **Avantajlar**
  - MPLS ve internet bağlantılarının entegrasyonu
  - Otomatik failover
  - Yük dengeleme
  - QoS garantisi

## APIC-EM Yapılandırma ve Yönetim

### Kurulum Adımları
1. Controller kurulumu
2. Ağ cihazlarının keşfi
3. Kimlik doğrulama yapılandırması
4. Policy tanımları
5. Servis aktivasyonu

### Temel Komutlar
```cisco
! APIC-EM durumunu kontrol etme
Router# show apic-em status

! Topoloji bilgilerini görüntüleme
Router# show apic-em topology

! Path analizi
Router# show apic-em path

! Servis durumunu kontrol etme
Router# show apic-em service
```

## APIC-EM Servisleri ve Uygulamaları

### 1. Network Plug and Play
- Yeni cihazların otomatik yapılandırması
- Zero-touch provisioning
- Merkezi yapılandırma yönetimi
- Cihaz şablonları

### 2. Path Trace
- End-to-end path analizi
- Sorun tespiti
- Performans ölçümü
- QoS doğrulama

### 3. Policy Yönetimi
- Merkezi policy tanımları
- Otomatik policy dağıtımı
- Policy uyumluluk kontrolü
- Policy raporlama

## APIC-EM Best Practices
1. Düzenli yedekleme yapın
2. Güvenlik politikalarını sıkı tutun
3. Performans izleme yapın
4. Policy değişikliklerini test edin
5. Dokümantasyonu güncel tutun
6. Yedek controller kullanın
7. Düzenli güncellemeleri takip edin

## Sorun Giderme
```cisco
! Debug modunu aktifleştirme
Router# debug apic-em

! Servis durumunu kontrol etme
Router# show apic-em service status

! Bağlantı sorunlarını tespit etme
Router# show apic-em connection
```

## Önemli Notlar
- APIC-EM, ağ yönetimini merkezileştirir
- REST API ile programlanabilir
- Otomatik ağ keşfi yapar
- Policy tabanlı yönetim sağlar
- Gerçek zamanlı izleme sunar
- Ağ servislerini otomatize eder 