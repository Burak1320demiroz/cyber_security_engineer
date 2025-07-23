### 🐳 **Docker Komutları – Sık Kullanılanlar (Temizlenmiş & Genelleştirilmiş)**

####  Docker Servisi ve İmaj İşlemleri

```bash
systemctl start docker                            # Docker servisini başlat (Linux için)
docker pull <image>                               # İmaj indir (örn: ubuntu, redis)
docker images                                     # Mevcut imajları listele
docker rmi <image_id|image_name>                  # Belirli imajı sil
docker rmi $(docker images -q)                    # Tüm imajları sil
```

---

####  Container Oluşturma, Çalıştırma ve Yönetim

```bash
docker run <image>                                # Basit container başlat
docker run -it <image>                            # Etkileşimli terminal ile başlat
docker run -d <image>                             # Arka planda çalıştır
docker run --name <name> <image>                  # İsim vererek container başlat
docker start <name|id>                            # Durdurulmuş container’ı başlat
docker stop <name|id>                             # Container'ı durdur
docker restart <name|id>                          # Container'ı yeniden başlat
docker rm <name|id>                               # Container sil
docker rm $(docker ps -aq)                        # Tüm container'ları sil
docker ps                                         # Çalışan container’ları listele
docker ps -a                                      # Tüm container’ları (çalışan + duran) listele
```

---

####  Port, Network ve Environment Ayarları

```bash
docker run -p <host_port>:<container_port> <image>              # Port yönlendirme
docker run --network host <image>                               # Host ağı kullan
docker run -e VAR=value <image>                                 # Ortam değişkeni ile başlat
docker run -v <host_path>:<container_path> <image>              # Volume (dizin) bağlama
```

---

####  Dockerfile ile İmaj Oluşturma (Build)

```bash
docker build -t <image_name> .                                  # Dockerfile'dan imaj oluştur
```

---

####  Kayıt ve Arşivleme (.tar ve GPG)

```bash
docker save -o <file.tar> <image>                               # İmajı .tar dosyası olarak kaydet
docker load -i <file.tar>                                       # .tar imajını yükle
gpg -c <file.tar>                                               # GPG ile dosyayı şifrele
gpg --output <file.tar> --decrypt <file.tar.gpg>                # Şifrelenmiş dosyayı çöz
tar -xvf <file.tar>                                             # .tar dosyasını çıkar
```

---

####  Loglar, Erişim ve Etiketleme

```bash
docker logs <name|id>                                           # Logları görüntüle
docker attach <name|id>                                         # Container'a bağlan
docker exec -it <name|id> bash                                  # Çalışan container'da terminale gir
docker tag <image> <new_name:tag>                               # İmaj etiketle
```

---

####  Kullanıcı Ayarları (Docker komutlarını sudo'suz kullanmak için)

```bash
sudo usermod -aG docker $USER
newgrp docker
```

---

####  Ekstra: ROS Uygulamaları için Örnek Docker Komutu

```bash
docker run -it --network=host \
  -e ROS_MASTER_URI=http://<master_ip>:11311 \
  -e ROS_IP=<local_ip> \
  <image_name>
```

---