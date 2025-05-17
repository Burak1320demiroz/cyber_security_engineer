# QoS (Quality of Service)

QoS, ağ trafiğini önceliklendirmek ve yönetmek için kullanılan bir mekanizmadır. Farklı uygulamaların ihtiyaçlarına göre trafik yönetimi sağlar.

## QoS Modelleri
### Best Effort
- Öncelik yok
- FIFO kuyruk
- Basit yapı
- Varsayılan model

### Integrated Services
- Garantili servis
- Resource reservation
- RSVP protokolü
- End-to-end QoS

### Differentiated Services
- Trafik sınıflandırma
- Marking
- Policing
- Shaping

## QoS Mekanizmaları
### Classification
- ACL
- NBAR
- CoS
- DSCP
- IP Precedence

### Marking
- CoS (802.1p)
- DSCP
- IP Precedence
- MPLS EXP
- QoS Group

### Policing/Shaping
- Rate limiting
- Traffic shaping
- Burst control
- Buffer management

## QoS Yapılandırması
- Policy map
- Class map
- Service policy
- Queue management
- WRED

## QoS Komutları
- class-map
- policy-map
- service-policy
- show policy-map
- show class-map
- show policy-map interface
- debug qos 