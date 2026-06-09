#PROGRAM PENGELOLAHAN PEKERJA Mengguna HashMap Separate Chaining

#Deskripsi
Program ini merupakan pengelolahan data pekerja sederhana , yang memungkinkan kita untuk mencari , mengubah, menghapus, menambahkan pekerja dengan hanya menggunakan id 

#Source Code

<img width="329" height="61" alt="Screenshot 2026-06-09 185814" src="https://github.com/user-attachments/assets/2bf37640-e036-4ed3-a7d7-0a0725ecf748" />

Pada baris 1–5 dibuat class Node yang digunakan untuk menyimpan data pekerja. Pada baris 2 dibuat constructor. Pada baris 3 nilai key digunakan untuk menyimpan ID pekerja. Pada baris 4 nilai value digunakan untuk menyimpan nama pekerja. Pada baris 5 dibuat pointer next yang digunakan untuk menghubungkan satu node dengan node lainnya dalam linked list.

<img width="332" height="49" alt="Screenshot 2026-06-09 185827" src="https://github.com/user-attachments/assets/bbe58b97-56cc-4c04-94c7-94cde1c50e4b" />

Pada baris 7–10 dibuat class HashmapID yang merupakan wadah utama dari struktur data hash map. Pada baris 8 dibuat constructor dengan parameter default ukuran 10. Pada baris 9 nilai atribut SIZE digunakan untuk menyimpan ukuran kapasitas tabel. Pada baris 10 dibuat atribut table berupa list (array) yang berisi nilai None sebanyak ukuran SIZE untuk menampung linked list.

<img width="313" height="25" alt="Screenshot 2026-06-09 185838" src="https://github.com/user-attachments/assets/55a97ce1-2922-491c-a5f6-efa822b63ba1" />

Pada baris 12–13 dibuat method hash_function yang menerima parameter key. Pada baris 13 fungsi ini mengembalikan nilai hasil dari operasi matematika modulo yang digunakan untuk menentukan di slot/indeks mana data pekerja akan ditempatkan pada tabel.

<img width="293" height="131" alt="Screenshot 2026-06-09 185850" src="https://github.com/user-attachments/assets/b9b0b52c-036d-401b-bf0e-18311b735b69" />

Pada baris 15–25 dibuat method insert untuk menambahkan data pekerja. Pada baris 16–17 program mencari indeks lokasi berdasarkan key dan mengecek isi tabel tersebut. Pada baris 18–22 program mengecek linked list; jika key (ID) sudah ada, nilai (nama) akan diperbarui. Pada baris 23–25 dibuat objek Node baru yang langsung disisipkan pada posisi paling depan (head) pada linked list di indeks tersebut.

<img width="265" height="96" alt="Screenshot 2026-06-09 185904" src="https://github.com/user-attachments/assets/acac37cc-7af6-43d1-9191-af2921d94f6f" />

Pada baris 27–34 dibuat method search untuk mencari data pekerja. Pada baris 28–29 program mencari indeks lokasi dari key yang dicari. Pada baris 30–33 program melakukan perulangan menyusuri linked list untuk mencocokkan key; jika cocok, program akan mengembalikan keseluruhan node tersebut. Pada baris 34 program mengembalikan nilai None jika sampai ujung pencarian data tidak ditemukan.

<img width="296" height="167" alt="Screenshot 2026-06-09 185915" src="https://github.com/user-attachments/assets/7b0ecc6c-412e-4cea-841a-fadb2d208d56" />

Pada baris 36–49 dibuat method delete untuk menghapus data pekerja. Pada baris 37–39 program menentukan indeks dan menyiapkan pointer previous untuk melacak node sebelumnya. Pada baris 40–49 program mencari key yang cocok, kemudian menghapus node tersebut dengan cara mengubah arah pointer node sebelumnya agar langsung menunjuk ke node setelahnya, lalu mengembalikan nilai True (berhasil) atau False (gagal).

<img width="382" height="109" alt="Screenshot 2026-06-09 185926" src="https://github.com/user-attachments/assets/f45ab259-9c99-4404-80f0-a001a52dec02" />

Pada baris 51–59 dibuat method display untuk menampilkan seluruh isi data pekerja. Pada baris 53 program melakukan perulangan utama sebanyak ukuran tabel. Pada baris 56–59 program menyusuri setiap node di dalam linked list pada masing-masing indeks, lalu mencetak nilai key dan value-nya secara berurutan hingga bertemu batas akhir NULL.

<img width="436" height="461" alt="Screenshot 2026-06-09 185941" src="https://github.com/user-attachments/assets/2ceabd3b-d97d-4f87-b697-bcfa7dc29ace" />

Pada baris 61–99 dibuat kerangka awal antarmuka program pada fungsi main(). Pada baris 64–69 program mencetak pilihan menu ke layar. Pada baris 70–74 program menerima input dari pengguna dengan sistem pengamanan try-except agar tidak error jika input bukan angka. Pada baris 76–99 program memproses percabangan if-elif untuk menjalankan fitur penambahan data (pilihan 1), penghapusan data (pilihan 2), dan penampilan daftar pekerja (pilihan 3).

<img width="396" height="193" alt="Screenshot 2026-06-09 185956" src="https://github.com/user-attachments/assets/8ba97ccb-a5b7-4dca-9873-f42b75af5ccc" />

Pada baris 100–115 merupakan kelanjutan dari proses pada fungsi main(). Pada baris 100–107 program menangani kemungkinan error saat pengguna memasukkan input ID serta menjalankan fitur pencarian pekerja (pilihan 4). Pada baris 108–110 program menjalankan fitur keluar dari program (pilihan 5) dengan memutus perulangan menggunakan perintah break. Pada baris 114–115 dibuat blok kondisional standar Python agar fungsi main() otomatis berjalan ketika file dieksekusi.

# Output Program


# Link YouTube
