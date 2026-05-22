# Program TASK SCHEDULER menggunakan Binery search tree
Program ini merupakan simulasi untuk penjadwalan tugas / pekerjaan yang dibuat dengan Binery search tree , program ini digunakan untuk mengurutkan jadwal secara in order , user dapat menginput dan menghapus tugas .


# source code

# Penjelasan
Line 1: Membuat kelas Node sebagai cetak biru (struktur dasar) untuk setiap data tugas.

Line 2: Konstruktor untuk membuat objek Node baru dengan parameter key dan task_name.

Line 3: Menyimpan nilai waktu/prioritas (key).

Line 4: Menyimpan nama tugas (task_name).

Line 5: Mengatur cabang kiri node menjadi None (kosong) di awal.

Line 6: Mengatur cabang kanan node menjadi None (kosong) di awal.

Line 8: Membuat kelas BSTLanjut untuk mengelola seluruh struktur pohon pencarian.

Line 9: Konstruktor saat pohon BSTLanjut pertama kali dibuat.

Line 10: Menetapkan akar (pusat) pohon atau root menjadi None (karena pohon masih kosong).

Line 12: Membuat fungsi helper rekursif untuk menyisipkan node ke dalam pohon.

Line 13: Mengecek apakah titik tujuan penyisipan saat ini kosong.

Line 14: Jika kosong, buat Node baru di titik tersebut.

Line 15: Mengecek apakah waktu/nilai baru lebih kecil dari node saat ini.

Line 16: Jika ya, lemparkan node baru untuk diproses ke cabang kiri.

Line 17: Mengecek apakah waktu/nilai baru lebih besar dari node saat ini.

Line 18: Jika ya, lemparkan node baru untuk diproses ke cabang kanan.

Line 19: Mengembalikan posisi node agar struktur cabang tidak putus.

Line 21: Fungsi utama insert yang akan dipanggil oleh user.

Line 22: Menjalankan fungsi helper insert_node mulai dari root pohon.

Line 24: Fungsi untuk mencari nilai terkecil (jadwal paling awal).

Line 25: Memulai pencarian dari node yang dikirimkan (biasanya root).

Line 26: Memulai looping selama cabang kirinya masih ada.

Line 27: Terus berpindah/turun ke cabang paling kiri.

Line 28: Mengembalikan node terakhir yang ditemukan di paling ujung kiri.

Line 30: Fungsi helper rekursif untuk menghapus sebuah node.

Line 31: Mengecek apakah pencarian gagal (node kosong).

Line 32: Jika ya, kembalikan None (tidak ada yang dihapus).

Line 33: Jika nilai yang dicari lebih kecil dari node saat ini.

Line 34: Cari terus node tersebut di cabang kiri.

Line 35: Jika nilai yang dicari lebih besar dari node saat ini.

Line 36: Cari terus node tersebut di cabang kanan.

Line 37: Jika nilai yang dicari akhirnya cocok (ditemukan).

Line 38: Mengecek apakah node tersebut tidak punya anak (node daun).

Line 39: Jika ya, langsung kembalikan None untuk menghapusnya.

Line 40: Mengecek apakah node hanya punya anak cabang kanan.

Line 41: Jika ya, posisi node tersebut digantikan oleh anak kanannya.

Line 42: Mengecek apakah node hanya punya anak cabang kiri.

Line 43: Jika ya, posisi node tersebut digantikan oleh anak kirinya.

Line 44: Kondisi jika node punya 2 anak (kiri dan kanan).

Line 45: Mencari penerus (successor), yaitu nilai terkecil di cabang kanan.

Line 46: Menimpa waktu (key) node saat ini dengan waktu successor.

Line 47: Menimpa nama tugas node saat ini dengan nama tugas successor.

Line 48: Menghapus node successor yang asli karena datanya sudah dipindah ke atas.

Line 49: Mengembalikan root agar cabang pohon tetap tersambung kembali setelah penghapusan.

Line 51: Fungsi utama delete yang akan dipanggil oleh user.

Line 52: Menjalankan fungsi helper delete_node mulai dari root

Line 54: Fungsi pop_next_task untuk mengeksekusi tugas paling awal.

Line 55: Mengecek apakah antrean kosong.

Line 56: Mengembalikan None jika tidak ada tugas yang bisa dieksekusi.

Line 57: Mencari tugas terawal dengan find_min_node.

Line 58: Menyimpan data tugas tersebut (backup data ke dalam variabel task_info).

Line 59: Menghapus tugas tersebut dari pohon menggunakan delete.

Line 60: Mengembalikan data tugas agar bisa dieksekusi (ditampilkan).

Line 62: Fungsi untuk mencetak isi pohon secara berurutan (In-Order).

Line 63: Mengecek selama node tidak kosong.

Line 64: Menelusuri seluruh isi cabang kiri terlebih dahulu.

Line 65: Mencetak waktu dan nama tugas node saat ini.

Line 66: Menelusuri seluruh isi cabang kanan setelah mencetak.

Line 69: Mendefinisikan fungsi main sebagai pusat berjalannya aplikasi.

Line 70: Membuat objek scheduler dari cetakan BSTLanjut.

Line 71: Membuat variabel pilih bernilai 0 untuk looping menu.

Line 72: Memulai perulangan menu utama selama user tidak memilih angka untuk keluar.

Line 73 - 78: Menampilkan baris-baris teks menu ke layar terminal.

Line 79 - 83: Menggunakan try-except untuk menangkap error jika user memasukkan huruf (bukan angka) pada pilihan menu.

Line 85: Mengecek jika user memilih menu 1 (Tambah Tugas).

Line 86 - 92: Mengambil input angka (prioritas) dan teks (nama), menyimpannya ke scheduler.insert, lalu menangani jika terjadi error input.

Line 94: Mengecek jika user memilih menu 2 (Batalkan Tugas).

Line 95 - 100: Mengambil input angka untuk jadwal yang mau dihapus, memanggil scheduler.delete, lalu menangani error input.

Line 102: Mengecek jika user memilih menu 3 (Lihat Semua Jadwal).

Line 103 - 105: Mencetak header, mengecek jika root kosong maka akan mencetak teks (Kosong).

Line 116: (Tampilan terpotong) Menampilkan pesan jika tidak ada tugas di antrean saat fitur dieksekusi.

Line 118: Mengecek jika user memilih menu 5 (Keluar).

Line 119 - 120: Mencetak pesan program selesai dan memberhentikan perulangan menu dengan break.

Line 121 - 122: Jika user mengetik angka selain opsi menu yang tersedia, cetak "Pilihan tidak valid!".

Line 125: Syarat agar kode Python ini hanya dieksekusi jika dijalankan secara langsung (bukan di-import dari file lain).

Line 126: Memanggil fungsi main() untuk mulai menjalankan seluruh program.

# Output program

# linkYoutube

