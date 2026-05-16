# SIMULASI NAVIGASI BROWSERR dengan Menggunakan Stack Linked list 

Program ini merupkan simulasi sistem antrean rumah sakit yang dibuat menggunakan struktur data queue linked list . program ini digunakan untuk mengatur urutan antran pasien yang datang dan dilayani berdasarkan prinsip FIFO. yaitu orang yang pertama datang akan dilayani terlebih dahulu . Kenapa memilih stack linked list bukan stack array ? , karna linked list membuat ukuran secara dinamsi , bukan statis.

# Source code

# penjelasan

Line 1: Mendeklarasikan class Node untuk membuat objek wadah data.

Line 2: Membuat fungsi konstruktor/inisialisasi objek dengan parameter data.

Line 3: Menyimpan nilai parameter ke dalam atribut self.data.

Line 4: Menginisialisasi atribut pointer self.next dengan nilai None (belum menunjuk ke node mana pun).

Line 6: Mendeklarasikan class QueueLinkedList untuk mengatur sistem antrean.

Line 7: Membuat fungsi konstruktor/inisialisasi untuk objek antrean.

Line 8: Menginisialisasi pointer depan (self.front_ptr) dengan None.

Line 9: Menginisialisasi pointer belakang (self.rear_ptr) dengan None.

Line 11: Membuat fungsi is_empty untuk memeriksa kondisi antrean.

Line 12: Mengembalikan nilai True jika front_ptr kosong (None), dan False jika ada isinya.

Line 14: Membuat fungsi enqueue dengan parameter x (nama pasien baru).

Line 15: Membuat objek Node baru dari input x dan menyimpannya di variabel new_node.

Line 16: Mengecek kondisi apakah antrean saat ini sedang kosong.

Line 17: Jika kosong, pointer depan (front_ptr) diarahkan ke new_node.

Line 18: Pointer belakang (rear_ptr) juga diarahkan ke new_node.

Line 19: Blok kode alternatif jika antrean tidak kosong.

Line 20: Menghubungkan node paling belakang lama ke new_node baru (rear_ptr.next).

Line 21: Memindahkan pointer belakang (rear_ptr) ke posisi new_node yang baru masuk.

Line 22: Mencetak pesan sukses bahwa pasien berhasil ditambahkan ke antrean.

Line 24: Membuat fungsi dequeue untuk memproses/mengeluarkan pasien terdepan.

Line 25: Mengecek apakah antrean sedang kosong.

Line 26: Jika kosong, mencetak pesan "Antrean sedang kosong".

Line 27: Menghentikan jalannya fungsi dequeue (keluar dari fungsi).

Line 28: Menyimpan node terdepan saat ini ke dalam variabel sementara temp.

Line 29: Mencetak pesan sukses pelayanan pasien yang datanya diambil dari temp.data.

Line 30: Menggeser pointer depan (front_ptr) ke node selanjutnya (front_ptr.next).

Line 31: Mengecek apakah setelah digeser, antrean menjadi benar-benar kosong.

Line 32: Jika kosong, pointer belakang (rear_ptr) juga diubah menjadi None.

Line 34: Membuat fungsi peek untuk melihat pasien di urutan pertama tanpa menghapusnya.

Line 35: Mengecek apakah antrean sedang kosong.

Line 36: Jika kosong, mencetak pesan "Antrean sedang kosong".

Line 37: Menghentikan jalannya fungsi peek.

Line 38: Mencetak nama pasien yang berada di posisi paling depan (self.front_ptr.data).

Line 40: Membuat fungsi display untuk menampilkan seluruh daftar antrean saat ini.

Line 41: Mengecek apakah antrean sedang kosong.

Line 42: Jika kosong, mencetak pesan "Antrean sedang kosong".

Line 43: Mencetak teks judul daftar antrean tanpa berpindah baris baru di akhir teks.

Line 44: Membuat pointer pelacak bernama current yang dimulai dari posisi paling depan (front_ptr).

Line 45: Melakukan perulangan looping selama pointer current tidak bernilai None.

Line 46: Mencetak data pasien yang ditunjuk oleh current dipisahkan oleh spasi.

Line 47: Memindahkan pointer pelacak current ke node berikutnya (current.next).

Line 48: Mencetak baris baru kosong setelah semua data selesai ditampilkan agar rapi.

Line 50: Membuat fungsi main sebagai pusat kendali jalannya program.

Line 51: Membuat objek antrean baru bernama queue berbasis class QueueLinkedList.

Line 52: Memulai perulangan tanpa batas (infinite loop) untuk menampilkan menu terus-menerus.

Line 53 - 58: Mencetak teks menu pilihan Sistem Antrean Rumah Sakit Unila di terminal.

Line 59: Meminta input pilihan menu dari pengguna dan langsung mengubahnya menjadi tipe data integer (int).

Line 60: Mengecek apakah pengguna memilih menu nomor 1.

Line 61: Meminta input teks nama pasien baru dari pengguna dan menyimpannya di variabel val.

Line 62: Memanggil fungsi enqueue(val) untuk memasukkan nama pasien ke dalam antrean.

Line 63: Mengecek apakah pengguna memilih menu nomor 2.

Line 64: Memanggil fungsi dequeue() untuk melayani pasien terdepan.

Line 65: Mengecek apakah pengguna memilih menu nomor 3.

Line 66: Memanggil fungsi peek() untuk melihat pasien terdepan.

Line 67: Mengecek apakah pengguna memilih menu nomor 4.

Line 68: Memanggil fungsi display() untuk melihat seluruh daftar pasien di antrean.

Line 69: Mengecek apakah pengguna memilih menu nomor 5.

Line 70: Mencetak tulisan "Program selesai." ke terminal.

Line 71: Menghentikan paksa perulangan while (break) untuk menutup program.

Line 72: Blok alternatif jika angka yang dimasukkan tidak ada di menu (bukan 1-5).

Line 73: Mencetak pesan peringatan "Pilihan tidak valid!".

Line 75: Kondisi untuk memastikan program hanya berjalan jika file ini dieksekusi secara langsung (bukan di-import oleh file lain).

Line 76: Memanggil dan menjalankan fungsi main().
# OUTPUT PROGRAM

# LINK YOUTUBE 


