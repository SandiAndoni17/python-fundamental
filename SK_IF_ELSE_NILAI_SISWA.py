jumlah_siswa = 10
data_siswa = []

#input nilai dan status tugas setiap siswa
for i in range (jumlah_siswa):
    nama_siswa = input(f"Masukkan nama siswa {i+1}:")
    nilai = float(input(f"Masukkan nilai siswa {i+1}:"))
    tugas_lengkap = input(f"Apakah siswa{i+1} mengumpulkan tugas? (ya/tidak:")

    #evaluasi keterangan lulus atau tidak
    if nilai>= 60 and tugas_lengkap.lower() == 'ya' :
        keterangan = "Lulus"
    elif 40 <= nilai < 60:
        keterangan = "Remidi"
    elif nilai < 40:
        keterangan = "Tidak Lulus"
    else:
        keterangan = "Belum Lulus (tugas belum lengakap)"

    #menambahkan data siswa ke dalam list
    data_siswa.append({
        "nama" : nama_siswa,
        "nilai": nilai,
        "tugas_lengkap": tugas_lengkap,
        "keterangan": keterangan
    })

#Menampilkan data siswa dan keterangan lulus
print("\n --- Data Siswa ----")

for siswa in data_siswa:
    print(f"\nNama: {siswa['nama']}")
    print(f"\nNilai: {siswa['nilai']}")
    print(f"\nTugas Lengkap: {siswa['tugas_lengkap']}")
    print(f"\nKeterangan: {siswa['keterangan']}")