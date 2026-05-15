class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class BrowserHistory:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def kunjungi_halaman(self, url):
        new_page = Node(url)
        new_page.next = self.top
        self.top = new_page
        print(f"Mengunjungi: {url}")

    def kembali(self):
        
        url_lama = self.top.url
        self.top = self.top.next
        print(f"Kembali dari: {url_lama}")
        if self.top:
            print(f"Sekarang di: {self.top.url}")
        else:
            print("Sekarang di: Halaman Kosong")

    def lihat_halaman_sekarang(self):
        if self.is_empty():
            print("Anda belum membuka halaman apapun.")
            return
        print(f"Halaman aktif adalah : {self.top.url}")

    def tampilkan_riwayat(self):
        if self.is_empty():
            print("Riwayat kosong.")
            return
        
        print("\n RIWAYAT URL Dari (Terbaru ke Lama) ")
        temp = self.top
        while temp:
            print(f"[{temp.url}] -> ", end="")
            temp = temp.next
        print("Selesai")

def main():
    history = BrowserHistory()
    
    while True:
        print("\n=== SIMULASI NAVIGASI BROWSER ===")
        print("1. Kunjungi URL Baru (Push)")
        print("2. Klik Tombol Back (Pop)")
        print("3. Lihat Halaman Aktif (Peek)")
        print("4. Lihat Semua Riwayat")
        print("5. Keluar")
        print("=================================")
        pilih = input("Pilih aksi: ")
        
        if pilih == '1':
            url = input("Masukkan URL (contoh: google.com): ")
            history.kunjungi_halaman(url)
        elif pilih == '2':
            history.kembali()
        elif pilih == '3':
            history.lihat_halaman_sekarang()
        elif pilih == '4':
            history.tampilkan_riwayat()
        elif pilih == '5':
            print("Browser ditutup.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()