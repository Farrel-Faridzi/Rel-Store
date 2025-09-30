### Repo: https://github.com/Farrel-Faridzi/Rel-Store
### Web: https://farrel-faridzi-relstore.pbp.cs.ui.ac.id

---

# Tugas 5

# Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Urutan prioritas CSS dari tinggi ke rendah:

1. ```Inline styles```
2. ```ID selector```
3. ```Class```, ```attribute```, dan ```pseudo-class selector```
4. ```Tag (element)``` dan ```pseudo-element selector```
5. Urutan deklarasi ```(Cascade)```
6. ```!important```


# Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Responsive design penting karena pengguna mengakses web melalui berbagai perangkat dengan ukuran layar berbeda. Dengan desain yang fleksibel, tampilan web tetap rapi, konten mudah dibaca, dan navigasi nyaman tanpa harus zoom manual. Selain meningkatkan pengalaman pengguna, responsive design juga mendukung SEO karena mesin pencari seperti Google memprioritaskan situs yang mobile-friendly.

Contoh aplikasi yang sudah menerapkan responsive design adalah Tokopedia, yang menampilkan grid produk berbeda antara desktop dan mobile sehingga tetap nyaman digunakan. Sebaliknya, beberapa portal akademik lama belum responsive, sehingga tabel dan menu sulit dibaca di layar ponsel karena harus scroll horizontal atau zoom manual, membuat pengalaman pengguna jadi kurang baik.


# Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Dalam CSS, elemen HTML digambarkan menggunakan box model. Tiga komponen penting yang sering dipakai adalah:


- Margin:

    Ruang di luar elemen.
    Mengatur jarak antar elemen agar tidak saling menempel.

- Border:

    Garis tepi yang membungkus elemen.
    Bisa diatur ketebalan, warna, dan gaya (solid, dashed, dotted, dll).

- Padding:

    Ruang di dalam elemen, antara konten (teks/gambar) dan border.
    Membuat konten tidak menempel langsung pada tepi elemen.

Contoh Implementasi:

```html```:

    <div class="box">
      Halo, ini contoh box model!
    </div>



```css```:

    .box {
        margin: 30px;             /* jarak luar elemen */
        border: 3px dashed blue;  /* garis tepi biru */
        padding: 20px;            /* jarak dalam sebelum konten */
    }
    
Hasilnya: elemen ```<div>``` memiliki jarak dari elemen lain (margin), dibungkus garis biru (border), dan teksnya punya ruang tambahan di dalam (padding).



# Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox (Flexible Box Layout) adalah sistem layout CSS yang dirancang untuk mengatur elemen dalam satu dimensi, baik secara horizontal (row) maupun vertikal (column). Kegunaannya terutama untuk membuat tata letak yang fleksibel dan mudah diatur seperti navbar, card list, atau alignment (tengah, kanan, rata). Misalnya, dengan ```display: flex; justify-content: center; align-items: center;```, kita bisa langsung membuat konten berada di tengah layar.

Grid Layout adalah sistem layout dua dimensi di CSS yang memungkinkan kita mengatur elemen berdasarkan baris dan kolom. Kegunaannya lebih cocok untuk membuat struktur halaman yang kompleks, seperti layout dashboard, galeri foto, atau template web dengan banyak bagian. Dengan ```display: grid; grid-template-columns: repeat(3, 1fr);```, misalnya, kita bisa langsung membuat tiga kolom yang sama besar.


# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1. Pertama saya menambahkan ```<meta name="viewport">``` di ```base.html``` agar web dapat menyesuaikan ukuran dan perilaku perangkat mobile. Kemudian saya menambahkan script CDN dari tailwind di file yang sama.

2. Lalu saya menambahkan fitur ```edit_product``` dan ```delete_product``` di ```views.py```, kemudian membuat berkas baru ```edit_product.html```. Setelah itu, saya mengimport fungsi edit ke ```urls.py``` dan menambahkan url path baru untuk edit produk. Saya juga menambahkan tombol edit dan delete produk di ```main.html```.

3. Kemudian saya konfigurasi static files menambahkan middleware WhiteNoise pada ```settings.py```, dan juga konfigurasi seperti ini :

            STATIC_URL = '/static/'
        if DEBUG:
            STATICFILES_DIRS = [
                BASE_DIR / 'static' # merujuk ke /static root project pada mode development
            ]
        else:
            STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production

4. Setelah itu, saya membuat berkas ```global.css``` di ```/static/css``` untuk custom styling css. Menambahkan script tailwind dan link stylesheet ke berkas ```global.css``` di ```base.html```.

5. Terakhir, saya melakukan styling dengan menambahkan berkas ```navbar.html```, ```card_product.html```, dan memodifikasi berkas ```login.html```, ```register.html```, ```edit_product.html```, ```main.html```, ```product_detail.html```, ```create_product``` agar cocok dengan tema toko olahraga Rel Store.