# praktek 1
# impor library numpy
import numpy as np

# membuat array dengan numpy
tinggi_badan = np.array([150, 165, 172, 160])

# akses data pada array
print(tinggi_badan[2])


# praktek 2
# import library numpy
import numpy as np

# membuat array dengan numpy
tinggi_siswa_1 = np.array([160, 155, 150, 165])
tinggi_siswa_2 = np.array([[158, 162, 149], [151, 150, 170]])

# cara akses elemen array
print(tinggi_siswa_1[0])
print(tinggi_siswa_2[1][1])

# mengubah nilai elemen array
tinggi_siswa_1[0] = 168
tinggi_siswa_2[1][1] = 155

# cek perubahannya dengan akses elemen array
print(tinggi_siswa_1[0])
print(tinggi_siswa_2[1][1])

# cek ukuran dan dimensi array
print("Ukuran Array : ", tinggi_siswa_1.shape)
print("Ukuran Array : ", tinggi_siswa_2.shape)
print("Dimensi Array : ", tinggi_siswa_2.ndim)


# praktek 3
# impor library numpy
import numpy as np

# membuat array
a = np.array([150, 155, 160])
b = np.array([145, 150, 155])

# menggunakan operasi penjumlahan pada 2 array
print(a + b)        # array([295, 305, 315])

# Indexing dan Slicing pada Array
arr = np.array([150, 155, 160, 165])
print(arr[1:3])     # array([155, 160])

# iterasi pada array
for x in arr:
    print(x)


# praktek 4
# membuat array
arr = [150, 155, 160, 165, 170]

# Linear Traversal ke tiap elemen arr
print("Linear Traversal: ", end=" ")
for i in arr:
    print(i, end=" ")
print()


# praktek 5
# membuat array
arr = [150, 155, 160, 165, 170]

# Reverse Traversal dari elemen akhir
print("Reverse Traversal: ", end=" ")
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")
print()


# praktek 7
# membuat array
arr = [150, 155, 160, 165, 170]

# mendeklarasikan nilai awal
n = len(arr)
i = 0

print("Linear Traversal using while loop: ", end=" ")
# Linear Traversal dengan while
while i < n:
    print(arr[i], end=" ")
    i += 1
print()


# praktek 8
# membuat array
arr = [150, 155, 160, 165, 170]

# mendeklarasikan nilai awal
start = 0
end = len(arr) - 1

print("Reverse Traversal using while loop: ", end=" ")
# Reverse Traversal dengan while
while start < end:
    
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print(arr)


# praktek 9
# membuat array
arr = [150, 155, 160, 165, 170]

# cetak arr sebelum penyisipan
print("Array Sebelum Insertion : ", arr)

# cetak panjang array sebelum penyisipan
print("Panjang Array : ", len(arr))

# menyisipkan array di akhir elemen menggunakan .append()
arr.append(163)

# cetak arr setelah penyisipan
print("Array Setelah Insertion : ", arr)

# cetak panjang array setelah penyisipan
print("Panjang Array : ", len(arr))


# praktek 10
# membuat array
arr = [150, 155, 160, 165, 170]

# cetak arr sebelum penyisipan
print("Array Sebelum Insertion : ", arr)

# cetak panjang array sebelum penyisipan
print("Panjang Array : ", len(arr))

# menyisipkan array pada tengah elemen menggunakan .insert(pos, x)
arr.insert(3, 100)

# cetak arr setelah penyisipan
print("Array Setelah Insertion : ", arr)

# cetak panjang array setelah penyisipan
print("Panjang Array : ", len(arr))


# praktek 11
# membuat array
a = [150, 155, 160, 165, 170]
print("Array Sebelum Deletion : ", a)

# menghapus elemen array pertama yang nilainya 30
a.remove(160)  
print("Setelah remove(160):", a)

# menghapus elemen array pada index 1 (155)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("Setelah pop(1):", a) 

# Menghapus elemen pertama (150)
del a[0]  
print("Setelah del a[0]:", a)


# praktek 12
# impor library numpy
import numpy as np

# membuat matiks dengan numpy
matriks_np = np.array([[2,4,8],
                        [10,12,14],
                        [16,18,20]])
print(matriks_np[1][1])


# praktek 13
# Program penjumlahan matriks yang dibuat dari list

X = [[2,4,6],
    [8,10,12],
    [14,16,18]]

Y = [[1,3,5],
    [7,9,11],
    [13,15,17]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# proses penjumlahan dua matriks menggunakan nested loop
# mengulang sebanyak row (baris)
for i in range(len(X)):
   # mengulang sebanyak column (kolom)
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

print("Hasil Penjumlahan Matriks dari LIST") 

# cetak hasil penjumlahan secara iteratif
for r in result:   
   print(r)


# praktek 14
# impor library numpy
import numpy as np

# Membuat matriks dengan numpy
X = np.array([
    [2,4,6],
    [8,10,12],
    [14,16,18]])

Y = np.array(
    [[1,3,5],
    [7,9,11],
    [13,15,17]])

# Operasi penjumlahan dua matrik numpy
result = X + Y

# cetak hasil
print("Hasil Pengurangan Matriks dari NumPy")
print(result)


# praktek 15
# impor library numpy
import numpy as np

# Membuat matriks dengan numpy
X = np.array([
    [22,4,6],
    [18,10,12],
    [14,36,18]])

Y = np.array(
    [[1,30,15],
    [7,19,11],
    [23,15,27]])

# Operasi pengurangan dua matrik numpy
result = X - Y

# cetak hasil
print("Hasil Pengurangan Matriks dari NumPy")
print(result)


# praktek 16
# impor library numpy
import numpy as np

# Membuat matriks dengan numpy
X = np.array([
    [2,4,6],
    [8,10,2],
    [14,6,8]])

Y = np.array(
    [[1,3,5],
    [7,9,11],
    [3,15,7]])

# Operasi perkalian dua matrik numpy
result = X * Y

# cetak hasil
print("Hasil Perkalian Matriks dari NumPy")
print(result)


# praktik 17
# impor library numpy
import numpy as np

# Membuat matriks dengan numpy
X = np.array([
    [2,4,6],
    [8,10,2],
    [14,6,8]])

Y = np.array(
    [[1,3,5],
    [7,9,11],
    [3,15,7]])

# Operasi pembagian dua matrik numpy
result = X / Y

# cetak hasil
print("Hasil Pembagian Matriks dari NumPy")
print(result)


# impor library numpy
import numpy as np

# membuat matriks
matriks_a = np.array([
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
])

# cetak matriks
print("Matriks Sebelum Transpose")
print(matriks_a)

# transpose matriks_a
balik = matriks_a.transpose()

# cetak matriks setelah dibalik
print("Matriks Setelah Transpose")
print(balik)