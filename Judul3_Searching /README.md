## SISTEM PENGECEK UNDIAN

Program ini  merupakan Sistem Verifikasi Pemenang Undian yang berfungsi untuk memvalidasi nomor tiket pengguna secara otomatis guna menentukan kelayakan mereka menerima hadiah "IPONG PROMAG". Kegunaan utamanya adalah untuk melakukan validasi data secara akurat, di mana sistem akan mencocokkan input pengguna dengan daftar nomor keberuntungan yang tersimpan di database sederhana secara cepat dan instan. Dengan sistem ini, penyelenggara undian dapat memproses klaim hadiah secara transparan karena setiap nomor yang dimasukkan akan diperiksa keabsahannya terhadap data pemenang yang sudah ada.

Dalam prosesnya, program ini menerapkan Algoritma Sequential Search (Pencarian Berurutan) dengan struktur data Array (atau List dalam Python) untuk menyimpan kumpulan nomor pemenang. Algoritma ini bekerja dengan cara menyisir setiap elemen data satu per satu mulai dari indeks pertama hingga akhir, membandingkan nilai input dengan setiap nilai dalam daftar. Penggunaan variabel counter di dalam kodingan tersebut menunjukkan bahwa struktur pencarian ini tidak hanya mencari keberadaan data, tetapi juga menghitung berapa kali nomor tersebut muncul, sehingga memberikan kepastian absolut dalam menentukan status kemenangan peserta.


