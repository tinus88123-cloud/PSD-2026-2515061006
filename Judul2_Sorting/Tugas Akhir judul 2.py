def bubble_sort_tinggi(data):
    n = len(data)
    for i in range(n):
        tukar = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                tukar = True
        if not tukar:
            break
    return data

def main():
    print("PROGRAM MENGHITUNG DATA TINGGI BADAN")
    
    try:
        input_user = input("Masukkan tinggi badan (pisahkan dengan spasi, misal: 160 175 155): ")
        daftar_tinggi = [int(x) for x in input_user.split()]
        
        if not daftar_tinggi:
            print("Data kosong. Silakan masukkan angka.")
            return
        
        print(f"\nData awal: {daftar_tinggi}")
        
        hasil = bubble_sort_tinggi(daftar_tinggi)
        
        print(f"Data urut (pendek ke tinggi): {hasil}")
        
    except ValueError:
        print("Error: Pastikan Anda hanya memasukkan angka!")

if __name__ == "__main__":
    main()