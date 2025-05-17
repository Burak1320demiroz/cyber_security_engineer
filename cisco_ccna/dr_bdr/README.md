# DR-BDR (Designated Router - Backup Designated Router)

DR-BDR, OSPF ağlarında broadcast ve non-broadcast çoklu erişim ağlarında (MA) kullanılan bir mekanizmadır. Ağ trafiğini optimize etmek ve yönetmek için kullanılır.

## DR-BDR'nin Özellikleri
- Ağ trafiğini azaltma
- Topoloji değişikliklerini yönetme
- LSA dağıtımını optimize etme
- Ağ kaynaklarını verimli kullanma

## DR-BDR Seçimi
### DR (Designated Router)
- En yüksek öncelik değeri
- En yüksek Router ID
- LSA'ları toplar ve dağıtır
- Ağ için merkezi nokta

### BDR (Backup Designated Router)
- İkinci en yüksek öncelik
- DR'nin yedeği
- DR'yi izler
- Hızlı geçiş yapar

## DR-BDR Öncelikleri
- 0: DR/BDR olamaz
- 1-255: DR/BDR seçilebilir
- Varsayılan: 1
- En yüksek öncelik kazanır

## DR-BDR Yapılandırması
- Interface önceliği
- Router ID
- Hello/Dead interval
- Network type
- Authentication

## DR-BDR Komutları
- ip ospf priority
- show ip ospf interface
- show ip ospf neighbor
- debug ip ospf adj
- clear ip ospf process 