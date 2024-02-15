def hitung_total_belanja():
    total_belanja = 0

    while True:
        nama_barang = input ("Masukkan nama barang (ketik 'selesai' untuk akhiri)")

        if nama_barang.lower() == 'selesai':   #jika diketik selesai, maka akan keluar fungsi if(break)
            break

        try:                                                         # try --execpt untuk test blok code
            harga_barang = float(input("masukkan harga barang:"))    # harus input format float
            jumlah_barang = int(input("masukkan jumlah barang:"))    # harus integer
            total_belanja += harga_barang * jumlah_barang            # += artinya masukkan harga * jumlah ke var
        except ValueError:                                           # total_belanja dan masukkan nilai baru ke tb juga
            print("Masukkan harga dan jumlah dalam format yang benar.\n")
    return total_belanja

#program utama
print("Selamat datang di program hitung total belanja")
total_belanja = hitung_total_belanja()
print(f"\nTotal belanja adalah : ${total_belanja: .2f}")
print("Terima kasih telah menggunakan program kami")