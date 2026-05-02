## SISTEM MENGHITUNG TINGGI MAHASISWA

Program ini berfungsi sebagai alat sederhana untuk mengurutkan daftar angka (khususnya data tinggi badan) yang diinput oleh pengguna secara acak menjadi urutan yang teratur dari nilai terkecil hingga terbesar (ascending). Program dilengkapi dengan penanganan kesalahan (error handling) untuk memastikan bahwa input yang dimasukkan benar-benar berupa angka.

Algoritma struktur data yang diterapkan dalam kode ini adalah Bubble Sort. Algoritma ini bekerja dengan cara membandingkan dua elemen yang bersebelahan dalam sebuah list dan menukarnya jika urutannya salah. Proses ini diulangi terus-menerus hingga elemen terbesar "mengapung" ke posisi akhir.

#source code

<img width="724" height="797" alt="Screenshot 2026-05-02 170608" src="https://github.com/user-attachments/assets/47d672b3-7f8c-4239-9f5b-9acf84fa936f" />


line 1 : membuat fungsi bubble sort dengan parameter data(list angka yang akan diurutkan)

line 2 : menghitung jumlah elemen dalam list dan menyimpannya di variabel n

line 3 : perulangan luar (outer loop). Fungsinya adalah memastikan bahwa proses penggeseran angka dilakukan sebanyak n kali.

line 4 : melakukan perulangan ini berjalan dari indeks pertama (0) sampai ke posisi yang belum terurut (n-i-1)

line 5 : melakukan perbandingan apakah elemen j lebih besar dari elemen di sebelahnya j+1

line 6 :  jika line diatas benar atau elemen j lebih besar dari elemen sebelahnya maka akan dilakukan pertukaran posisi.
#output program

line 7 : Setelah semua putaran perulangan selesai (baik i maupun j), fungsi mengembalikan list data yang sekarang posisinya sudah tersusun rapi dari terkecil ke terbesar.

line 8 : Mendefinisikan fungsi utama program.

line 10 :  Menampilkan judul program di layar.

line 12 : Memulai blok penanganan error (agar program tidak langsung mati jika user salah input).

line 13 : Mengambil input dari user dalam bentuk teks (string).

line 14 : Memecah string berdasarkan spasi, mengubah tiap potongan menjadi angka (integer), dan menyimpannya dalam list.

line 16 : Mengecek jika user hanya menekan enter tanpa memasukkan angka.

line 17 : Menampilkan pesan peringatan dan menghentikan fungsi jika data kosong.

line 20 : menampilkan data awal

line 22 : mendeklarasikan variabel hasil yang di isi fungsi buble sort dengan parameter daftar tinggi

line 24 : menampilkan pesan hasil pengurutan secara ascending

line 26 : Menangkap error jika user memasukkan selain angka (misal: huruf).

line 27 : menampilkan pesan eror jika line 26 ke trigger

line 30 : memanggil fungsi main() untuk menjalankan program

<img width="933" height="109" alt="Screenshot 2026-05-02 135532" src="https://github.com/user-attachments/assets/effeec09-8271-4050-b53f-63b128ec3df8" />

# penjelasan output
Program dimulai , kemudian user diminta untuk memasukan data tinggi mahasiswa yang dipisah dengan spasi , setelah memasukan data,  user akan menekan tombol enter yang akan memproses data , program akan menampilkan data sebelum diurutkan dan sesudah di urutkan secara ascending . 

# link youtube 
