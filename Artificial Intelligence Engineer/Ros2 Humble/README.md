# Ros2 Humble

-------------------------------------

### (  ...~$ export TURTLEBOT3_MODEL=burger )

- export ==> Terminalde bir çevre değişkeni (environment variable) tanımlamak için kullanılır.
- TURTLEBOT3_MODEL değişkenine "burger" değerini atar.
###### Nasıl Çalışır?
- ROS 2, hangi TurtleBot3 modelinin kullanılacağını buradan öğrenir.
- TurtleBot3'ün üç modeli vardır:
    burger → Küçük ve hafif model.
    waffle → Daha büyük ve güçlü model, daha fazla sensör var.
    waffle_pi → Raspberry Pi tabanlı versiyon.

-------------------------------------

### (  ...~$ ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py )

- ros2 launch → ROS 2'de bir launch dosyası çalıştırmaya yarar.
- turtlebot3_gazebo → TurtleBot3'ün Gazebo simülasyonu için gerekli paketin adı.
- turtlebot3_world.launch.py → TurtleBot3'ü Gazebo ortamında başlatan Python tabanlı bir launch dosyası.
###### Nasıl Çalışır?
- Gazebo Simülatörü Açılır ==> Sanal bir dünya ve içinde TurtleBot3 robotu yüklenir.
- Robotun Sensörleri ve Motorları Simüle Edilir ==> Lidar, kamera, motor gibi bileşenler simülasyon ortamında aktif olur.
- ROS 2 Düğümleri Başlatılır ==> Robotun hareketi, sensör verileri ve kontrol mekanizmaları devreye girer.

-------------------------------------

### (  ...~$ echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc )

- echo  ==> "export TURTLEBOT3_MODEL=burger" komutunu ekrana yazdırır.
- ~/.bashrc  ==> Bu komutun çıktısını ~/.bashrc dosyasının sonuna ekler
- ~/.bashrc  ==> terminal açıldığında otomatik çalıştırılan bir betik dosyadır.

-------------------------------------

### (  ...~$ source ~/.bashrc )

- source  ==> belirtilen dosyanın içeriğini mevcut terminal oturumuna yükler.
~/.bashrc dosyasındaki değişikliklerin hemen geçerli olmasını sağlar.

-------------------------------------

### (  ...~$ ros2 launch turtlebot3_bringup rviz2.launch.py )

- ros2 launch → ROS 2'de bir launch dosyası çalıştırmaya yarar.
- turtlebot3_bringup → TurtleBot3'ün temel bileşenlerini başlatan paket.
- rviz2.launch.py → RViz2'yi başlatan bir Python tabanlı launch dosyasıdır.

-------------------------------------

### (  ...~$ ros2 topic list )
- Bu komut, ROS 2 sisteminde mevcut olan tüm topic’leri listeler.

-------------------------------------

### (  ...~$ ros2 topic echo <topic_adi> )


### (  ...~$ ros2 topic echo /odom )

- nav_msgs/msg/Odometry
- Bu mesaj türü, robotun konum (position) ve hız bilgilerini (velocity) içeren odometri verisini tutar.

###### Çıktının İçeriği ==> 
- header.stamp	⇒  Mesajın zaman damgası
- header.frame_id  ⇒  Hangi çerçevede ölçüm yapıldığı ("odom")
- child_frame_id	  ⇒  Robotun tabanı ("base_footprint")
- pose.position  ⇒  Robotun dünya koordinatındaki konumu (x, y, z)
- pose.orientation  ⇒  Robotun yönelimi (dönme bilgisi)
- pose.covariance  ⇒  Konum ölçüm belirsizliği (hata matrisi)
- twist.linear ⇒ Robotun doğrusal hızı (x, y, z)
- twist.angular  ⇒  Robotun açısal hızı (x, y, z)
- twist.covariance  ⇒  Hız ölçüm belirsizliği (hata matrisi)

-------------------------------------

### (  ...~$ ros2 topic echo /point_cloud)

- sensor_msgs/msg/PointCloud2
- Bu mesaj türü, 3D nokta bulutları için kullanılır. Lidar veya stereo kameralar tarafından üretilen derinlik verilerini içerir.
- İçeriği ==>
    Header → Zaman damgası ve koordinat çerçevesi.
    Height & Width → Görüntünün veya nokta bulutunun boyutları.
    Point Fields → X, Y, Z koordinatları ve RGB renk bilgileri.
    Data → Ham nokta bulutu verisi.

-------------------------------------

### (  ...~$ ros2 topic echo /scan )

- sensor_msgs/msg/LaserScan
- Lidar veya lazer tarayıcıların ürettiği 2D mesafe verilerini içerir.
- İçeriği ==>
    Header → Zaman damgası ve koordinat çerçevesi.
    Angle_min & Angle_max → Tarama açısının başlangıç ve bitiş değerleri.
    Angle_increment → Tarama açısının çözünürlüğü.
    Range_min & Range_max → Lidar’ın ölçebileceği minimum ve maksimum mesafe.
    Ranges → Lidar’ın algıladığı mesafeler dizisi.

-------------------------------------

### (  ...~$ ros2 topic echo /camera/image_raw )

- sensor_msgs/msg/Image
- Kameralar tarafından çekilen görüntü verilerini içerir.
- İçeriği ==> 
    Header → Zaman damgası ve çerçeve bilgisi.
    Height & Width → Görüntü boyutları (piksel cinsinden).
    Encoding → Görüntü formatı (RGB, BGR, Mono8, vs.).
    Step → Satır başına düşen byte miktarı.
    Data → Ham görüntü verisi.

-------------------------------------

- nav_msgs/msg/Odometry	   __   Robotun konum ve hız bilgileri__Navigasyon, SLAM, AMCL
- sensor_msgs/msg/PointCloud2 __3D nokta bulutu verisi	      __3D haritalama, nesne tanıma
- sensor_msgs/msg/LaserScan __  2D lazer tarayıcı verisi	  __Engel algılama, SLAM
- sensor_msgs/msg/Image	   __   Kamera görüntü verisi	      __Görüntü işleme, nesne algılama

-------------------------------------

### (  ...~$ ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.2, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}" -r 10 )

- ros2 topic pub → ROS 2’de bir topic’e veri yayınlamak için kullanılır.
- /cmd_vel → Robotun hareket komutlarını aldığı topic’tir.
- geometry_msgs/msg/Twist → Gönderilen mesaj tipi.
- "{linear: {x: 0.2, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}" → Mesajın içeriği (hız bilgileri).
- -r 10 → Komutun 10 Hz (saniyede 10 kez) tekrar edilmesini sağlar.

-------------------------------------

source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
source ~/.bashrc
echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
echo 'source /usr/share/gazebo/setup.sh' >> ~/.bashrc