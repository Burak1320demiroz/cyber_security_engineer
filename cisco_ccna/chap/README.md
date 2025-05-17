# CHAP (Challenge Handshake Authentication Protocol)

CHAP, PPP bağlantılarında kullanılan güvenli bir kimlik doğrulama protokolüdür. Üç yönlü el sıkışma ve şifreli kimlik doğrulama sağlar.

## CHAP'nin Özellikleri
- Güvenli kimlik doğrulama
- Şifreli iletişim
- Periyodik doğrulama
- MD5 hash kullanımı

## CHAP Çalışma Prensibi
### Challenge
- Sunucu challenge gönderir
- Rastgele değer
- Tek kullanımlık
- Zaman damgası

### Response
- İstemci yanıt verir
- MD5 hash
- Şifre + Challenge
- Güvenli yanıt

### Success/Failure
- Doğrulama sonucu
- Bağlantı onayı
- Hata durumu
- Yeniden deneme

## CHAP Güvenlik Özellikleri
- Şifre ağda dolaşmaz
- Her oturumda farklı challenge
- Replay saldırılarına karşı koruma
- Sniffing'e karşı direnç

## CHAP Yapılandırması
- Kullanıcı adı
- Şifre
- Hostname
- Authentication list
- Interface yapılandırması

## CHAP Komutları
- username
- ppp authentication chap
- show ppp
- debug ppp authentication
- show running-config 