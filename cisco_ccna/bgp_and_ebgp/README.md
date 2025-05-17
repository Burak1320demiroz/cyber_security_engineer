# BGP (Border Gateway Protocol) ve EBGP

BGP, internet üzerinde AS'ler (Autonomous Systems) arası yönlendirme yapan bir dış yönlendirme protokolüdür. Path vector protokolü olarak çalışır.

## BGP Türleri
### IBGP (Internal BGP)
- Aynı AS içinde
- Full mesh gerekliliği
- Route reflector
- Confederation

### EBGP (External BGP)
- Farklı AS'ler arası
- Doğrudan bağlantı
- AS path kontrolü
- Route filtering

## BGP Özellikleri
- Path vector protokolü
- TCP port 179
- Incremental updates
- Policy-based routing
- Loop prevention

## BGP Bileşenleri
### Attributes
- AS Path
- Next Hop
- Origin
- Local Preference
- MED
- Community

### Neighbor States
- Idle
- Connect
- Active
- OpenSent
- OpenConfirm
- Established

## BGP Yapılandırması
- Router ID
- AS numarası
- Neighbor tanımları
- Network tanımları
- Route filtering
- Route redistribution

## BGP Komutları
- router bgp
- neighbor
- network
- show ip bgp
- show ip bgp summary
- show ip bgp neighbors
- debug ip bgp 