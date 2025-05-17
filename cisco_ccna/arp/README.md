# ARP (Address Resolution Protocol)

ARP, IP adreslerini MAC adreslerine çeviren bir protokoldür. Aynı ağ içindeki cihazların birbirleriyle iletişim kurabilmesi için kullanılır.

## ARP'nin Temel Özellikleri
- Katman 2 ve 3 arasında köprü görevi görür
- Yerel ağ içinde çalışır
- Dinamik ve statik ARP tabloları
- ARP önbelleği kullanır

## ARP İşleyişi
1. ARP İsteği (Request)
   - Yayın (Broadcast) olarak gönderilir
   - Hedef IP adresine sahip cihazı arar
2. ARP Yanıtı (Reply)
   - Tek noktaya (Unicast) gönderilir
   - MAC adresi bilgisini içerir

## ARP Tablosu
- IP Adresi
- MAC Adresi
- Arayüz
- Tip (Dinamik/Statik)
- Yaş (Age)

## ARP Komutları
- show arp
- show ip arp
- clear arp-cache
- arp -a (Windows)
- arp -n (Linux)

## ARP Güvenliği
- ARP Zehirlenmesi (Spoofing)
- Statik ARP Tabloları
- ARP Doğrulama
- Port Güvenliği 