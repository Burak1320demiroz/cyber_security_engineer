# CHAP (Challenge Handshake Authentication Protocol)

CHAP, PPP bağlantılarında kullanılan güvenli bir kimlik doğrulama protokolüdür. Üç yönlü el sıkışma mekanizması ve şifreli kimlik doğrulama sağlar. PAP'a göre daha güvenlidir.

## CHAP Temel Kavramlar

### Protokol Özellikleri
- Güvenli kimlik doğrulama mekanizması
- Şifreli iletişim sağlar
- Periyodik doğrulama yapar
- MD5 hash algoritması kullanır
- RFC 1994 standardına uygun

### CHAP vs PAP Karşılaştırması
1. **CHAP Avantajları**
   - Şifreler ağda açık metin olarak dolaşmaz
   - Her oturumda farklı challenge kullanır
   - Replay saldırılarına karşı koruma sağlar
   - Periyodik doğrulama yapar

2. **PAP Dezavantajları**
   - Şifreler açık metin olarak gönderilir
   - Tek seferlik doğrulama yapar
   - Replay saldırılarına açıktır
   - Daha az güvenlidir

## CHAP Çalışma Prensibi

### 1. Challenge (Meydan Okuma)
- **Özellikler**
  - Sunucu tarafından gönderilir
  - Rastgele değer içerir
  - Tek kullanımlıktır
  - Zaman damgası içerir

- **Güvenlik**
  - Her oturumda benzersiz
  - Tahmin edilemez
  - Kısa ömürlü
  - Şifrelenmiş

### 2. Response (Yanıt)
- **İşlem Adımları**
  - İstemci challenge'ı alır
  - Şifre ile birleştirir
  - MD5 hash hesaplar
  - Hash'i gönderir

- **Güvenlik Özellikleri**
  - Şifre asla gönderilmez
  - Hash tek yönlüdür
  - Challenge ile bağlantılı
  - Doğrulanabilir

### 3. Success/Failure (Başarı/Başarısızlık)
- **Başarılı Durum**
  - Doğrulama onaylanır
  - Bağlantı kurulur
  - Oturum başlar
  - Periyodik doğrulama planlanır

- **Başarısız Durum**
  - Doğrulama reddedilir
  - Bağlantı reddedilir
  - Hata mesajı gönderilir
  - Yeniden deneme yapılır

## CHAP Yapılandırma ve Yönetim

### Temel CHAP Yapılandırması
```cisco
! Kullanıcı adı ve şifre tanımlama
Router(config)# username ROUTER2 password CISCO

! PPP kimlik doğrulama yapılandırması
Router(config)# interface Serial0/0
Router(config-if)# encapsulation ppp
Router(config-if)# ppp authentication chap

! CHAP hostname yapılandırması
Router(config)# hostname ROUTER1
```

### CHAP Doğrulama ve İzleme
```cisco
! PPP durumunu kontrol etme
Router# show ppp all
Router# show interfaces serial 0/0

! CHAP debug
Router# debug ppp authentication
Router# debug ppp negotiation

! Yapılandırmayı görüntüleme
Router# show running-config | include ppp
```

## CHAP Güvenliği ve Best Practices

### 1. Güvenlik Önlemleri
- **Şifre Politikası**
  - Güçlü şifreler kullanın
  - Şifreleri düzenli değiştirin
  - Şifreleri güvenli saklayın
  - Şifreleri paylaşmayın

- **Yapılandırma Güvenliği**
  - Hostname eşleşmesini kontrol edin
  - Şifreleri şifreleyin
  - Erişim kontrolü uygulayın
  - Loglama yapın

### 2. Best Practices
- CHAP'i tercih edin (PAP yerine)
- Güçlü şifreler kullanın
- Periyodik doğrulama yapın
- Şifreleri düzenli değiştirin
- Loglama ve izleme yapın
- Yedekleme yapın
- Güvenlik politikaları uygulayın

## CHAP Sorun Giderme

### Yaygın Sorunlar
1. Kimlik doğrulama başarısız
2. Şifre uyuşmazlığı
3. Hostname eşleşmeme
4. PPP bağlantı sorunları

### Sorun Giderme Adımları
1. Kullanıcı adı ve şifreleri kontrol et
2. Hostname yapılandırmasını doğrula
3. PPP yapılandırmasını kontrol et
4. Debug çıktılarını analiz et
5. Bağlantı durumunu kontrol et

### Debug Komutları
```cisco
! PPP ve CHAP debug
Router# debug ppp authentication
Router# debug ppp negotiation
Router# debug ppp error
```

## Önemli Notlar
- CHAP, PAP'a göre daha güvenlidir
- Şifreler ağda açık metin olarak dolaşmaz
- Her oturumda farklı challenge kullanılır
- Periyodik doğrulama yapılır
- MD5 hash algoritması kullanılır
- Hostname eşleşmesi önemlidir
- Güvenlik politikaları uygulanmalıdır 