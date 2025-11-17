// Ambil elemen-elemen dari HTML
const toast = document.getElementById("toast-component");
const toastIcon = document.getElementById("toast-icon");
const toastTitle = document.getElementById("toast-title");
const toastMessage = document.getElementById("toast-message");
const toastClose = document.getElementById("toast-close");

let hideTimeout;

/**
 * Menampilkan toast notifikasi.
 * @param {string} type - Jenis toast: "success" | "error" | "warning" | "info"
 * @param {string} title - Judul toast
 * @param {string} message - Pesan toast
 * @param {number} duration - Durasi tampil (ms)
 */
function showToast(type, title, message, duration = 3000) {
    // Hentikan timer sebelumnya jika toast masih tampil
    clearTimeout(hideTimeout);

    // Reset kelas dan style awal
    toast.className = "fixed bottom-8 right-8 p-4 pr-6 rounded-xl shadow-2xl z-50 flex items-start gap-3 transition-all duration-500 opacity-0 translate-y-8";

    // Tentukan ikon dan warna berdasarkan tipe
    let icon = "";
    let bg = "";
    switch (type) {
        case "success":
            icon = "✅";
            bg = "bg-green-100 border-l-4 border-green-500";
            break;
        case "error":
            icon = "❌";
            bg = "bg-red-100 border-l-4 border-red-500";
            break;
        case "warning":
            icon = "⚠️";
            bg = "bg-yellow-100 border-l-4 border-yellow-500";
            break;
        default:
            icon = "ℹ️";
            bg = "bg-blue-100 border-l-4 border-blue-500";
    }

    // Isi konten dan terapkan warna
    toastIcon.textContent = icon;
    toastTitle.textContent = title;
    toastMessage.textContent = message;
    toast.classList.add(bg, "opacity-100", "translate-y-0", "pointer-events-auto");

    // Animasi tampil (fade + slide)
    requestAnimationFrame(() => {
        toast.style.opacity = "1";
        toast.style.transform = "translateY(0)";
    });

    // Sembunyikan otomatis setelah durasi tertentu
    hideTimeout = setTimeout(hideToast, duration);
}

/**
 * Menyembunyikan toast dengan animasi
 */
function hideToast() {
    toast.style.opacity = "0";
    toast.style.transform = "translateY(2rem)";
    toast.classList.remove("pointer-events-auto");

    setTimeout(() => {
        toast.classList.add("opacity-0");
    }, 500);
}

// Tombol manual untuk menutup
toastClose.addEventListener("click", hideToast);
