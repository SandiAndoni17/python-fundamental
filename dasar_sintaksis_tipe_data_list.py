daftar_buku=['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
print('Tampilkan variable daftar_buku')
print(daftar_buku)

print('\n Proses semua dengan For in')
for buku in daftar_buku:
    print(buku)

print ('\n Tampilkan isi daftar buku dalam indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\n Tampilkan dalam for in range')
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

daftar_buku =[1, 'Kenji Volume 2', -313, 3.14]
print('\n Tampilkan dalam for in range dimana tipe data tiap elemen beda')
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print('kembalikan nilai awal daftar buku')
daftar_buku=['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
print('\n tambahkan 1 buku baru')
daftar_buku.append ('Dunia Matematika Kelas 5')
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print('\n Clear list')
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print('\n Ganti elemen pertama')
daftar_buku=['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
daftar_buku[0] = 'Eight Habits'
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print('\n Ambil elemen ke -2')
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n buku yang diambil tadi')
print(buku)

print('\n Pop')
daftar_buku.pop()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n Pop-1')
daftar_buku=['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
daftar_buku.pop(-4)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])












