# PVST (Per-VLAN Spanning Tree)

PVST, her VLAN için ayrı bir spanning tree örneği oluşturan Cisco'ya özel bir STP türüdür. VLAN bazlı yük dengeleme sağlar.

## PVST'nin Özellikleri
- VLAN bazlı spanning tree
- Her VLAN için ayrı root bridge
- Yük dengeleme imkanı
- Cisco'ya özel protokol

## PVST Avantajları
- VLAN bazlı yük dengeleme
- Daha iyi bant genişliği kullanımı
- VLAN izolasyonu
- Esnek yapılandırma

## PVST Yapılandırması
- spanning-tree mode pvst
- spanning-tree vlan
- spanning-tree cost
- spanning-tree priority
- spanning-tree port-priority

## PVST Komutları
- show spanning-tree
- show spanning-tree vlan
- show spanning-tree root
- show spanning-tree detail
- debug spanning-tree

## PVST Güvenliği
- BPDU Guard
- Root Guard
- Loop Guard
- BPDU Filter
- Port Fast 