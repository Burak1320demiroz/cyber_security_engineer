# Burp Suite

## Temel Modüller

| Menü       | Ana Modüller               |
|------------|----------------------------|
| Burp       | Dashboard                  |
| Project    | Target                     |
| Intruder   | Proxy, Intruder            |
| Repeater   | Repeater, Sequencer        |
| Window     | Decoder, Comparer          |
| Help       | -                          |

## Modül Detayları

### Target
- Hedef uygulamanın içerik ve fonksiyonlarını analiz etmek için kullanılır
- Site haritası oluşturma ve hedef kapsamını belirleme özellikleri sunar

### Proxy
- Burp suite içerisinde en çok kullanılan modüllerden birisidir. Client ile server arasında istekleri inceleyip değiştirmek için kullanılır.
- Client-server arasındaki trafiği:
  - Yakalar (intercept)
  - İnceler
  - Değiştirir
- Manuel güvenlik testleri için ideal

### Scanner
- Hedef web uygulama üzerinde otomatize zafiyet taraması gerçekleştirmeye yardımcı olan modüldür.
- Otomatik web uygulama zafiyet taraması yapar
- SQL Injection, XSS gibi yaygın açıkları tespit eder

### Intruder
- Hedef web uygulamaya otomatize saldırı senaryoları oluşturmak ve spesifik saldırı tekniklerini test etmek için kullanılır.
- Otomatize saldırı senaryoları oluşturur
- Brute-force, fuzz test gibi teknikler uygular
- Parametre bazlı özelleştirilebilir saldırılar

### Repeater
- HTTP isteklerini inceleyebilmeyi, istekler üzerinde değiştirme yapmayı ve bu değişikliğin uygulamada nasıl yorumlandığını görmemizi sağlayan basit ama işlevsel bir modül
- HTTP isteklerini:
  - Tekrar gönderir
  - Değiştirir
  - Sonuçları karşılaştırır
- API testleri için kullanışlı

### Sequencer
- Veri örnekleminde rastgelelik kalitesini analiz etmek için bir araçtır. Oturum tokenları, anti-CSRF tokenlar gibi rastgele olması gereken parametrelerin kalitesini ölçmede yararlanılır.
- Rastgelelik analiz aracı
- Token'ların (session, CSRF) entropisini ölçer
- Güvenlik açısından tahmin edilebilirliği test eder

### Decoder
- Kodlanmış verileri çözümlemek veya ham verileri çeşitli kodlanmış ve karma biçimlere dönüştürmek için basit bir araçtır.
- Veri dönüşümleri yapar:
  - Base64, URL, HTML encoding/decoding
  - Hash hesaplama (MD5, SHA1 vb.)
  - String format dönüşümleri

### Comparer
- Herhangi iki veri öğesi arasında karşılaştırma yapmak için kullanılan basit bir araçtır.
- İki veri setini karşılaştırır:
  - Byte-by-byte fark analizi
  - Kelime bazlı karşılaştırma
  - Hex görünümüyle inceleme
