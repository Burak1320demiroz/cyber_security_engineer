# Kali Linux - Temel Komutlar Rehberi

## Paket Yönetimi
```bash
apt-get clean      - Kullanılmayan paket dosyalarını siler (depo temizliği)
apt-get update     - Paket listesini yeniler (güncel veritabanı)
apt-get upgrade    - Tüm yüklü yazılımları günceller
```

## Dosya/Dizin İşlemleri
```bash
ls       - Dizindeki dosyaları listeler
  ls -l   - Detaylı listeleme (izinler, boyut, tarih)
  ls -la  - Gizli dosyalar dahil tam liste

cd       - Dizin değiştir
  cd ..  - Bir üst dizine çık

mkdir    - Yeni klasör oluştur
touch    - Yeni dosya oluştur
rm -r    - Dosya/klasör sil (recursive)
cp       - Kopyalama yapar
mv       - Taşır veya yeniden adlandırır
```

## Sistem Bilgileri
```bash
uname -a  - Sistem ve çekirdek bilgileri
whoami    - Aktif kullanıcıyı gösterir
pwd       - Bulunulan dizin yolunu gösterir
```

## Metin İşlemleri
```bash
cat       - Dosya içeriğini göster
  cat -n  - Satır numaralarıyla göster
head      - Dosyanın ilk 10 satırını göster
```

## Sistem İzleme
```bash
free -h   - Bellek kullanımı
top/htop  - Sistem kaynak takibi
df -h     - Disk kullanımı
ncdu      - Disk analiz aracı
```

## Diğer Yararlı Komutlar
```bash
clear     - Ekranı temizle
history   - Komut geçmişi
ctrl+c    - İşlemi durdur
wc        - Satır/kelime/karakter sayımı
```
