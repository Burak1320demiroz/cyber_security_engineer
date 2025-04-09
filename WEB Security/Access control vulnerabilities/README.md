# Access control vulnerabilities
- Erişim kontrolü, bir uygulama veya sistemde kaynaklara kimin ve hangi eylemleri gerçekleştirmeye yetkili olduğunu belirleyen kısıtlamalardır. Web uygulamaları bağlamında, erişim denetimi kimlik doğrulama ve oturum yönetimi ile ilişkilidir. Kimlik doğrulama, kullanıcının söylediği kişi olup olmadığını doğrularken, oturum yönetimi, kullanıcının sonraki isteklerini takip eder. Erişim denetimi, kullanıcının belirli bir kaynağa veya işlevselliğe erişip erişemeyeceğini belirler.
###### Erişim Kontrolü Türleri:
- Dikey Erişim Kontrolleri: Belirli kullanıcı türlerine, hassas işlevlere erişim izni verir. Örneğin, bir yönetici herhangi bir kullanıcının hesabını değiştirebilirken, sıradan bir kullanıcı bu işlevlere erişemez.
- Yatay Erişim Kontrolleri: Aynı türdeki kaynaklara erişimi belirli kullanıcılara sınırlar. Örneğin, bir bankacılık uygulaması, kullanıcının sadece kendi hesabındaki işlemleri görüntülemesine izin verir.
- Bağlam Bağımlı Erişim Denetimleri: Uygulamanın durumu veya kullanıcının uygulama ile etkileşimine bağlı olarak kaynaklara erişim sınırlandırılır. Örneğin, ödeme işlemi yapıldıktan sonra sepetin içeriği değiştirilemez.
###### Bozuk Erişim Kontrollerine Örnekler:
- Dikey Ayrıcalık Yükseltme: Bir kullanıcı, yönetici yetkilerine sahip olmadan yönetici işlevlerine erişebiliyorsa.
- Korumasız İşlevsellik: Bir kullanıcı, gizli URL'ler veya yönetici işlevlerine erişim sağlayabilir.
- Parametre Tabanlı Erişim Kontrolü: Kullanıcıların rolü veya erişim hakları, URL parametrelerinde veya çerezlerde saklanıyorsa ve kullanıcı bu parametreleri değiştirebiliyorsa.

-------------------------------------

