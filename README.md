### Repo: https://github.com/Farrel-Faridzi/Rel-Store
### Web: https://farrel-faridzi-relstore.pbp.cs.ui.ac.id

---

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### 1. Membuat project Django baru
Hal pertama yang saya lakukan adalah membuat git repository baru. Setelah itu saya membuat project Django baru bernama Rel-Store dengan memasukkan command ```django-admin startproject Rel_Store.``` di terminal.

### 2. Setup environment & project awal
Saya membuat file ```.env``` dan ```.env.prod``` untuk menyimpan konfigurasi penting. selain itu, juga mengaktifkan virtual environment, kemudian menginstall semua dependency yang dibutuhkan melalui ```requirements.txt``` dan membuat file ```.gitignore``` agar semua file yang kurang penting tidak di push ke repository.

### 3. Konfigurasi settings.py
Saya memodifikasi file ```settings.py``` pada directory ```Rel_Store``` untuk mengkonfigurasi database agar sesuai dengan yang tertera di tutorial (mengubah database, menambahkan variable ```PRODUCTION```, etc.). Kemuidian jika saya ingin deploy ke ```PWS```, saya juga memasukkan URL baru ke dalam ```ALLOWED_HOSTS``` supaya aplikasi dapat di host melalui ```PWS```, da dapat diakses publik.

### 4. Setup URL
Di dalam ```main/urls.py```, saya mendefinisikan path yang menghubungkan URL dengan fungsi ```home_page```. Dari sini, URL tersebut juga diarahkan ke template HTML (misalnya ```home.html```) untuk menampilkan tampilan frontend.

### 5. Membuat view dan template
Di file ```main/views.py```, saya membuat fungsi home_page untuk menampilkan halaman awal aplikasi. Halaman awal ini berisi nama toko saya serta informasi identitas diri (nama, npm dan kelas).

### 6. Membuat model
Pada ```main/models.py```, saya membuat sebuah model Django bernama Product yang memiliki atribut sesuai kebutuhan Tugas 1. Selain itu, saya menambahkan atribut ```views``` untuk mengetahui berapa kali sebuah produk di lihat oleh pengguna dan ```id``` sebagai penanda produk dalam bentuk ```UUID```.

### 7. Setup Git dan Deploy ke PWS
Saya sudah melakukan inisialisasi Git repository, kemudian push project ke ```PWS```. Setelah itu, saya juga deploy project ke GitHub Setelah memastikan aplikasi berjalan dengan baik, saya melakukan penyesuaian terakhir pada ````settings.py``` (menambahkan ```ALLOWED_HOSTS```), lalu melakukan push ulang ke GitHub dan ```PWS``` agar perubahan tersebut ter-deploy.

### 8. Membuat README.md
Terakhir, saya membuat file ```README.md``` yang berisi dokumentasi proyek. File ini mencakup link menuju repository GitHub, link aplikasi PWS, serta jawaban dari pertanyaan yang diberikan. Setelah itu, saya kembali melakukan push agar file ```README.md``` tersimpan di repository.

---

# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara ```urls.py```, ```views.py```, ```models.py```, dan berkas ```html```.

<img width="1350" height="650" alt="image" src="https://github.com/user-attachments/assets/fd63449b-4aec-4089-8e50-8cdf1e3562bc" />

Bagan di atas menunjukkan alur request–response pada aplikasi Django. Ketika client mengirim request, request tersebut pertama kali diarahkan ke ```urls.py``` untuk mencocokkan URL dengan fungsi view yang sesuai. Selanjutnya, ```views.py``` bertugas mengolah logika: jika butuh data, view akan berinteraksi dengan ```models.py``` untuk mengambil atau memodifikasi data di database. Setelah data tersedia, view akan memanggil template HTML untuk menampilkan data dalam bentuk yang terstruktur. Akhirnya, hasil render dikirim kembali sebagai response kepada client. Dengan demikian, keempat berkas ini saling berhubungan dalam memproses request hingga menghasilkan response.

---

# Jelaskan peran ```settings.py``` dalam proyek Django!
File ```settings.py``` berfungsi sebagai pusat konfigurasi untuk proyek Django. Semua pengaturan utama proyek, seperti database, aplikasi yang digunakan (```INSTALLED_APPS```), ```middleware```, ```template```, ```static files```, keamanan (secret key, debug mode), serta daftar host yang diizinkan (```ALLOWED_HOSTS```) didefinisikan di sini.

Dengan kata lain, ```settings.py``` mengatur bagaimana aplikasi Django dijalankan dan berinteraksi dengan server, database, maupun pengguna.

---

# Bagaimana cara kerja migrasi database di Django?
Migrasi database di Django adalah proses yang menghubungkan perubahan pada model di ```models.py``` dengan struktur tabel di database. Ketika kita membuat atau mengubah model, Django menghasilkan file migrasi dengan perintah ```makemigrations``` yang berisi instruksi perubahan, lalu perintah ```migrate``` digunakan untuk menerapkan instruksi tersebut ke database. Dengan mekanisme ini, Django memastikan struktur database selalu sinkron dengan model tanpa perlu menulis query SQL secara manual.

---

# Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django dipilih sebagai permulaan pembelajaran pengembangan perangkat lunak karena framework ini bersifat ```batteries``` included, artinya sudah menyediakan banyak fitur bawaan seperti autentikasi, manajemen database, admin panel, hingga sistem routing tanpa harus menginstal banyak library tambahan. Django juga menggunakan pola arsitektur ```Model-View-Template``` yang membantu mahasiswa memahami konsep pemisahan logika, data, dan tampilan dalam aplikasi. Selain itu, Django ditulis dengan Python yang sintaksnya sederhana dan mudah dipahami, sehingga lebih ramah bagi pemula untuk mempelajari konsep fundamental dalam pengembangan web dan perangkat lunak secara umum.

---

# Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Karena lab yang dilakukan Tutorial 1 dilakukan secara daring, jadi saya tidak banyak berinteraksi dengan asisten dosen. Saya hanya berinteraksi sekali ketika program saya menampilkan error message, dan ketika saya bertanya ke salah satu asisten dosen. Beliau dapat membantu saya hingga program saya dapat berjalan tanpa ada error.
