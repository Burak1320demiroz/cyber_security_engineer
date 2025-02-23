# Ros2 Humble

-------------------------------------

(  ...~$ export TURTLEBOT3_MODEL=burger )

- export ==> Terminalde bir çevre değişkeni (environment variable) tanımlamak için kullanılır.
- TURTLEBOT3_MODEL değişkenine "burger" değerini atar.

Nasıl Çalışır?
- ROS 2, hangi TurtleBot3 modelinin kullanılacağını buradan öğrenir.
- TurtleBot3'ün üç modeli vardır:
    burger → Küçük ve hafif model.
    waffle → Daha büyük ve güçlü model, daha fazla sensör var.
    waffle_pi → Raspberry Pi tabanlı versiyon.

-------------------------------------

(  ...~$ ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py )

- ros2 launch → ROS 2'de bir launch dosyası çalıştırmaya yarar.
- turtlebot3_gazebo → TurtleBot3'ün Gazebo simülasyonu için gerekli paketin adı.
- turtlebot3_world.launch.py → TurtleBot3'ü Gazebo ortamında başlatan Python tabanlı bir launch dosyası.

Nasıl Çalışır?
- Gazebo Simülatörü Açılır ==> Sanal bir dünya ve içinde TurtleBot3 robotu yüklenir.
- Robotun Sensörleri ve Motorları Simüle Edilir ==> Lidar, kamera, motor gibi bileşenler simülasyon ortamında aktif olur.
- ROS 2 Düğümleri Başlatılır ==> Robotun hareketi, sensör verileri ve kontrol mekanizmaları devreye girer.

-------------------------------------

(  ...~$ echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc )

- echo  ==> "export TURTLEBOT3_MODEL=burger" komutunu ekrana yazdırır.
- >> ~/.bashrc  ==> Bu komutun çıktısını ~/.bashrc dosyasının sonuna ekler
- ~/.bashrc  ==> terminal açıldığında otomatik çalıştırılan bir betik dosyadır.

-------------------------------------

(  ...~$ source ~/.bashrc )

- source  ==> belirtilen dosyanın içeriğini mevcut terminal oturumuna yükler.
~/.bashrc dosyasındaki değişikliklerin hemen geçerli olmasını sağlar.

-------------------------------------
