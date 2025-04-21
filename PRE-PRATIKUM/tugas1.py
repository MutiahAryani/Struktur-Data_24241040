angka = int(input('Masukkan angka ganjil: '))
for i in range(1, angka + 1, 2):
    spasi = ' ' * ((angka - i) // 2)
    print(spasi + '*' * i)

angka = 0
while angka < 5: # kondisi
    angka += 1 # aksi 1
    print("*" * angka) # aksi 2