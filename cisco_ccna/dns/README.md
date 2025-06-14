# DNS (Domain Name System)

DNS (Domain Name System), internet üzerindeki alan adlarını IP adreslerine çeviren hiyerarşik bir isimlendirme sistemidir. İnsanların anlamlı isimler kullanarak internet kaynaklarına erişmesini sağlar.

## DNS Temel Kavramlar

### Protokol Özellikleri
- UDP ve TCP port 53 kullanır
- Dağıtık veritabanı sistemi
- Hiyerarşik yapı
- Önbellek (Cache) mekanizması
- RFC 1034 ve 1035 standartlarına uygun

### DNS Hiyerarşisi
1. **Kök Sunucular (Root Servers)**
   - 13 adet kök sunucu
   - TLD sunucularının adreslerini bilir
   - Dünya genelinde dağıtık

2. **TLD Sunucuları (Top Level Domain)**
   - .com, .org, .net gibi üst düzey alanlar
   - Yetkili DNS sunucularını bilir
   - Alan adı kayıtlarını yönetir

3. **Yetkili DNS Sunucuları**
   - Belirli bir alan adı için yetkili
   - Alan adı kayıtlarını tutar
   - DNS sorgularına yanıt verir

## DNS Kayıt Türleri ve Kullanımı

### Temel Kayıt Türleri
1. **A Kaydı (Address)**
   - IPv4 adreslerini eşleştirir
   - En yaygın kayıt türü
   - Örnek: example.com. IN A 192.168.1.1

2. **AAAA Kaydı (IPv6 Address)**
   - IPv6 adreslerini eşleştirir
   - IPv6 desteği için gerekli
   - Örnek: example.com. IN AAAA 2001:db8::1

3. **CNAME Kaydı (Canonical Name)**
   - Takma ad tanımlar
   - Bir alan adını diğerine yönlendirir
   - Örnek: www.example.com. IN CNAME example.com.

4. **MX Kaydı (Mail Exchange)**
   - E-posta sunucularını belirtir
   - Öncelik değeri içerir
   - Örnek: example.com. IN MX 10 mail.example.com.

5. **NS Kaydı (Name Server)**
   - Alan adı için yetkili sunucuları belirtir
   - Alt alan adları için gerekli
   - Örnek: example.com. IN NS ns1.example.com.

### Özel Kayıt Türleri
1. **TXT Kaydı**
   - Metin bilgisi içerir
   - SPF, DKIM gibi kayıtlar için kullanılır
   - Örnek: example.com. IN TXT "v=spf1 ip4:192.168.1.1"

2. **PTR Kaydı (Pointer)**
   - Ters DNS sorguları için kullanılır
   - IP adresinden alan adına çözümleme
   - Örnek: 1.1.168.192.in-addr.arpa. IN PTR example.com.

## DNS Sunucu Türleri ve Yapılandırma

### Sunucu Türleri
1. **Özyinelemeli DNS Sunucuları (Recursive)**
   - İstemci sorgularını çözümler
   - Önbellek kullanır
   - Hiyerarşik sorgu yapar

2. **Yetkili DNS Sunucuları (Authoritative)**
   - Belirli bir alan için yetkili
   - Zone dosyalarını tutar
   - Doğrudan yanıt verir

### DNS Yapılandırması
```cisco
! DNS sunucu yapılandırması
Router(config)# ip name-server 8.8.8.8
Router(config)# ip domain-name example.com
Router(config)# ip domain-lookup

! DNS önbellek yapılandırması
Router(config)# ip dns server
Router(config)# ip dns server view default
Router(config-dns-view)# dns forwarder 8.8.8.8
```

## DNS Güvenliği ve Best Practices

### 1. Güvenlik Önlemleri
- **DNSSEC (DNS Security Extensions)**
  - DNS kayıtlarını imzalar
  - Sahte yanıtları engeller
  - Bütünlük ve doğrulama sağlar

- **DNS Tünelleme Koruması**
  - DNS trafiğini izler
  - Şüpheli sorguları engeller
  - Rate limiting uygular

### 2. Best Practices
- DNSSEC kullanın
- DNS önbelleğini yapılandırın
- DNS sunucularını güncel tutun
- DNS filtreleme uygulayın
- DNS izleme yapın
- Yedek DNS sunucuları kullanın
- DNS güvenlik politikaları uygulayın

## DNS Sorun Giderme

### Yaygın Sorunlar
1. DNS çözümleme başarısız
2. Yanlış DNS kayıtları
3. DNS sunucu erişim sorunları
4. DNS önbellek sorunları
5. DNSSEC doğrulama hataları

### Sorun Giderme Adımları
1. DNS sunucu durumunu kontrol et
2. DNS kayıtlarını doğrula
3. DNS önbelleğini temizle
4. DNS sorgularını test et
5. Debug çıktılarını analiz et

### Debug Komutları
```cisco
! DNS debug
Router# debug ip dns
Router# debug ip domain
Router# show hosts
```

## Önemli Notlar
- DNS, internet altyapısının temelidir
- Güvenlik önlemleri kritiktir
- Önbellek performansı artırır
- DNSSEC güvenlik sağlar
- DNS sunucuları yedekli olmalıdır
- DNS kayıtları düzenli kontrol edilmelidir
- DNS izleme ve loglama yapılmalıdır 