# HTTP (Hypertext Transfer Protocol)

- Web üzerindeki istemci (tarayıcı) ile sunucu arasında veri iletişimini sağlayan bir protokoldür. 
- Temel amacı, web sayfalarının metin, resim, video ve diğer içeriklerinin istemciye iletilmesini sağlamaktır.
- Uygulama seviyesinde bir iletişim protokolüdür
- İstemci (client) ve sunucu (server)
- İstek (request) 
- Cevap (response)
- İki bölümden oluşur; Header ve Body

-------------------------------------

- HTTP Metotları
    - GET: Veri okuma
    - POST: Veri gönderme/oluşturma
    - PUT/PATCH: Veri güncelleme/değiştirme
    - DELETE: Bir kaynağı silmek için kullanılır.
    - HEAD: GET ile aynı ancak sadece başlık döner
    - OPTIONS: İzin verilen HTTP metotlarını döndürür

-------------------------------------

- HTTP Durum Kodları (HTTP Status Codes)
    - Başarı (2xx)
        - 200 OK → İstek başarıyla işlendi.
        - 201 Created → Yeni bir kaynak oluşturuldu.
    - Yönlendirme (3xx)
        - 301 Moved Permanently → Kalıcı yönlendirme.
        - 302 Found → Geçici yönlendirme.
    - İstemci Hataları (4xx)
        - 400 Bad Request → Geçersiz istek.
        - 401 Unauthorized → Kimlik doğrulama gerekli.
        - 403 Forbidden → Erişim izni yok.
        - 404 Not Found → Kaynak bulunamadı.
    - Sunucu Hataları (5xx)
        - 500 Internal Server Error → Sunucuda bir hata oluştu.
        - 503 Service Unavailable → Sunucu şu anda hizmet veremiyor.

# HTTPS (Hypertext Transfer Protocol Secure)
- HTTP protokolünün güvenli versiyonudur. SSL/TLS şifreleme protokollerini kullanarak veri iletimini şifreler ve kullanıcı ile sunucu arasındaki iletişimi korur.