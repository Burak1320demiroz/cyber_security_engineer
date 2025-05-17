# SNMP (Simple Network Management Protocol)

SNMP, ağ cihazlarını izlemek ve yönetmek için kullanılan bir protokoldür. Ağ yönetimi ve izleme için standart bir yöntem sağlar.

## SNMP Versiyonları
### SNMPv1
- İlk versiyon
- Basit güvenlik
- Community string
- GET/SET/TRAP

### SNMPv2c
- Community-based
- Bulk operations
- 64-bit sayaçlar
- İyileştirilmiş hata yönetimi

### SNMPv3
- Güvenli iletişim
- Kimlik doğrulama
- Şifreleme
- Kullanıcı bazlı erişim

## SNMP Bileşenleri
### MIB (Management Information Base)
- Hiyerarşik yapı
- OID (Object Identifier)
- Değişken tanımları
- Standart/Özel MIB'ler

### SNMP Mesajları
- GET
- GETNEXT
- GETBULK
- SET
- TRAP
- INFORM

## SNMP Yapılandırması
- Community string
- Access list
- Trap host
- View tanımları
- Group tanımları
- User tanımları

## SNMP Komutları
- snmp-server community
- snmp-server location
- snmp-server contact
- snmp-server enable traps
- show snmp
- debug snmp
- show snmp community 