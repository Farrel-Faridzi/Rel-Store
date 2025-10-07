### Repo: https://github.com/Farrel-Faridzi/Rel-Store
### Web: https://farrel-faridzi-relstore.pbp.cs.ui.ac.id

---

# Tugas 5

 # 1. Apa perbedaan antara synchronous request dan asynchronous request?

- Synchronous Request (sinkron)

    - Client (browser) mengirim request ke server → browser menunggu hingga server selesai memproses dan mengirim response.
    - Selama menunggu, halaman web akan ter-blocking (tidak bisa berinteraksi penuh).
 
- Asynchronous Request (asinkron)

    - Client mengirim request ke server, tapi tidak perlu reload halaman.
    - Browser tetap bisa digunakan sambil menunggu response.
    - Response biasanya berupa data (JSON/HTML parsial), lalu diolah dengan JavaScript untuk update bagian tertentu dari halaman.
 
 # 2. Bagaimana AJAX bekerja di Django (alur request–response)?
Alurnya kira-kira seperti ini:

1. User melakukan aksi di halaman web (misalnya klik tombol atau submit form).
2. JavaScript (AJAX) di browser menangkap aksi tersebut dan mengirimkan request asinkron ke URL Django (misalnya ```/check-username/```).
3. Django menerima request → View yang sesuai dijalankan → biasanya mengembalikan JSONResponse atau ```HttpResponse``` (bukan full template render).
4. JavaScript menerima response dari server.
5. JS memproses response (misalnya menampilkan pesan “username sudah dipakai” tanpa reload halaman).

 # 3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?

- Tidak perlu reload halaman penuh → lebih cepat.
- Interaktif dan real-time → misalnya autocomplete search, validasi form, live notification.
- Menghemat bandwidth → hanya data yang dibutuhkan yang dikirim, bukan seluruh halaman HTML.
- Pengalaman pengguna (UX) lebih baik → lebih smooth.

 # 4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

- Gunakan CSRF token
    - Django sudah punya proteksi CSRF. Pastikan AJAX request menyertakan ```X-CSRFToken``` di header.
- Gunakan HTTPS
    - Agar data sensitif (password, email) tidak dikirim plaintext.
- Validasi di server, bukan hanya di client
    - Jangan percaya validasi JavaScript saja, karena bisa dimanipulasi.
- Gunakan ```JsonResponse``` atau ```HttpResponse``` yang aman
    - Jangan bocorkan data sensitif di response.
- Rate limiting / throttling (opsional, via DRF atau middleware)
    - Untuk mencegah brute-force login.
  
 # 5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

- Lebih cepat → pengguna tidak bosan menunggu reload halaman penuh.
- Lebih interaktif → form validasi real-time, infinite scroll, dynamic search.
- Lebih modern → terasa seperti aplikasi desktop (SPA-like).
- Namun: butuh fallback jika JS nonaktif, dan developer harus hati-hati agar flow aplikasi tetap jelas (tidak membingungkan user).
