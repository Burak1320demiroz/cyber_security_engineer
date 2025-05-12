# Docker

###  **Docker Başlatma ve İmaj İşlemleri**
```bash
systemctl --user start docker-desktop     # Docker'ı başlat
docker pull ubuntu                        # Ubuntu imajını indir
docker images                             # Yüklü imajları göster
```

---

###  **Container Oluşturma ve Yönetimi**
```bash
docker run redis                          # Redis container başlat
docker run ubuntu                         # Ubuntu container başlat (varsayılan)
docker run -it ubuntu                     # Etkileşimli Ubuntu terminali
exit                                      # Container'dan çık
docker ps                                 # Çalışan container'ları listele
docker ps -a                              # Tüm container'ları listele (çalışan + durdurulmuş)
docker container ls -a                    # Aynı şekilde tüm container'ları gösterir
```

---

###  **İsimlendirme ve Başlatma**
```bash
docker run -it --name bash_ubuntu ubuntu     # 'bash_ubuntu' adında container
docker start bash_ubuntu                     # Container'ı başlat
docker stop bash_ubuntu                      # Container'ı durdur
docker rm bash_ubuntu                        # Container'ı sil
docker container rm $(docker container ls -aq)  # Tüm container'ları sil
```

---

###  **Farklı Sürümler ve Etiketleme**
```bash
docker run redis:7                           # Redis 7 imajını çalıştır
docker image tag ubuntu my-ubuntu            # 'ubuntu' imajını 'my-ubuntu' olarak etiketle
```

---

### **Arka Planda Çalıştırma ve Erişim**
```bash
docker run -d redis                          # Redis container'ı arka planda başlat
docker attach <id>                           # ID ile container’a bağlan
```

---

###  **Dockerfile'dan Build Etme ve Port Açma**
```bash
docker build -t ctf-2 .                      # Dockerfile'dan imaj oluştur
docker run -d -p 8080:8080 ctf-2             # Port yönlendirmeyle çalıştır
docker run -d -m 2g -p 8080:8080 ctf-2       # 2 GB bellek limitiyle çalıştır
```

---

### **Logları Görüntüleme**
```bash
docker logs <container_name_or_id>          # Logları göster (örn: jovial_kepler)
```
