# HSRP (Hot Standby Router Protocol)

HSRP, Cisco'ya özel bir yedeklilik protokolüdür. Birden fazla router'ı sanal bir router gibi çalıştırarak yüksek erişilebilirlik sağlar.

## HSRP'nin Özellikleri
- Sanal router oluşturma
- Otomatik yedeklilik
- Yüksek erişilebilirlik
- Hızlı failover

## HSRP Bileşenleri
### Active Router
- Aktif router
- Trafiği yönlendirir
- Hello mesajları gönderir
- Öncelik değeri yüksek

### Standby Router
- Yedek router
- Aktif router'ı izler
- Hızlı geçiş yapar
- İkinci öncelik

### Virtual Router
- Sanal IP adresi
- Sanal MAC adresi
- İstemciler için tek nokta
- 0000.0C07.ACXX formatı

## HSRP Yapılandırması
- Grup numarası
- Sanal IP adresi
- Öncelik değeri
- Preempt
- Authentication

## HSRP Komutları
- standby
- show standby
- show standby brief
- debug standby
- show standby all 