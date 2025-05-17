# BPDU (Bridge Protocol Data Unit)

BPDU, spanning tree protokolünün çalışması için switch'ler arasında gönderilen kontrol mesajlarıdır. Ağ topolojisini oluşturmak ve yönetmek için kullanılır.

## BPDU Türleri
### Configuration BPDU
- Topoloji bilgisi
- Root bridge seçimi
- Port durumları
- Düzenli gönderilir

### TCN (Topology Change Notification) BPDU
- Topoloji değişikliği
- Hızlı yeniden hesaplama
- Acil durum bildirimi
- Anlık gönderilir

## BPDU Alanları
- Protocol ID
- Version
- Message Type
- Flags
- Root ID
- Root Path Cost
- Bridge ID
- Port ID
- Message Age
- Max Age
- Hello Time
- Forward Delay

## BPDU İşleme
- BPDU alımı
- BPDU işleme
- BPDU gönderimi
- BPDU filtreleme

## BPDU Güvenliği
- BPDU Guard
- BPDU Filter
- Root Guard
- Loop Guard
- BPDU Tunneling 