# PAT (Port Address Translation)

PAT, tek bir genel IP adresi kullanarak birden fazla iç ağ cihazının internete bağlanmasını sağlayan bir NAT türüdür. Port numaralarını kullanarak çoklu bağlantıları yönetir.

## PAT'nin Özellikleri
- Tek IP, çoklu bağlantı
- Port numarası kullanımı
- Otomatik port ataması
- Bağlantı takibi

## PAT Çalışma Prensibi
1. İç ağ cihazı bağlantı isteği gönderir
2. Router kaynak port numarasını değiştirir
3. Dönüşüm tablosuna kayıt eklenir
4. Yanıt geldiğinde doğru cihaza yönlendirilir

## PAT Avantajları
- IP adresi tasarrufu
- Kolay yapılandırma
- Güvenlik artışı
- Maliyet etkinliği

## PAT Yapılandırması
- İç arayüz tanımı
- Dış arayüz tanımı
- ACL oluşturma
- PAT kuralları

## PAT Komutları
- ip nat inside source list
- ip nat inside source overload
- show ip nat translations
- debug ip nat
- clear ip nat translation 