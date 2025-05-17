# ACL (Access Control List)

ACL, ağ trafiğini filtrelemek ve kontrol etmek için kullanılan bir güvenlik mekanizmasıdır. Ağ kaynaklarına erişimi yönetmek için kullanılır.

## ACL Türleri
### Standart ACL
- Sadece kaynak IP adresine göre filtreleme
- 1-99 ve 1300-1999 numaralı listeler
- Basit filtreleme işlemleri

### Genişletilmiş ACL
- Kaynak ve hedef IP adresi
- Protokol türü
- Port numaraları
- 100-199 ve 2000-2699 numaralı listeler

## ACL Özellikleri
- Sıralı kurallar
- İlk eşleşme prensibi
- Varsayılan izin vermeme
- Her arayüz için giriş/çıkış yönü

## ACL Kullanım Alanları
- Trafik filtreleme
- Yönlendirme kontrolü
- QoS uygulamaları
- NAT yapılandırması
- VPN erişim kontrolü

## ACL Komutları
- access-list
- ip access-list
- show access-lists
- show ip access-lists
- clear access-list counters 