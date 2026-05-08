def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = [55,99,101,121,188]
    n = len(data)
    print("SELAMAT DATANG DI UNDIAN BERHADIAH")
    print("SEMOGA BERUNTUNG")
    while True:
        try:
            target = int(input("Masukan Nomor Undian Anda: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")
    counter = sequential_search(data, n, target)
    if counter > 0:
        print(f"Selamat Nomor Anda {target} adalah Nomor Keberuntungan")
        print(f"Selamat Anda berhak membawa hadian IPONG PROMAG")
    else:
        print(f"Maaf nomor anda {target} belum beruntung, coba lagi .")

if __name__ == "__main__":
    main()
