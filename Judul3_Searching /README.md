## SISTEM PENGECEK UNDIAN

Program ini  merupakan Sistem Verifikasi Pemenang Undian yang berfungsi untuk memvalidasi nomor tiket pengguna secara otomatis guna menentukan kelayakan mereka menerima hadiah "IPONG PROMAG". Kegunaan utamanya adalah untuk melakukan validasi data secara akurat, di mana sistem akan mencocokkan input pengguna dengan daftar nomor keberuntungan yang tersimpan di database sederhana secara cepat dan instan. Dengan sistem ini, penyelenggara undian dapat memproses klaim hadiah secara transparan karena setiap nomor yang dimasukkan akan diperiksa keabsahannya terhadap data pemenang yang sudah ada.

Dalam prosesnya, program ini menerapkan Algoritma Sequential Search (Pencarian Berurutan) dengan struktur data Array (atau List dalam Python) untuk menyimpan kumpulan nomor pemenang. Algoritma ini bekerja dengan cara menyisir setiap elemen data satu per satu mulai dari indeks pertama hingga akhir, membandingkan nilai input dengan setiap nilai dalam daftar. Penggunaan variabel counter di dalam kodingan tersebut menunjukkan bahwa struktur pencarian ini tidak hanya mencari keberadaan data, tetapi juga menghitung berapa kali nomor tersebut muncul, sehingga memberikan kepastian absolut dalam menentukan status kemenangan peserta.

# Source code
<img width="1294" height="732" alt="Screenshot 2026-05-08 164031" src="https://github.com/user-attachments/assets/03235a67-68a9-42df-a34a-d3bfad6b5c16" />

# penjelasan code :

Line 1: Mendefinisikan fungsi sequential_search dengan parameter data (daftar angka), n (jumlah data), dan target (angka yang dicari).

Line 2: Inisialisasi variabel i = 0 sebagai indeks awal untuk memulai pencarian.

Line 3: Inisialisasi variabel counter = 0 untuk menghitung berapa kali angka target ditemukan.

Line 4: Melakukan perulangan while selama indeks i lebih kecil dari jumlah data n.

Line 5: Mengecek apakah elemen data pada indeks ke-i sama dengan angka target.

Line 6: Jika cocok, nilai counter ditambah 1.

Line 7: Menaikkan nilai indeks i sebesar 1 untuk memeriksa elemen berikutnya.

Line 8: Mengembalikan nilai total counter ke pemanggil fungsi.

Line 11: Mendefinisikan fungsi main sebagai program utama.

Line 12: Membuat list data yang berisi daftar nomor-nomor undian pemenang.

Line 13: Menghitung panjang atau jumlah elemen di dalam list data dan menyimpannya di variabel n.

Line 14-15: Mencetak kalimat sapaan dan judul program ke layar.

Line 16: Memulai perulangan while True untuk memastikan input yang masuk valid.

Line 17-18: Mencoba mengambil input dari pengguna, mengubahnya menjadi integer, dan menyimpannya di variabel target.

Line 19: Menghentikan perulangan (break) jika input berhasil diproses sebagai angka.

Line 20-21: Menangani error jika pengguna memasukkan selain angka dan menampilkan pesan peringatan.

Line 22: Memanggil fungsi sequential_search dan menyimpan hasilnya ke dalam variabel counter.

Line 23: Mengecek apakah nilai counter lebih besar dari 0 (artinya target ditemukan).

Line 24-25: Mencetak pesan selamat, nomor yang menang, jumlah kemunculannya, dan hadiah yang didapat.

Line 26-27: Jika counter adalah 0, mencetak pesan bahwa nomor tersebut belum beruntung.

Line 29-30: Mengecek apakah file dijalankan secara langsung, jika ya, maka menjalankan fungsi main().

# output program :
<img width="506" height="91" alt="Screenshot 2026-05-08 163936" src="https://github.com/user-attachments/assets/fb79b54e-b7e3-49b2-9aeb-fb4f6e2d7cf9" />
<img width="786" height="108" alt="Screenshot 2026-05-08 163920" src="https://github.com/user-attachments/assets/cbac6771-6376-4668-8116-16d159b31392" />

output pada kodingan ini menujukan hasil dari inputan user , yang dimana menggunakan algoritma sequential search yang memeriksa target apakah sama / ada di data , jika ada maka output nya adalah anda berhasil menang hadiah ipong promag namun jika  inputan yang dimasukan tidak ada di data maka sistem akan menampilkan output anda tidak beruntung , coba lagi. 

# link Youtube 

https://youtu.be/EnunQhngiJg
