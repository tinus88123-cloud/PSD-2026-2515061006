class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node
        print(f"berhasil menambahkan pasien {x} ke dalam antrean ")

    def dequeue(self):
        if self.is_empty():
            print("Antrean sedang kosong")
            return
        temp = self.front_ptr
        print(f" Berhasil melayani pasien {temp.data} ")
        self.front_ptr = self.front_ptr.next
        if self.front_ptr is None:
            self.rear_ptr = None

    def peek(self):
        if self.is_empty():
            print("Antrean sedang kosong")
            return
        print(f"Pasien paling depan dalam antrean adalah {self.front_ptr.data}")

    def display(self):
        if self.is_empty():
            print(" Antrean sedang kosong")
        print("Daftar Antrean sekarang : ", end="")
        current = self.front_ptr
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    queue = QueueLinkedList()
    while True:
        print("\n===SISTEM ANTREAN RUMAH SAKIT UNILA ===")
        print("1. Masukan Pasien ke daftar Antrean")
        print("2. Layani Pasien ke daftar Antrean")
        print("3. Lihat Antrean sekarang ")
        print("4. Lihat daftar Antrean " )
        print("5. Keluar Program ")
        pilih =int(input("Pilih Menu :"))
        if pilih == 1:
            val = (input("Masukan nama pasien: "))
            queue.enqueue(val)
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()