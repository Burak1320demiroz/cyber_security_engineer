# SPAN (Switch Port Analyzer)

SPAN, switch portlarındaki trafiği izlemek ve analiz etmek için kullanılan bir özelliktir. Ağ izleme ve sorun giderme için önemli bir araçtır.

## SPAN Türleri
### Local SPAN
- Aynı switch içinde
- Kaynak ve hedef portlar
- VLAN bazlı izleme
- Port bazlı izleme

### Remote SPAN (RSPAN)
- Farklı switch'ler arası
- Özel RSPAN VLAN
- Uzaktan izleme
- Merkezi analiz

### Encapsulated Remote SPAN (ERSPAN)
- GRE tünelleme
- Layer 3 destek
- Uzun mesafe izleme
- IP ağları üzerinden

## SPAN Yapılandırması
- Kaynak port/VLAN
- Hedef port
- İzleme yönü
- Filtreleme
- Encapsulation

## SPAN Komutları
- monitor session
- show monitor
- show monitor session
- debug monitor
- show monitor capture 