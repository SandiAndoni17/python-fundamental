def tampilkan_daftar_belanja (daftar_belanja):
    print("\nDaftar Belanja:")
    for indeks, item in enumerate(daftar_belanja, start=1):
        print(f"{indeks}. {item}")

def tambah_item(daftar_belanja):
    item_baru = input ("Masukkan item baru: ")
    daftar_belanja.append(item_baru)
    print(f"{item_baru} ditambahkan ke daftar belanja.")

def hapus_item(daftar_belanja):
    if not daftar_belanja:
        print("Daftar belanja kosong.")
        return
    tampilkan_daftar_belanja(daftar_belanja)
    indeks_hapus = int(input("Masukkan nomor item yang akan di hapus:"))

    if 1<= indeks_hapus <= len(daftar_belanja):
        item_hapus = daftar_belanja.pop (indeks_hapus -1)
        print(f"{item_hapus} dihapus dari daftar belanja.")
    else:
        print("nomor item tidak valid.")

def main():
    daftar_belanja = []

    while True:
        print("\nMenu:")
        print("1. Tampilkan Daftar Belanja")
        print("2. Tambah Item ke Daftar Balanja")
        print("3. Hapus Item dari Daftar Balanja")
        print("4. Keluar")

        pilihan = input("Pilih menu (1/2/3/4) : ")

        if pilihan == "1":
            tampilkan_daftar_belanja(daftar_belanja)
        elif pilihan =="2":
            tambah_item(daftar_belanja)
        elif pilihan =="3":
            hapus_item(daftar_belanja)
        elif pilihan == "4":
            print("Terima Kasih! Keluar Dari Program.")
            break
        else:
            print("pilihan tidak valid.")

if __name__ == "__main__": # perintah untuk jalankan fungsi main di line 24
    main()

