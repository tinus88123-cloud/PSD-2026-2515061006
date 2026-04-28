
class Pasien:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None  

class AntreanRumahSakit:
    def __init__(self):
        self.head = None  
        self.rear = None  
        self.jumlah = 0

   
    def tambah_pasien(self, nama, keluhan):
        baru = Pasien(nama, keluhan)
        if self.rear is None:
            self.head = self.rear = baru
        else:
            self.rear.next = baru
            self.rear = baru
        self.jumlah += 1
        print(f"\n[Selesai] Pasien {nama} berhasil ditambahkan ke antrean.")

    def layani_pasien(self):
        if self.head is None:
            print("\n[Info] Antrean kosong. Tidak ada pasien untuk dilayani.")
            return
        
        pasien_dilayani = self.head
        print(f"\n[Proses] Melayani Pasien: {pasien_dilayani.nama}")
        print(f"Keluhan: {pasien_dilayani.keluhan}")
        
        self.head = self.head.next
        
        if self.head is None:
            self.rear = None
            
        self.jumlah -= 1

  
    def tampilkan_antrean(self):
        if self.head is None:
            print("\n[Info] Antrean saat ini kosong.")
            return
        
        print(f"\n--- DAFTAR ANTREAN ({self.jumlah} Pasien) ---")
        saat_ini = self.head
        no = 1
        while saat_ini:
            print(f"{no}. {saat_ini.nama} | Keluhan: {saat_ini.keluhan}")
            saat_ini = saat_ini.next
            no += 1
        print("---------------------------")

def menu():
    antrean = AntreanRumahSakit()
    while True:
        print("\n=== SISTEM ANTREAN RS UNILA ===")
        print("1. Tambah Pasien (Datang)")
        print("2. Layani Pasien (Panggil)")
        print("3. Lihat Daftar Antrean")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':
            nama = input("Masukkan nama pasien: ")
            keluhan = input("Masukkan keluhan: ")
            antrean.tambah_pasien(nama, keluhan)
        elif pilihan == '2':
            antrean.layani_pasien()
        elif pilihan == '3':
            antrean.tampilkan_antrean()
        elif pilihan == '4':
            print("Program dihentikan. Semoga sehat selalu!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()