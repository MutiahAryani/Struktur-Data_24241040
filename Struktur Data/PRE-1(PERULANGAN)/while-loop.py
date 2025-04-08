angka = 0
while angka < 3: # kondisi
    angka += 1 # aksi 1
    print("*" * angka) # aksi 2

i = 1
baris = 3
while i <= 5:
    spasi = (5 - i) // 2
    print(' ' * spasi + '*' * i)
    i += 2