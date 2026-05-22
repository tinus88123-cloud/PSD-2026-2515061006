class Node:
    def __init__(self, key, task_name):
        self.key = key             
        self.task_name = task_name 
        self.left = None
        self.right = None

class BSTLanjut:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key, task_name):
        if root is None:
            return Node(key, task_name)
        if key < root.key:
            root.left = self.insert_node(root.left, key, task_name)
        elif key > root.key:
            root.right = self.insert_node(root.right, key, task_name)
        return root

    def insert(self, key, task_name):
        self.root = self.insert_node(self.root, key, task_name)

    def find_min_node(self, root):
        current = root
        while current is not None and current.left is not None:
            current = current.left
        return current

    def delete_node(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.find_min_node(root.right)
                root.key = successor.key
                root.task_name = successor.task_name 
                root.right = self.delete_node(root.right, successor.key)
        return root

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def pop_next_task(self):
        if self.root is None:
            return None
        min_node = self.find_min_node(self.root)
        task_info = (min_node.key, min_node.task_name)
        self.delete(min_node.key) 
        return task_info

    def in_order(self, root):
        if root is not None:
            self.in_order(root.left)
            print(f"Jam/Prioritas {root.key} -> {root.task_name}")
            self.in_order(root.right)


def main():
    scheduler = BSTLanjut()
    pilih = 0
    while pilih != 6:
        print("\n=== TASK SCHEDULER  ===")
        print("1. Tambah Jadwal Tugas (Insert)")
        print("2. Batalkan Tugas (Delete)")
        print("3. Lihat Semua Jadwal (In-Order / Berurutan)")
        print("4. Kerjakan Tugas Terawal (Pop Min)")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                x = int(input("Masukkan Waktu/Prioritas (Angka): "))
                nama = input("Masukkan Nama Tugas: ")
                scheduler.insert(x, nama)
                print(f"Tugas '{nama}' dijadwalkan pada waktu {x}.")
            except ValueError:
                print("Input waktu harus angka!")
        
        elif pilih == 2:
            try:
                x = int(input("Batalkan tugas di waktu (Angka): "))
                scheduler.delete(x)
                print(f"Jadwal di waktu {x} yaitu {nama} berhasil dihapus.")
            except ValueError:
                print("Input tidak valid!")
        
        elif pilih == 3:
            print("\n--- Daftar Jadwal Berurutan ---")
            if scheduler.root is None:
                print("(Kosong)")
            else:
                scheduler.in_order(scheduler.root)
        
            
        elif pilih == 4:
            task = scheduler.pop_next_task()
            if task:
                print(f"\n[MENJALANKAN TUGAS] Waktu: {task[0]} | Tugas: {task[1]}")
                print(" selesai dan dihapus dari antrean.")
            else:
                print("\nTidak ada tugas di antrean.")
                
        elif pilih == 5:
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()