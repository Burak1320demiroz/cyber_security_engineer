# /robots.txt

- robots.txt, bir web sitesinin kök dizininde bulunan ve arama motoru botlarına (örneğin, Googlebot, Bingbot) hangi sayfaların veya dizinlerin taranıp taranamayacağını belirten bir metin dosyasıdır. Bu dosya, web sitesinin SEO yönetimi ve gizlilik politikaları için önemlidir.
-------------------------------------
###### Örnek bir robots.txt dosyası şu şekilde olabilir ==> 
- User-agent: 
- Disallow: /private/
- Allow: /public/
###### Burada ==> 
- User-agent: * ifadesi, tüm arama motoru botlarını ifade eder.
- Disallow: /private/ ifadesi, /private/ dizinine botların erişmesini engeller.
- Allow: /public/ ifadesi, /public/ dizinine botların erişmesine izin verir.
-------------------------------------
- robots.txt dosyası, web sayfasının arama motorları tarafından nasıl taranacağını kontrol etmek için kullanılır, ancak arama motorları bu dosyayı zorunlu olarak dikkate almazlar
