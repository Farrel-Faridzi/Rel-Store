### Repo: https://github.com/Farrel-Faridzi/Rel-Store
### Web: https://farrel-faridzi-relstore.pbp.cs.ui.ac.id

---

# Tugas 4

# Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

```AuthenticationForm``` di Django adalah form bawaan yang disediakan oleh ```django.contrib.auth.forms``` untuk menangani proses login pengguna dengan memverifikasi username dan password ke sistem autentikasi Django. Kelebihannya, form ini sudah siap pakai, terintegrasi penuh dengan model ```User```, aman karena otomatis melakukan validasi dan hashing password, serta mudah dikustomisasi jika butuh tambahan field atau styling. Namun, kekurangannya adalah fleksibilitasnya terbatas untuk kebutuhan autentikasi yang kompleks (misalnya login dengan email, OTP, atau third-party authentication), sehingga developer sering kali perlu membuat form kustom di luar ```AuthenticationForm``` untuk menyesuaikan dengan kasus penggunaan tertentu.


# Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Autentikasi adalah proses memverifikasi identitas pengguna (misalnya dengan username dan password), sedangkan otorisasi adalah proses menentukan hak akses atau izin pengguna terhadap suatu resource setelah identitasnya terverifikasi. Di Django, autentikasi diimplementasikan melalui sistem ```django.contrib.auth```, yang menyediakan model ```User```, form seperti ```AuthenticationForm```, serta backend autentikasi untuk memvalidasi kredensial. Sementara itu, otorisasi diimplementasikan dengan sistem permissions dan groups, di mana setiap ```User``` dapat memiliki izin tertentu (seperti ```add```, ```change```, ```delete```, ```view```) atau bergabung ke dalam grup dengan set izin tertentu, dan developer dapat mengeceknya menggunakan method seperti ```user.has_perm()``` atau ```user.is_superuser```.


# Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Cookies dan session sama-sama digunakan untuk menyimpan state di aplikasi web, tetapi punya perbedaan penting. Cookies disimpan di sisi klien (browser), sehingga ringan untuk server dan cocok untuk menyimpan data kecil seperti preferensi pengguna, namun rawan dimodifikasi atau dicuri jika tidak diamankan (misalnya tanpa enkripsi atau ```HttpOnly```/```Secure``` flag). Session disimpan di sisi server dengan hanya menyimpan session ID di cookies klien, sehingga lebih aman untuk data sensitif dan mudah dikontrol server (misalnya bisa kadaluarsa atau dihapus), tetapi menambah beban penyimpanan di server dan tidak skalabel jika jumlah pengguna sangat besar tanpa mekanisme khusus.


# Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Penggunaan cookies tidak sepenuhnya aman secara default, karena cookies bisa dicuri atau dimodifikasi melalui serangan seperti **XSS (Cross-Site Scripting)** atau session hijacking, apalagi jika tidak diberi proteksi tambahan. Risiko potensialnya termasuk pencurian identitas, akses ilegal ke akun, atau manipulasi data di sisi klien. Django menangani hal ini dengan memberikan beberapa proteksi bawaan: cookies session ditandatangani secara kriptografis sehingga tidak bisa dimodifikasi tanpa terdeteksi, developer dapat mengaktifkan flag keamanan seperti ```HttpOnly``` (mencegah akses JavaScript), ```Secure``` (hanya terkirim lewat HTTPS), dan ```SameSite``` (mencegah CSRF lewat cross-site request). Selain itu, Django juga memiliki middleware CSRF protection untuk mencegah penyalahgunaan cookies dalam permintaan berbahaya.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Pertama, saya membuat fungsi registrasi, login dan logout dengan import modules berikut di ```views.py``` :
    from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
    from django.contrib.auth import authenticate, login, logout
    from django.contrib import messages

    kemudian, saya menambahkan fungsi ```register``` , ```login_user``` , dan ```logout_user``` ke ```views.py```. Setelah itu, saya membuat file ```register.html``` , ```login.html``` dan menambahkan tombol logout di ```main.html```. Tidak lupa untuk mengimport ketiga fungsi tersebut ke dalam urls.py dan manambahkannya ke path urlpatterns.

2. Kedua, saya merestriksi akses halaman main dan product details, dengan import ```login_required``` dari ```django.contrib.auth.decorators``` ke views.py.
    kemudian saya menambahkan decorator: ```@login_required(login_url='/login')``` diatas fungsi ```show_main``` dan ```show_product```.

3. Lalu saya menggunakan data dari cookies, dengan mengimport module berikut di ```views.py```:
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse

    Kemudian saya menyimpan cookie baru bernama ```last_login``` yang berisi timestamp di fungsi ```login_user``` dan context pada ```show_main```. lalu, saya menghapus cookie tersebut di fungsi ```logout_user``` , serta menampilkan time stamp terakhir user login di ```main.html```.

4. Terakhir, saya menghubugnkan Model ```Product``` dengan ```User``` dengan import User ke ```models.py``` dan membuat relasi one-to-many antara ```Product``` dan ```User```. kemudian saya menambahkan entry user di fungsi ```create_news``` dan menambahkan filter pada ```show_main``` di ```views.py```. Setelah itu, saya menambahkan tombol filter di ```main.html``` dan nama penjual di ```product_details.html```.