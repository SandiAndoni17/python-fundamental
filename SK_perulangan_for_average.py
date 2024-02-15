def hitung_rata_rata(nilai):
    total = 0
    jumlah_nilai = len(nilai)

    for nilai_siswa in nilai :
        total += nilai_siswa

    rata_rata = total / jumlah_nilai
    return rata_rata

#input jumlah siswa dan nilai siswa
jumlah_siswa = int(input("Masukkan jumlah siswa:"))

nilai_siswa = []
for i in range(jumlah_siswa):
    nilai = float(input(f" Masukkan nilai siswa ke- {i+1}:"))
    nilai_siswa.append(nilai)

#hitung rata-rata nilai
rata_rata_nilai = hitung_rata_rata(nilai_siswa)

#tampilkan hasil
print(f"\nRata-rata nilai dari {jumlah_siswa} siswa adalah: {rata_rata_nilai: .2f}")