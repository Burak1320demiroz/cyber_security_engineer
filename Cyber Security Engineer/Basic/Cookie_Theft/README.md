# Cookie Theft (Çerez Hırsızlığı)

##### Gereksinimler

- Kali Linux veya Parrot OS gibi bir pentest dağıtımı
- Wireshark veya Tcpdump gibi ağ trafiği analiz araçları
- Mitmproxy veya Bettercap gibi Man-in-the-Middle (MitM) saldırı araçları
- Hedef cihazın HTTP üzerinden giriş yaptığı bir site (HTTPS siteleri için ek önlemler gerekebilir)
- ARP Spoofing veya DNS Spoofing için ettercap veya arpspoof

-------------------------------------

##### Senaryo Adımları

- ARP Spoofing ile Trafiği Yönlendirme, Hedef cihazın tüm internet trafiğini kendi sistemine yönlendirmek için ARP Spoofing yapabilirsin.
    - arpspoof -i wlan0 -t [Hedef_IP] -r [Modem_IP] : Bu komut, hedefin modem yerine seni görmesini sağlayarak araya girmeni sağlar.

- HTTP Trafiğini İzleme, Eğer hedef site HTTP kullanıyorsa, Wireshark veya tcpdump ile çerezleri yakalayabilirsin.
    - tcpdump -i wlan0 -A | grep "Cookie:" veya Wireshark açıp "http.cookie" filtresiyle çerezleri görebilirsin.

- 
