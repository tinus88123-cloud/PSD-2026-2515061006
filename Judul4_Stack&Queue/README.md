# SIMULASI NAVIGASI BROWSERR dengan Menggunakan Stack Linked list 

<h1>Program ini dibuat untuk mensimulasikan navigasi browser , mulai dari mengunjungi, melakukan undo (back) , serta meilhat riwayat </h1>
<h1>Struktur data yang digunakan pada program ini adalah stack linked list dengan konsep LIFO (last in First out), Yaitu data terakhir yang masuk akan menjadi data pertama yang keluar. Nmaun terdapat perbedaan antara stack biasa dengan stack linked list yaitu penyimpanan nya, pada stack biasa kita harus mendeklarasikan luas max penyimpanan (statis) sedangkan pada stack linked list , penyimpan secara dinamis .</h1>

# Source code

# penjelasan
Baris 1: Mendefinisikan class Node sebagai kerangka simpul.

Baris 2: Konstruktor class untuk inisialisasi node dengan parameter url.

Baris 3: Menyimpan data URL ke dalam atribut self.url.

Baris 4: Menginisialisasi self.next dengan None sebagai penunjuk node di bawahnya.

Baris 6: Mendefinisikan class BrowserHistory untuk mengelola tumpukan.

Baris 7: Konstruktor class untuk inisialisasi stack linked list.

Baris 8: Menginisialisasi self.top dengan None (tanda stack kosong).

Baris 10: Mendefinisikan fungsi is_empty untuk mengecek status stack.

Baris 11: Mengembalikan nilai True jika self.top kosong.
Baris 13: Mendefinisikan fungsi kunjungi_halaman (Push).

Baris 14: Membuat objek Node baru dari URL yang dimasukkan.

Baris 15: Menyambungkan next dari node baru ke halaman lama (self.top).

Baris 16: Memperbarui self.top menjadi node yang baru dibuat.

Baris 17: Menampilkan pesan URL berhasil dikunjungi.

Baris 19: Mendefinisikan fungsi kembali (Pop).

Baris 21: Mengambil data URL dari node teratas untuk ditampilkan.

Baris 22: Menggeser penanda self.top ke node di bawahnya (self.top.next).

Baris 23: Menampilkan pesan halaman yang berhasil ditinggalkan.

Baris 24-27: Mengecek dan menampilkan halaman aktif saat ini atau pesan kosong.

Baris 29: Mendefinisikan fungsi lihat_halaman_sekarang (Peek).

Baris 30: Mengecek apakah stack dalam kondisi kosong.

Baris 31-32: Menampilkan pesan peringatan jika tidak ada halaman.

Baris 33: Menampilkan halaman yang berada di posisi top.

Baris 35: Mendefinisikan fungsi tampilkan_riwayat (Display/Traversal).

Baris 36-38: Validasi jika riwayat kosong.

Baris 40: Menampilkan judul riwayat URL.

Baris 41: Membuat variabel bantuan temp untuk menelusuri list tanpa merusak top.

Baris 42: Melakukan perulangan selama temp memiliki isi (bukan None).

Baris 43: Menampilkan data URL yang sedang ditunjuk oleh temp.

Baris 44: Menggeser temp ke node selanjutnya

Baris 47: Mendefinisikan fungsi utama main().

Baris 48: Membuat objek history dari class BrowserHistory.

Baris 50: Memulai perulangan menu utama.

Baris 51-57: Menampilkan daftar menu simulasi browser.

Baris 58: Mengambil input pilihan aksi dari pengguna.

Baris 60-62: Proses input URL baru dan menjalankan fungsi kunjungi_halaman.

Baris 63-64: Menjalankan fungsi kembali saat memilih menu 2.

Baris 65-66: Menjalankan fungsi lihat_halaman_sekarang saat memilih menu 3.

Baris 67-68: Menjalankan fungsi tampilkan_riwayat saat memilih menu 4.

Baris 69-71: Menampilkan pesan penutup dan menghentikan perulangan.

Baris 72-73: Menampilkan pesan jika input pilihan tidak valid.

Baris 75: Mengecek apakah file dijalankan secara langsung.

Baris 76: Memanggil fungsi main()

# OUTPUT PROGRAM

# LINK YOUTUBE 


