# OSPF (Open Shortest Path First)

OSPF, açık kaynak kodlu bir link-state yönlendirme protokolüdür. Büyük ağlarda hızlı yakınsama ve verimli yönlendirme sağlar.

## OSPF'nin Özellikleri
- Hiyerarşik yapı
- Hızlı yakınsama
- VLSM desteği
- Yük dengeleme

## OSPF Alanları
### Backbone Area (Area 0)
- Merkezi alan
- Tüm alanları bağlar
- Transit trafik
- Omurga ağ

### Normal Areas
- Area 1-4294967295
- Backbone'a bağlı
- Yerel trafik
- Stub/Totally Stub

## OSPF Paketleri
- Hello
- DBD (Database Description)
- LSR (Link State Request)
- LSU (Link State Update)
- LSAck (Link State Acknowledgment)

## OSPF Yapılandırması
- Router ID
- Area tanımları
- Ağ tanımları
- Interface öncelikleri
- Authentication

## OSPF Komutları
- router ospf
- network
- area
- show ip ospf
- show ip ospf neighbor
- show ip ospf database 