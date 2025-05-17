# EIGRP (Enhanced Interior Gateway Routing Protocol)

EIGRP, Cisco'ya özel gelişmiş bir iç yönlendirme protokolüdür. Distance Vector ve Link State protokollerinin avantajlarını birleştiren hibrit bir protokoldür.

## EIGRP'nin Özellikleri
- Hızlı yakınsama
- Düşük bant genişliği kullanımı
- Yük dengeleme
- VLSM desteği

## EIGRP Bileşenleri
### DUAL (Diffusing Update Algorithm)
- En iyi yol seçimi
- Yedek yol hesaplama
- Topoloji tablosu
- Feasible Successor

### RTP (Reliable Transport Protocol)
- Güvenilir iletişim
- Sıralı paket iletimi
- ACK mekanizması
- Multicast kullanımı

## EIGRP Paketleri
- Hello
- Update
- Query
- Reply
- ACK

## EIGRP Yapılandırması
- Router ID
- AS numarası
- Ağ tanımları
- Metric ağırlıkları
- Yük dengeleme

## EIGRP Komutları
- router eigrp
- network
- show ip eigrp
- show ip eigrp neighbors
- show ip eigrp topology 