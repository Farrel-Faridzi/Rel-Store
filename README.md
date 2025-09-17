### Repo: https://github.com/Farrel-Faridzi/Rel-Store
### Web: https://farrel-faridzi-relstore.pbp.cs.ui.ac.id

---

# Tugas 3

# Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

### Data delivery = cara dan mekanisme pengiriman data antar-komponen (frontend↔backend, microservices↔microservices, eksternal↔platform). Kita butuh karena:

- Decoupling & scalability — memisahkan pengirim dan penerima (mis. frontend vs backend, service A vs B) supaya masing-masing bisa diskalakan, di-deploy, dan di-develop terpisah.

- Reliability & resiliency — mekanisme seperti message queue (Kafka, RabbitMQ) memungkinkan retry, buffering, dan toleransi gangguan.

- Latency & UX — beberapa kasus membutuhkan real-time (WebSocket/SSE) untuk UX responsif; lainya cukup batch/REST.

- Contract & backward-compatibility — data contract (schema/OpenAPI/JSON Schema) membantu evolusi API tanpa merusak client.

- Security & governance — centralisasi aturan autentikasi, validasi, enkripsi, dan audit trail saat data dikirim.

- Observability — tracing, metrics, logging pada jalur pengiriman memudahkan debugging/performance tuning.


# Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

### JSON: lebih ringan, langsung cocok dengan JavaScript (JSON.parse), mudah dibaca, banyak tooling modern (REST/SPA), payload lebih kecil => populer untuk web API.

### XML: lebih verbose, punya fitur kompleks (namespaces, atribut, XSD, XSLT) => unggul untuk dokumen yang kompleks/terstruktur dan kebutuhan enterprise/legacy (SOAP, dokumen hukum/finance).

Mengapa JSON lebih populer:

- Natural fit untuk web/JS sehingga integrasi front-end lebih mudah.

- Sederhana: format objek/array langsung ter-mapping ke struktur bahasa pemrograman.

- Payload umumnya lebih kecil; parsingnya cepat di browser/server modern.

- Ekosistem RESTful APIs dan microservices mengadopsi JSON sebagai standar de-facto.

- Tooling modern (fetch, axios, banyak library) bekerja mulus dengan JSON.


# Jelaskan fungsi dari method ```is_valid()``` pada form Django dan mengapa kita membutuhkan method tersebut?

### Apa yang dilakukan form.is_valid():

- Memanggil full_clean() pada form.

- Untuk tiap field: konversi tipe (to_python), validators, dan pembersihan (clean_<field>).

- Menjalankan clean() tingkat form (cross-field validation).

- Mengisi form.cleaned_data jika valid, atau form.errors jika tidak.

- Mengembalikan True/False.

### Kenapa fungsi ```is_valid()``` dibutuhkan:

- Mencegah pemrosesan input buruk — jangan pernah memakai ```cleaned_data``` tanpa ```is_valid()```; kalau tidak valid, data belum tervalidasi/terkonversi.

- Menjaga integritas dan keamanan — validasi tipe, panjang, pola, nilai unik, dsb.

- UX — ```form.errors``` memberi feedback ke user.

- Integrasi dengan ModelForm — ```is_valid()``` memastikan data bisa dipakai untuk ```form.save()```.


# Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

### CSRF (Cross-Site Request Forgery) = penyerang membuat permintaan (biasanya POST/state-changing) ke aplikasi target menggunakan browser korban yang sudah terautentikasi. Browser otomatis mengirim cookie (session) sehingga permintaan tampak sah.

### Kenapa csrf_token diperlukan:

- Token yang disisipkan ke form/template bersifat unik/rahasia untuk sesi dan diverifikasi oleh server lewat CsrfViewMiddleware.

- Memastikan request berasal dari halaman yang benar (bukan dari situs luar).

### Jika tidak menambahkan csrf_token:

- Pada Django default, middleware akan menolak POST tanpa token (403). Jika kamu menonaktifkan CSRF atau menandai view @csrf_exempt, aplikasi menjadi rentan.

- Risiko nyata: penyerang bisa memaksa user melakukan aksi yang merugikan (mengubah email/password, mengirimkan transaksi, mem-post konten atas nama user, dll).


# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Pertama saya menambahkan ```base.html``` ke direktori ```templates``` pada root folder dan memasukkanya ke var ```TEMPLATES``` di settings.py sebagai template dasar untuk halaman web lainnya.

2. Kemudian saya membuat berkas ```forms.py``` untuk membuat struktur form yang menerima data product baru di direktor ```main```, serta mengimport berkas ini ke ```views.py```.

3. Kemudian saya menambahkan fungsi ```create_product``` dan ```show_product``` di ```views.py``` untuk membuat atau melihat product. Lalu saya import kedua fungsi tersebut ke ```urls.py``` dan juga menambahkan path url baru untuk kedua fungsi tersebut.

4. Saya juga mengupdate code di ```main.html``` untuk menampilkan data product serta tombol ```Add product``` yang akan redirect ke laman form.

5. Kemudian saya membuat berkas ```create_product.html``` dan ```prouct_detail.html``` sebagai halaman untuk membuat dan menampilkan data product.

6. Saya juga tidak lupa untuk menambahkan entri url proyek pws ke ```CSRF_TRUSTED_ORIGINS``` di ```settings.py```.

7. Kemudian saya membuat melakukan test dengan menambahkan product baru.

8. Lalu saya membuat dua fungsi yaitu: ```show_xml``` dan ```show_json``` yang return function berupa ```HttpResponse``` yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML atau JSON.

9. Lalu saya membuat dua fungsi lagi yaitu: ```show_xml_by_id``` yang juga return function berupa ```HttpResponse``` yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML atau JSON, namun menyimpan hasil query dari data dengan id tertentu yang terdapat di ```Product```. Saya juga menambahkan try except block untuk antisipasi error ```Product.DoesNotExist```.

10. Kemudian saya mengimport 4 fungsi tersebut ke ```urls.py``` dan menambahkannya ke ```urlpatterns```.

#  Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Asdos sangat membantu saat saya bingung membuat tutorial kali ini lebih lancar bagi saya.

# Screenshot hasil akses URL pada Postman:
 
### XML
<img width="1129" height="941" alt="image" src="https://github.com/user-attachments/assets/210f3795-5e87-4ef1-8459-971d24f60fc0" />

### JSON
<img width="1109" height="932" alt="image" src="https://github.com/user-attachments/assets/a04c91e4-28b2-43c9-8ac6-eebcb7461aee" />

### XML by ID
<img width="1118" height="925" alt="image" src="https://github.com/user-attachments/assets/3485c587-afab-4efd-a584-a3854dbde600" />

### JSON by ID
<img width="1128" height="931" alt="image" src="https://github.com/user-attachments/assets/dfbbd892-ae9c-4e34-aacb-d9c344ea9f71" />


