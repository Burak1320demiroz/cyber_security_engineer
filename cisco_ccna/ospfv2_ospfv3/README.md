# OSPFv2 ve OSPFv3

OSPF (Open Shortest Path First), link-state tabanlı bir routing protokolüdür. OSPFv2 IPv4 için, OSPFv3 ise IPv6 için kullanılır.

## OSPFv2 (IPv4)
### Özellikleri
- Link-state protokolü
- Hiyerarşik yapı
- Alan bölümleme
- Otomatik özetleme
- VLSM desteği

### Alan Tipleri
- Backbone (Area 0)
- Normal Alan
- Stub Alan
- Totally Stubby Alan
- NSSA

### Paket Tipleri
- Hello
- DBD (Database Description)
- LSR (Link State Request)
- LSU (Link State Update)
- LSAck (Link State Acknowledgment)

## OSPFv3 (IPv6)
### Özellikleri
- IPv6 desteği
- Gelişmiş güvenlik
- Çoklu adres ailesi
- Instance ID desteği
- Link-local adresler

### OSPFv3 LSA Tipleri
- Router LSA
- Network LSA
- Inter-Area Prefix LSA
- Inter-Area Router LSA
- AS-External LSA
- Link LSA
- Intra-Area Prefix LSA

## Yapılandırma
### OSPFv2
- Router ID
- Alan tanımı
- Ağ tanımı
- Özetleme
- Authentication

### OSPFv3
- Router ID
- Instance ID
- Alan tanımı
- Interface yapılandırması
- Authentication

## Komutlar
### OSPFv2
- router ospf
- network
- area
- summary-address
- show ip ospf

### OSPFv3
- ipv6 router ospf
- ipv6 ospf
- area
- summary-prefix
- show ipv6 ospf 