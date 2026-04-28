## SISTEM MENEJEMEN ANTREAN PASIEN DI RS UNILA MENGGUNAKAN LINKED LIST

Program ini berfungsi untuk mengelolah urutan kedatangan pasien di Rumah sakit secara digital. sistem ini memungkinkan petugas untuk menambah pasien baru ke dalam antrean, melyani pasien berdasarkan urutan pertama yang datang, dan melihat daftar seluruh pasien yang sedang menunggu/mengantre.
ALgoritma yang digunakan adalah QUEUE yang di implementasikan menggunakan SINGLY LINKED LIST. Prinsip utama yang digunakan adalah FIFO, dimana pasien yang pertama kali masuk ke sistem akan menjadi yang pertama kali dilayani.

# source code :
<img width="863" height="856" alt="Screenshot 2026-04-28 174425" src="https://github.com/user-attachments/assets/0c95ffb0-6be2-4706-a5d9-b4123a4f99dc" />
<img width="798" height="855" alt="Screenshot 2026-04-28 174634" src="https://github.com/user-attachments/assets/e32ad22c-e0f2-4a8d-bb0f-5e2021167f8c" />
<img width="666" height="261" alt="Screenshot 2026-04-28 175033" src="https://github.com/user-attachments/assets/1e110264-bb2d-4319-9b15-0ecfe98a2a50" />

# penjelasan :

Baris 1: Membuat class Pasien, wadah untuk membuat objek pasien.
  
Baris 2: Fungsi awal untuk menyiapkan data saat pasien dibuat.

Baris 3: Menyimpan Nama pasien ke dalam objek.

Baris 4: Menyimpan Keluhan pasien ke dalam objek.

Baris 5: Menyiapkan Tali Penghubung (next) yang awalnya kosong.

Baris 7: Membuat class AntreanRumahSakit, pengelola utama seluruh antrean.

Baris 8: Fungsi awal untuk menyiapkan kondisi antrean saat pertama kali dibuka.

Baris 9: Menentukan posisi Paling Depan (head), awalnya kosong.

Baris 10: Menentukan posisi Paling Belakang (rear), awalnya kosong.

Baris 11: Menyiapkan penghitung Jumlah Pasien, dimulai dari 0.

Baris 14: Fungsi untuk memasukkan pasien baru ke dalam barisan.

Baris 15: Membuat objek pasien nyata berdasarkan nama dan keluhan yang diinput.

Baris 16: Cek apakah antrean masih kosong.

Baris 17: Jika kosong, pasien baru menjadi yang pertama sekaligus terakhir.

Baris 18: Jika sudah ada isinya.

Baris 19: Pasien yang di belakang menyambungkan "tali" ke pasien yang baru datang.

Baris 20: Status "paling belakang" berpindah ke pasien yang baru tersebut.

Baris 21: Menambah angka jumlah total pasien.

Baris 22: Menampilkan pesan konfirmasi bahwa pasien berhasil masuk.

Baris 24: Fungsi untuk memanggil pasien paling depan.

Baris 25: Cek apakah antrean kosong.

Baris 26: Jika kosong, beri tahu bahwa tidak ada orang untuk dilayani.

Baris 27: Keluar dari fungsi (karena tidak ada yang diproses).

Baris 29: Menandai siapa pasien yang sedang dilayani (posisi head).

Baris 30: Mencetak nama pasien yang dipanggil.

Baris 31: Mencetak keluhan pasien tersebut.

Baris 33: Memindahkan posisi "paling depan" ke orang di belakangnya.

Baris 35: Cek jika setelah dipindah, antrean ternyata jadi kosong.

Baris 36: Jika kosong, pastikan posisi "paling belakang" juga dikosongkan.

Baris 38: Mengurangi angka jumlah total pasien.

Baris 41: Fungsi untuk melihat daftar semua pasien yang menunggu.

Baris 42: Cek apakah tidak ada orang di antrean.

Baris 43: Beri tahu jika antrean kosong.

Baris 44: Keluar dari fungsi.

Baris 46: Mencetak judul daftar dan total pasien saat ini.

Baris 47: Mulai menelusuri dari pasien paling depan.

Baris 48: Variabel untuk nomor urut (dimulai dari 1).

Baris 49: Selama posisi saat ini masih ada orangnya (bukan None).

Baris 50: Mencetak nomor, nama, dan keluhan pasien tersebut.

Baris 51: Bergeser mengikuti "tali penghubung" ke pasien berikutnya.

Baris 52: Menambah nomor urut untuk pasien selanjutnya.

Baris 53: Mencetak garis penutup.

Baris 55: Fungsi untuk mengatur tampilan pilihan pengguna.

Baris 56: Membuat satu sistem antrean nyata dari class AntreanRumahSakit.

Baris 57: Melakukan pengulangan terus-menerus (looping).

Baris 58-62: Mencetak teks menu pilihan (Tambah, Layani, Lihat, Keluar).

Baris 64: Meminta input angka dari pengguna.

Baris 66: Jika pengguna memilih menu '1'.

Baris 67: Meminta input nama pasien.

Baris 68: Meminta input keluhan pasien.

Baris 69: Menjalankan fungsi tambah_pasien.

Baris 70: Jika pengguna memilih menu '2'.

Baris 71: Menjalankan fungsi layani_pasien.

Baris 72: Jika pengguna memilih menu '3'.

Baris 73: Menjalankan fungsi tampilkan_antrean.

Baris 74: Jika pengguna memilih menu '4'.

Baris 75: Mencetak pesan perpisahan.

Baris 76: Menghentikan perulangan (program selesai).

Baris 77: Jika input bukan 1, 2, 3, atau 4.

Baris 78: Memberi tahu bahwa pilihan salah.

baris 80: mengecek apakah file dijalankan sebagai program utama

baris 81: Memanggil fungsi main() untuk memulai program.

# OUTPUT PROGRAM

<img width="582" height="736" alt="Screenshot 2026-04-28 185105" src="https://github.com/user-attachments/assets/1738ab70-0349-4378-a2be-0681fa9f1232" />

<img width="509" height="806" alt="Screenshot 2026-04-28 185200" src="https://github.com/user-attachments/assets/20cfe586-129f-4a29-82fa-40b1511a7586" />

Output program menunjukan proses memasukan , mengeluarkan serta menampilkan antrean  pasien. admin memilih 4 opsi yang terdiri dari 1.tambah pasien, 2.layani pasien , 3.lihat daftar antrean , 4. keluar . ketika admin memilih opsi 1 , maka admin diminta untuk memasukan nama serta keluhan dari pasien , dimana setiap input akan dibuat node baru dan ditambahkan ke dalam list secara  berurutan di bagian akhir , setelah itu admin juga dapat memilih opsi 2 untuk memanggil / mengeluarkan pasien dari antrean ketika sudah dilyani yang dimana program akan mengambil / mengeluarkan node yang sudah ada di awal dalam urutan list , admin juga dapat melihat daftar antrean dengan memilih opsi no 3 , dan terakhir opsi no 4 untuk menghentikan program.

# link YOUTUBE

