class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashmapID:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        previous = None
        while current is not None:
            if current.key == key:
                if previous is None:
                    self.table[index] = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def display(self):
        print("\nData Pekerja:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next
            print("NULL")

def main():
    Hashmapx = HashmapID()
    while True:
        print("\n PROGRAM KITAKERJA")
        print("1.Tambahkan ID pekerja")
        print("2.Hapus ID Pekerja")
        print("3.Tampilkan Daftar Pekerja")
        print("4.Cari Pekerja")
        print("5.Keluar Program")
        try:
            pilih = int(input("Pilih Menu :"))
        except ValueError:
            print("Input tidak valid. Masukkan angka antara 1 dan 5.")
            continue

        if pilih == 1:
            try:
                id = int(input("Tambah Id Pekerja: "))
            except ValueError:
                print("ID harus berupa angka.")
                continue
            value = input("Tambah Nama Pekerja: ")
            Hashmapx.insert(id, value)
            print(f"ID Pekerja {id} dengan nama {value} berhasil ditambahkan.")
        elif pilih == 2:
            try:
                id = int(input("Masukan ID Pekerja yang ingin dihapus: "))
            except ValueError:
                print("ID harus berupa angka.")
                continue
            if Hashmapx.delete(id):
                print(f"ID Pekerja {id} berhasil dihapus.")
            else:
                print(f"ID Pekerja {id} tidak ditemukan.")
        elif pilih == 3:
            Hashmapx.display()
        elif pilih == 4:
            try:
                id = int(input("Masukan ID Pekerja yang ingin dicari: "))
            except ValueError:
                print("ID harus berupa angka.")
                continue
            hasil = Hashmapx.search(id)
            if hasil is not None:
                print(f"Pekerja ditemukan: {hasil.value}")
            else:
                print("Pekerja tidak ditemukan")
        elif pilih == 5:
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()