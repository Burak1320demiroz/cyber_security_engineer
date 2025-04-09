# DOM (Document Object Model)

###### DOM Nedir?
- DOM, Javascript gibi diller ile etkileşim sağlayan bir API dır.
- Tarayıcılar üzerinden görüntülediğimiz internet sayfaları birer belge ve bu belgedeki her bir eleman da bir nesnedir.
- Tarayıcıların sunucudan aldığı HTML belgesini işleyerek oluşturduğu hiyerarşik nesne yapısıdır.
- Her HTML elementi (başlık, paragraf, bağlantı vb.) bir nesne (object) olarak temsil edilir.
- JavaScript gibi diller, DOM üzerinden bu nesneleri değiştirerek sayfanın dinamik olarak güncellenmesini sağlar.
- Tarayıcı, sunucudan dönen HTML’i parse eder, javascript ve CSS’leri de yorumlayarak DOM yapısını oluşturur.

###### DOM'un Oluşumu
1. Tarayıcı, sunucudan gelen HTML'i parse eder (ayrıştırır)
2. CSS ve JavaScript dosyalarını yorumlar
3. Tüm elemanları ağaç (tree) yapısında düzenleyerek DOM'u oluşturur

###### DOM Yapısı Örneği
```html
Document (Kök)  
│  
└── <html>  
    ├── <head>  
    │   └── <title> → Metin: "My title"  
    └── <body>  
        ├── <a href="..."> → Metin: "My link"  
        └── <h1> → Metin: "My header"

- Document: En üstteki kök nesne
- Elementler: html, head, body gibi HTML tag'leri.
- Attribute (Özellikler): Örneğin, a elementinin href değeri.
- Metin İçerikleri: Elementlerin içindeki yazılar (örneğin, title'daki "My title").
