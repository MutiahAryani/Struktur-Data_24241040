# Modul 1 Tipe Data, List, Tuple, Dictionary

Seluruh percobaan pada modul ini dapat diakses melalui [link ini](https://github.com/adamMaulachela/Kuliah_Struktur_data/blob/main/1.%20Modul-1%20Tipe%20Data,%20List,%20Tuple,%20Dict/2.%20Pecobaan_tipe_data.ipynb)

Modul ini secara khusus membahas tentang **Tipe Data**, **List**, **Dictionary**, dan **Tuple**. Tujuannya agar mahasiswa dapat lebih mudah dalam menyelesaikan permasalahan algoritma menggunakan bahasa pemrograman python. 

Pada modul ini kita juga akan berkenalan dengan sebuah library python yang bernama `numpy` (Numerical Python) yang menyediakan fungsi yang siap dipakai untuk memudahkan dalam melakukan perhitungan saintifik, seperti matriks, aljabar, statistik, dan lainnya. 

## Tipe Data

Baik kita mulai dengan membahas tentang **Tipe Data**, dimana secara umum ada tiga jenis tipe data yang akan kita pelajari, yaitu :
1. Tipe Data Numerik
2. Tipe Data String
3. Tipe Data List

### 📌 1. Tipe Data Numerik (Numeric Types)
Pada bahasa pemrograman python terdapat dua jenis tipe data numerik, yaitu :

### Integer (`int`)

Tipe data integer dapat diidentifikasi melalui beberapa ciri berikut ini, yaitu :
* Menyimpan **bilangan bulat** positif maupun negatif.
* Tidak memiliki bagian **desimal**.
* Ukuran nilainya **tidak terbatas** (tidak seperti bahasa lain yang terbatas oleh bit).

berikut contohnya : 
```python
x = 10
y = -200
z = 0
print(type(x))  # <class 'int'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'int'>
```
outputnya : 

```
<class 'int'>
<class 'int'>
<class 'int'>
```

Penjelasannya : 

Terdapat variabel `x` dengan nilai `10`. dan juga varibel `y` dengan nilai `-200`, serta variabel `z` dengan nilai `0`. Jika kita melihat pada ciri dari tipe data integer maka ketika kita menjalankan perintah `print(type(x))` maka outpurnya adalah `<class 'int'>` ini menandakan bahwa python memberitahu variabel `x` menyimpan nilai yang bertipe data integer. 

ciri khas lainnya dari tipe data numerik adalah :
* Mendukung operasi aritmetika: `+`, `-`, `*`, `//`, `%`, `**`
* Bisa digunakan untuk indexing, pengulangan, dan pembanding.

Sebagai contoh :
```python
# operator penjumlahan untuk tipe data integer
a1 = 5
a2 = -180

a3 = a1 + a2
print(a3)
print(type(a3))
```

outputnya 
```
-175
<class 'int'>
```

### Float (`float`)

Tipe data numerik berikutnya adalah `float` atau *floating-point number*, yang dalam matematika bisa kita sebut sebagai bilangan yang memiliki angka dibelakang koma (pecahan) atau bilangan rasional. Tipe data numerik ini berguna untuk representasi angka yang memerukan *ketelitian desimal*. 

contohnya : 
```python
# Tipe data float
a = 3.141592
b = -0.001
c = 1.0
d = float('inf') # memasukkan infinity sebagai float

# melihat isi variabel
print(a)
print(b)
print(c)
print(d)

# cek tipe data dari variabel
print(type(a))  # <class 'float'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'float'>
print(type(d))  # <class 'float'>
```
Outputnya : 
```
# Tipe data float
a = 3.141592
b = -0.001
c = 1.0
d = float('inf') # memasukkan infinity sebagai float

# melihat isi variabel
print(a)
print(b)
print(c)
print(d)

# cek tipe data dari variabel
print(type(a))  # <class 'float'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'float'>
print(type(d))  # <class 'float'>
```

Penjelasannya : 
variabel `a` menampung data berisi bilangan pecahan positif yaitu `3.141592`, sementara variabel b menampung data beisi bilangan pecahan negatif `-0.001`. Yang menarik adalah variabel `d` yang menampung nilai pecahan yang tak hingga atau infinity `float('inf')`. Nilai infinity ini kadangkala dapat kita butuhkan ketika membutuhkan bilangan yang nilainya selalu lebih besar dari bilangan lainnya. 

```python
# membandingkan nilai b3 dengan yang lain
if (a < d):
    print('lebih kecil')
else:
    print('lebih besar')
```

outputnya akan selalu `lebih kecil` karena bilangan apapun jika dibandingkan dengan bilangan infinity maka bilangan itu akan selalu lebih kecil. 

Selanjutnya apakah tipe data `float` seperti halnya `int`, jawabannya iya berikut contohnya : 

```python
# Operasi aritmatika pada float
print(a + c)
print(b ** a)
print(abs(a))
```
outputnya :
```
4.141592
(-3.3943828540367223e-10-1.618060304898697e-10j)
3.141592
```

Ciri khas dari tipe data `float` adalah :
1. Menggunakan titik (`.`) sebagai pemisah desimal.
2. Operasi float **menghasilkan float** juga (kecuali eksplisit diubah ke tipe lain).

ciri khas kedua yaitu operasi pada `float` hanya akan menghasilkan nilai bertipe data float dapat dilihat pada contoh berikut : 
```python
# hasil operasi aritmatika pada float
float = b * a
print(float)
print(type(float))

# mengubah hasil operasi aritmatika float menjadi integer
print(int(b * a))
```

outputnya :
```
-0.0031415920000000003
<class 'float'>
```

### 📌 2. Tipe Data String (`str`)

#### Pengertian 
Pada bahasa pemrograman python tipe data yang dapat digunakan untuk menyimpan teks atau tulisan adalah tipe data *string* (`str`). String diapit oleh tanda kutip tunggal `('...')` atau ganda `("...")`, dan bisa juga tiga kutip `('''...'''` atau `"""...""")` untuk string multi-baris.

contohnya : 
```python
a = 'Halo'
b = "Python"
c = """Ini adalah
string multi-baris"""
print(type(a))  # <class 'str'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'str'>
```
outputnya : 
```
<class 'str'>
<class 'str'>
<class 'str'>
```

#### Karakteristik
Karakteristik tipe data string yang dapat diidentifikasi adalah : 
* **Immutable**: isi string tidak bisa diubah langsung setelah didefinisikan.
* Dapat diakses menggunakan **index**.
* Dapat di-**slice** (potong).
* Mendukung banyak **operasi bawaan dan metode**.

#### Indexing dan Slicing 
Sebuah string sejatinya memiliki indeks, yang digunakan untuk mengidentifikasi posisi sebuah karakter dari string. Indeks tersebut dimulai dari 0 (positif dari kiri, negatif dari kanan). 

Contohnya : 
```python
# indexing dan slicing 
text = "Python"
print(text[0])     # Output: P
print(text[-1])    # Output: n
print(text[0:3])   # Output: Pyt
print(text[:4])    # Output: Pyth
print(text[::2])   # Output: Pto (loncat 2 karakter)
```
outputnya : 
```
P
n
Pyt
Pyth
Pto
```

`[0]` pada script diatas berarti ambil karakter indeks ke nol dari string pada variabel `text = "Python"` yaitu `P`, dan potong (*slicing*) karakter selanjutnya. `[-1]` memiliki pengertian mengambil karakter indeks ke -1 dari string yang artinya sama dengan mengambil karakter terakhir dari string yaitu `n`. 

Selanjutnya `[0:3]` berarti mengambil karakter pada indeks ke 0 sampai dengan indeks ke 3 yaitu `Pyt` dan potong karakter lainnya. Beriktunya `[:4]` memiliki arti bahwa mengambil karakter awal sampai dengan karakter pada indeks ke 4, yaitu `Pyth`. Sementara `[::2]` berarti mengambil karakter mulai dari indeks ke 0 kemudian loncat 2 indeks atau kelipatan 2, yaitu `Pto`. 

#### Operasi pada String

Kita dapat melalukan beberapa **operasi** terhadap data bertipe data string, yaitu : 

| Operasi      | Contoh               | Hasil         |
| ------------ | -------------------- | ------------- |
| Penggabungan | `'Hello' + ' World'` | `Hello World` |
| Pengulangan  | `'Hi' * 3`           | `'HiHiHi'`    |
| Pengecekan   | `'a' in 'data'`      | `True`        |
| Panjang      | `len('Python')`      | `6`           |

```python
# Operasi penggabungan string
print('Hello ' + 'World')

# Operasi pengulangan string
print('Hi' * 3)

# Operasi Pengecekan string
print('a' in 'data') # menghasilkan boolean (True/False)

# Operasi panjang string
print(len('Python'))
```
output :
```
Hello World
HiHiHi
True
6
```
#### Fungsi dalam String

Dalam python terdapat beberapa **fungsi** bawahan untuk mengelola data bertipe string. Berikut ini adalah fungsi python untuk mengelola string :
1. `.upper()`, digunakan untuk mengubah string menjadi huruf besar
2. `.capitalize()`, digunakan untuk menjadikan huruf pertama kata menjadi huruf besat
3. `.title()`, digunakan untuk menjadikan huruf pertama dari setiap kata dalam kalimat menjadi huruf besar
4. `.replace()`, digunakan untuk mengubah kata 
5. `.split()`, digunakan untuk memisahkan kata dalam kalimat
6. `.find()`, digunakan untuk mencari urutan string

contohnya : 
```python
s = "python programming"
print(s.upper())       # 'PYTHON PROGRAMMING'
print(s.capitalize())  # 'Python programming'
print(s.title())       # 'Python Programming'
print(s.replace("python", "java"))  # 'java programming'
print(s.split())       # ['python', 'programming']
print(s.find("gram"))  # 10
```

outputnya : 
```
PYTHON PROGRAMMING
Python programming
Python Programming
java programming
['python', 'programming']
10
```
#### String Format
Untuk menyisipkan nilai dari sebuah variabel ke dalam sebuah string python menyediakan dua cara penulisan yaitu : 
1. F-String 
```python
# String format menggunakan F-String
name = "Adam"
age = 25
print(f"Halo, nama saya {name}, umur saya {age}")
```
output : 
```
Halo, nama saya Adam, umur saya 25
```
2. Format Method
```python
# String format dengan format method
print("Halo, nama saya {}, umur saya {}".format(name, age))
```
output : 
```
Halo, nama saya Adam, umur saya 25
```
perbedaan kedua cara ini hanya terletak pada cara penulisan fungsi format, dimana f-string menggunakannya didepan menggunakan symbol `f`. Sementara format method menggunakan `.format()`. 

## List
**List** adalah **struktur data urutan** (sequence) yang digunakan untuk menyimpan **kumpulan item** dalam satu **variabel**. List bersifat:
* **Mutable**: bisa diubah setelah dibuat.
* **Terurut (ordered)**: elemen disimpan dalam urutan tertentu.
* Dapat menyimpan **berbagai tipe data campuran** dalam satu list.

### Cara Membuat List 
Sebenarnya tidak ada cara khusus dalam membuat list, cukup mendefinsikan sebuah varibel yang ditambahkan sama dengan `=` dan tanda kurung siku `[]`. Berikut contohnya : 
```python
# membuat list
angka = [1, 2, 3, 4, 5]
buah = ["apel", "jeruk", "mangga"]
campuran = [1, "dua", 3.0, True]
kosong = []

# memanggil list
print(angka)
print(buah)
print(campuran)
print(kosong)
```

outputnya : 
```
[1, 2, 3, 4, 5]
['apel', 'jeruk', 'mangga']
[1, 'dua', 3.0, True]
[]
```
### Indexing dan Slicing 
Seperti halnya indexing dan slicing pada string, list juga memiliki indeks dan dapat dipotong. Dalam matematika list ini bisa kita asumsikan sebagai sebuah himpunan, dimana setiap himpunan dapat memiliki anggota atau elemen himpunan. Setiap elemen atau anggota dari list inilah yang memiliki indeks. Berikut contohnya : 

```python
# indexing dan slicing pada list
data = ["a", "b", "c", "d"]
print(data[0])      # Output: a
print(data[-1])     # Output: d
print(data[1:3])    # Output: ['b', 'c']
print(data[:2])     # Output: ['a', 'b']
```

outputnya : 
```
a
d
['b', 'c']
['a', 'b']
```

terdapat sebuah list `data` yang memiliki empat anggota atau elemen. `data[0]` berarti kita akan mengambil anggota pada indeks ke 0 yaitu `a`. Selanjutnya `data[-1]` menunjukkan anggota dengan indeks terakhir dari list, yaitu `d`. Sementara `data[1:3]` artinya kita hanya mengambil anggota list yang indeksnya 1 sampai dengan 2, yaitu `['b', 'c']`. Dan `data[:2]` berarti kita hanya mengambil anggota list pada indeks ke 0 sampai 1, yaitu `['a', 'b']`. 


### Operasi Pada List
List pada python juga memiliki beberapa operasi yang dapat digunakan yaitu sebagai berikut ini : 

| Operasi     | Contoh            | Hasil                                     |
| ----------- | ----------------- | ----------------------------------------- |
| Penambahan  | `data + [10, 20]` | Menambah elemen baru                      |
| Pengulangan | `[1, 2] * 3`      | `[1, 2, 1, 2, 1, 2]`                      |
| Panjang     | `len(data)`       | Menghitung jumlah anggota/elemen          |
| Keanggotaan | `"a" in data`     | `True` jika ada dan `False` Jika tida ada |


contohnya : 
```python
# Operasi penambahan anggota list
data = [1, 2, 3, 4, 5]
data = data + [10, 20]
print(data)

# Operasi pengulangan list
list = [1, 2]
list = list * 3
print(list)

# Operasi mengukur panjang list
print(len(data))
print(len(list))

# Operasi mengecek keanggotaan pada list
print(20 in data)
print(13 in list)
```
Outputnya : 
```
[1, 2, 3, 4, 5, 10, 20]
[1, 2, 1, 2, 1, 2]
7
6
True
False
```

### Fungsi pada list
Pada python memiliki beberapa fungsi bawaan, berikut ini adalah beberapa fungsi bawaan dari list pada bahasa pemrograman python beserta contohnya : 

| Fungsi       | Deskripsi                                              |
| ------------ | ------------------------------------------------------ |
| `.append()`  | Menambah anggota list pada indeks terakhir             |
| `.insert()`  | Menyisipkan anggota baru pada indeks tertentu          |
| `.remove()`  | Menghapus anggota pada indeks pertama                  |
| `.pop()`     | Menghapus anggota pada indeks terakhir                 |
| `.sort()`    | Mengurutkan list secara ascending                      |
| `.reverse()` | Membalik urutan indeks anggota                         |
| `.index()`   | Mengembalikan indeks dari nilai tertentu               |
| `.count()`   | Menghitung jumlah kemunculan sebuah anggota dalam list |

contoh : 
```python
# Fungsi pada list 
a = [3, 1, 4, 1, 5]
print(a)
a.append(9)         # Menambahkan elemen di akhir
print(a)
a.insert(2, 7)      # Menyisipkan angka 7 di indeks ke-2
print(a)
a.remove(1)         # Menghapus elemen pertama yang bernilai 1
print(a)
a.pop()             # Menghapus elemen terakhir
print(a)
a.sort()            # Mengurutkan list secara ascending
print(a)
a.reverse()         # Membalik urutan elemen
print(a)
print(a.index(4))   # Mengembalikan indeks dari nilai 4
print(a.count(1))   # Menghitung jumlah kemunculan angka 1
```
output : 
```
[3, 1, 4, 1, 5]
[3, 1, 4, 1, 5, 9]
[3, 1, 7, 4, 1, 5, 9]
[3, 7, 4, 1, 5, 9]
[3, 7, 4, 1, 5]
[1, 3, 4, 5, 7]
[7, 5, 4, 3, 1]
2
1
```
### List Bersarang (Nested List)
Pada beberapa kasus kita dapat membuat list di dalam sebuah list atau yang dikenal sebagai list bersarang (Nested List). Biasanya list bersarang digunakan untuk membuat matriks, seperti pada contoh berikut ini :

```python
# membuat matriks dari list bersarang
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# memanggil matriks
print(matrix)
# memanggil elemen list pada indeks [1][2]
print(matrix[1][2])  # Output: 6
```
outputnya : 
```
6
```

Pada contoh program diatas terdapat sebuah list bernama `matrix` yang menampung elemen berupa list lainnya, `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`. Pada list bersarang indeks pada elemen terdiri dari baris dan kolom. dimulai dari indeks `[0][0]` bernilai `1` yang merupakan indeks pertama dan `[2][2]` bernilai `9` menjadi indeks pada elemen terakhir. 

Sementara pada contoh jika indeks yang dipanggil adalah `[1][2]` maka isi elemen tersebut adalah `6`. 

### Looping List
Looping list adalah cara untuk menampilkan elemen pada list secata berulang-ulang, dimulai dari indeks pertama sampai dengan indeks terakhir. Berikut contohnya :

```python
# Contoh looping list
buah = ["apel", "jeruk", "mangga"]

# For Loop
for item in buah:
    print(item)

# Mengakses indeks dan elemen
for i, item in enumerate(buah):
    print(f"{i}: {item}")
```
Outputnya : 
```
apel
jeruk
mangga
0: apel
1: jeruk
2: mangga
```

### List Comprehension
Ini merupakan cara ringkas untuk membuat list baru dari proses iterable atau perulangann. Berikut adalah contohnya : 
```Python
# Buat list kuadrat dari 0-9
kuadrat = [x**2 for x in range(10)]
print(kuadrat)  # [0, 1, 4, 9, ..., 81]

# Filter hanya bilangan genap
genap = [x for x in range(10) if x % 2 == 0]
print(genap)  # [0, 2, 4, 6, 8]
```

output : 
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 2, 4, 6, 8]
```

### Latihan List
Membuat program dengan ketentuan berikut ini : 
1. Meminta pengguna memasukkan data mahasiswa, yang terdiri dari nama dan 3 nilai ujian. 
2. Menyimpan data dalam list bersarang (nested list)
3. Menghitung nilai rata-rata mahasiswa
4. Menampilkan semua data dalam format tabel
5. Menampilkan mahasiswa dengan nilai rata-rata >= 75


Kita mulai dengan membuat list kosong dengan nama `data_mahasiswa` untuk menyimpan semua data. dan meminta user untuk memasukkan berapa jumlah data mahasiswa yang ingin diinputkan. Berikut kodenya : 

```python
data_mahasiswa = []
jumlah = int(input("Input jumlah mahasiswa: "))
```

Selanjutnya lakukan perulangan untuk setiap iterasi lakukan, input nama dan 3 nilai ujian untuk setiap mahasiswa, hitung rata-rata dari 3 nilai yang diinputkan, dan simpan semua data kedalam list dalam format `[nama, nilai, rata2]`. Berikut codenya : 

```python
# perulangan untuk memasukkan nama mahasisqa
for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nama = input("Nama: ")
    nilai = list(map(int, input("Masukkan 3 nilai dipisahkan spasi: ").split()))
    rata2 = sum(nilai) / len(nilai)
    data_mahasiswa.append([nama, nilai, rata2])
```

Selanjutnya kita akan menampilkan semua data mahasiswa dalam bentuk tabel, berikut kodenya : 
```python
# Tampilkan semua data
print("\nData Mahaiswa:")
print("Nama\tNilai\t\tRata-rata")
for siswa in data_siswa:
    print(f"{siswa[0]}\t{siswa[1]}\t{siswa[2]:.2f}")
```
Terakhir kita akan menampilkan hanya data mahasiswa yang nilai rata-ratanya lebih dari sama dengan 75, berikut kodenya 
```python
# Tampilkan siswa yang lulus
print("\nMahasiswa Lulus (>= 75):")
for siswa in data_siswa:
    if siswa[2] >= 75:
        print(f"{siswa[0]} - {siswa[2]:.2f}")
```

jika dijalankan berikut outpunya : 
```
Input jumlah siswa: 2

Siswa ke-1:
Nama: Ani
Masukkan 3 nilai dipisahkan spasi: 80 85 90

Siswa ke-2:
Nama: Budi
Masukkan 3 nilai dipisahkan spasi: 60 65 70

Data Siswa:
Nama    Nilai             Rata-rata
Ani     [80, 85, 90]      85.00
Budi    [60, 65, 70]      65.00

Siswa Lulus (>= 75):
Ani - 85.00
```

## Tuples
`Tuple` adalah tipe data di Python yang mirip dengan `list`, namun **bersifat tetap (immutable)**—artinya **isinya tidak bisa diubah setelah didefinisikan**. Namun dapat diisi dengan berbagai macam nilai dan objek. 

### Cara Membuat Tuple di Python
Secara umum cara kita membuat tuple di dalam python sangat mudah cukup dengan membuat tanda kurung `()`, Syntaxnya :
```python
t = (nilai_satu, "objek_dua")
```

contohnya : 
```python
t = (1234, 'Hello World')
t1 = (1, 2, 3)
t2 = "a", "b", "c"        # Tanpa tanda kurung juga valid
t3 = ()                   # Tuple kosong
t4 = (5,)                 # Tuple satu elemen (perlu koma!)
```
terlihat pada contoh pembuatan tuple diatas khususnya variabel `t4`, yang telihat sedikit aneh, karena diakhir isi tuple, diberikan tanda `,`. Hal ini terjadi jika kita akan membuat tuple yang isi elemennya hanya satu atau yang bisa disebut *singleton*. 

Mengapa tuple yang singleton harus diberikan tanda `,` jika tidak python akan menganggapnya sebagai string. Perhatikan contoh berikut : 
```python
# membuat tuple singleton 
satu = ('Isi',)
dua = "ini adalah tuple?",

# cek tipe datanya
print(type(satu))
print(type(dua))

# jika tidak pakai koma
satu = ('Isi')
dua = "ini adalah tuple?"

# cek tipe datanya
print(type(satu))
print(type(dua))
```
outputnya : 
```
<class 'tuple'>
<class 'tuple'>
<class 'str'>
<class 'str'>
```
Terlihat jika diberikan tanda koma python langsung mengidentifikasinya sebagai tuple dan jika tidak maka diidentifikasi sebagai string. 

### Indexing dan Slicing Tuple
Untuk mengakses nilai atau isi elemen yang ada pada tuple caranya sama dengan cara mengakses isi elemen di list. Indeks elemen pada tuple juga sama dengan list dimana indeks pertama diawali dengan Nol. Berikut contohnya :
```python
# membuat tuple
nama = ('Adam', 'Bachtiar', 'Maulachela')

# mengakses indeks ke 1 dari tuple
print(nama[1])
```
outputnya : 
```
Bachtiar
```
Selanjutnya apakah isi dari elemen tuple bisa diubah sebagaimana list? kita lakukan percobaan berikut ini : 
```python
# Membuat Tuple
t = (1, 5, 10, 15)

# mengubah isi elemen tuple
t[0] = 0
```
outputnya : 
```python
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[50], line 5
      2 t = (1, 5, 10, 15)
      4 # mengubah isi elemen tuple
----> 5 t[0] = 0

TypeError: 'tuple' object does not support item assignment
```

muncul pesan error yang menyatakan tuple tidak bisa diubah-ubah nilainya. Hal ini sesuai dengan sifat tuple yang **immutable**

Selanjutnya untuk memotong atau *slicing* elemen pada tuple apakah bisa? Pada Tuple terdapat juga fungsi slicing seperti pada list. Lalu Bagaimana caranya kita memotong / slicing tuple? Caranya juga sama seperti list. Berikut contohnya : 

```python
# membuat tuple
angka = (10, 20, 30, 40)

# Memotong tuple
print(angka[1:3]) 
print(angka[:2])
print(angka[2:])

```
outputnya : 
```
(20, 30)
(10, 20)
(30, 40)
```

Terdapat sebuah tuple dengan empat buah elemen, kemudian kita mencoba untuk memotong-motong tuple tersebut. Perintah `angka[1:3]` artinya kita akan memotong tuple dari indeks ke 1 sampai ke 2, yaitu (20, 30). Sementara perintah `angka[:2]` artinya kita memotong tuple dari indeks ke 0 sampai ke 1, yaitu (10, 20). Terakhir perintah `angka[2:]` menunjukkan kita akan memotong tuple pada indeks ke 2 sampai terakhir, yaitu (30, 40). 

### Operasi pada Tuple

Pada tuple terdapat beberapa jenis operasi yang dapat dilakukan, yaitu : 

| Operasi      | Contoh            | Hasil                                     |
| ------------ | ----------------- | ----------------------------------------- |
| Penggabungan | `(1, 2) + (3, 4)` | `(1, 2, 3, 4)`                            |
| Pengulangan  | `("A",) * 3`      | `("A", "A", "A")`                         |
| Panjang      | `len(data)`       | Menghitung jumlah anggota/elemen Tuple    |
| Keanggotaan  | `3 in (1, 2, 3)`  | `True` jika ada dan `False` Jika tida ada |

contohnya berikut ini : 
```python
# penggabungan tuple
print((1, 2) + (3, 4))

# pengulangan tuple
print(('A',) * 3)

# cek panjang tuple
data = (1, 2, 4, 5)
print(len(data))

# cek keanggotaan tuple
print(3 in data)
```

output : 
```
(1, 2, 3, 4)
('A', 'A', 'A')
4
False
```

### Tuple Bersarang (Nested Tuple)
Seperti list tuple juga bisa dibuang bersarang (nested tuple), berikut contohnya : 
```python
t = (1, 2, (3, 4))
print(t[2][0])  # Output: 3

tuple1 = "aku", "mahasiswa", "PTI UNDIKMA"
tuple2 = "selama", 3, "tahun"
tuple3 = (tuple1, tuple2) # <- nested tuple

print(tuple3)
```

outputnya : 
```
3
(('aku', 'mahasiswa', 'PTI UNDIKMA'), ('selama', 3, 'tahun'))
```

lebih unik lagi dari tuple, bahwa isi elemen pada tuple tidak hanya dapat diisi oleh sebuah nilai, tetapi dapat diisi dengan sebuah objek seperti list. berikut contohnya : 
```python
# tuple berisi list
t = ([1,2,3,4], True)

print (t)
```

outputnya : 
```
([1, 2, 3, 4], True)
```

### Sequence Unpacking
Proses pembuatan tuple dapat disebut sebagai *packing*, sementara untuk mengambil tuple (ekstrak) seluruh isinya disebut *unpacking*. 

contohnya : 
```python
# mula-mula kita buat tuple seperti ini
web = 123, "PTI UNDIKMA", "https://fsttundikma.id"

# lalu di-unpacking
id_web, nama, url = web

# maka sekarang tiga variabel tersebut akan bernilai
# sesuai yang ada di dalam tuple
#
# mari kita cetak
print(id_web)
print(nama)
print(url)
```

Outputnya : 
```
123
PTI UNDIKMA
https://fsttundikma.id
```

Dengan melakukan *upacking*, isi tuple akan di-copy ke variabel. Lalu dengan variabel kita bisa melakukan apapun, seperti **mengubah isinya**. Karena variabel bersifat *mutable*.

### Latihan Tuple
Buatlah program yang:

1. Menerima input data mata kuliah dalam bentuk tuple (`kode`, `nama`, `sks`).
2. Simpan semua mata kuliah ke dalam list.
3. Tampilkan daftar mata kuliah dan total SKS yang diambil.

Penyelesainnya : 
Lakukan inisialisasi list penampung data 
```python
matkul_list = []
```

`matkul_list` menjadi sebuah list kosong yang dapat digunakan untuk menyimpan data mata kuliah. Setiap elemen list akan diubah menjadi tuple `(kode, nama, sks)`. 

Selanjutnya kita akan membuat inputan agar user dapat memasukkan jumlah data yang diinginkan, berikut kodenya
```python
jumlah = int(input("Input jumlah mata kuliah: "))
```
program meminta user untuk memasukkan berapa banyak data mata kuliah yang akan dimasukkan atau dicatat. Hasil inputan ini akan langsung dikonversi menjadi `int`. 

berikutnya lakukan perulangan sebanyak inputan dari user untuk memasukkan data `kode`, `nama`, dan `sks` setiap mata kuliah, berikut kodenya
```python
for i in range(jumlah):
    print(f"\nMata kuliah ke-{i+1}:")
    kode = input("Kode: ")
    nama = input("Nama: ")
    sks = int(input("SKS: "))
    matkul = (kode, nama, sks)
    matkul_list.append(matkul)
```
selain ketiga data tadi kode diatas juga secara berulang melakukan pembuatan tuple `matkul` dengan inputan berupa `(kode, nama, sks)`, dan menambahkan tupel `matkul` kedalam list `matkul_list`. 

Selanjutnya kita akan menampilkan seluruh data yang telah diinputkan menggunakan kode berikut ini : 
```python
print("\nDaftar Mata Kuliah:")
for m in matkul_list:
    print(m)
```
kode diatas mengakses isi setiap elemen dalam list `matkul_list` secara langsung dimana setiap elemen list merupakan sebuah tuple yang berisi `(kode, nama, sks)`. berikut ouputnya : 
```
('CS101', 'Algoritma', 3)
('CS102', 'Basis Data', 4)
('CS103', 'AI', 3)
```

Selanjutnya kita akan menghitung dan menampilkan total sks dengan kode berikut : 
```python
total_sks = sum(m[2] for m in matkul_list)
print(f"\nTotal SKS: {total_sks}")
```

pada kode diatas kita menggunakan **list comperhension** dan `sum()` untuk menjumlahkan seluruh nilai `sks` (yang berada pada indeks ke-2 dari tuple). `m[2]` mengacu pada elemen ketiga dalam tuple `sks`. dan hasilnya kemudian ditampilkan secara rapi menggunkan f-string. Jika input sks tiap mata kuliah adalah, 3, 4, dan 3, maka total sks adalah 10.

Output dari latihan diatas : 
```Input jumlah mata kuliah: 3

Mata kuliah ke-1:
Kode: CS101
Nama: Algoritma
SKS: 3

Mata kuliah ke-2:
Kode: CS102
Nama: Basis Data
SKS: 4

Mata kuliah ke-3:
Kode: CS103
Nama: AI
SKS: 3

Daftar Mata Kuliah:
('CS101', 'Algoritma', 3)
('CS102', 'Basis Data', 4)
('CS103', 'AI', 3)

Total SKS: 10
```

## Dictionary

`Dictionary` adalah **struktur data berpasangan** (*key-value pair*) di Python. Setiap elemen memiliki kunci (`key`) yang unik, dan nilai (`value`) yang terkait dengan kunci tersebut.

* Bersifat **mutable** artinya isinya dapat diubah setelah dibuat
* Tidak mempertahankan urutan 

contohnya : 
```python
aku = {
    "nama": "Adam Bachtiar Maulachela",
    "url:" "https://www.fsttundikma.id"
}
```

pada contoh terdapat variabel `aku` dengan isi data nama dan url. Isian `nama` dan `url` adalah `key` digunakan untuk mengakses nilai yang ada didalamnya. Sementara nilai dari `key` disebut sebagai `value`. 

### Cara membuat Dictionary
Lalu bagaimana cara kita membuat `Dictionary`? Hal yang wajib kita perhatikan dan ada dalam sebuah dictionary adalah :
* nama `dictiornay`
* `key`
* `value`
* buka dan tutup menggunakan tanda kurung kurawal `{}`

kemudian antara `key` dan `value` terdapat tanda pemisah yaitu `:`, jika didalam sebuah `dictionary` terdapat lebih dari satu pasangan `key` dan `value` maka untuk memisahkannya gunakan tanda baca `,`. Berikut contohnya : 
```python
# contoh jika 1 item
nama_dict = {
    "key": "value"
}

# contoh jika lebih dari 1 item
nama_dict = {
    "key1": "value",
    "key2": "value",
    "key3": "value"
}
```

`value` pada dictionary dapat berupa string, integer, objek, list, tuple, dan dictionary sendiri. contohnya : 
```python
# membuat dictionary
dict = {
    "nama"      : "Adam Bachtiar Maulachela",
    "NIDN"      : 62708078505,
    "Prodi"     : "Pendidikan Teknologi Informasi",
    "mat_kul"    : ['Algoritma dan Pemrograman', 'Struktur Data', 'PBO'],
    "status"    : True,
    "sosmed"    : {
        "Github"    : "@adamMaulachela",
        "twiter"    : '_',
        "instagram" : '-'
    }
}
```
Perhatikan : 
* `nama` berisi data dengan tipe data `string`
* `NIDN` berisi data dengan tipe data `int`
* `Prodi` berisi data dengan tipe data `string`
* `mat_kul` berisi data dengan tipe data `list`
* `status` berisi data dengan tipe data `boolean`
* `sosmed` berisi data dengan tipe data `dict`

### Fungsi atau Method Dictionary
Berikut ini adalah fungsi atau method penting yang sering digunakan pada dictionary, yaitu : 
| Fungsi/Method        | Keterangan                             |
| -------------------- | -------------------------------------- |
| `dict.key()`         | Mengembalikan daftar semua key         |
| `dict.values()`      | Mengembalikan semua value              |
| `dict.items()`       | Mengembalikan pasangan key-value       |
| `dict.update({...})` | Menggabungkan atau memperbarui data    |
| `dict.get()`         | Mengambil nilai dari key (dengan aman) |
| `dict.pop(key)`      | Menghapus dan mengembalikan nilai      |

### Mengakses Nilai Dictionary
Setelah kita berhasil membuat `dict` selanjutnya bagaimana cara kita mengaksesnya?

Untuk mengaksesnya sama seperti mengakses `list` dan juga `tuple`, akan tetapi perbedaannya pada cara aksesnya yang tidak menggunakan indeks tetapi menggunakan `key`. 

```python
# mengakses dict menggunakan key
print("Nama Saya adalah %s" % dict['nama'])
print("Akun Github saya %s" % dict['sosmed']['Github'])

# cara lainnya dengan menggunakan .get
print("NIDN Saya adalah %s" % dict.get('NIDN'))
```
outputnya : 
```
Nama Saya adalah Adam Bachtiar Maulachela
Akun Github saya @adamMaulachela
NIDN Saya adalah 62708078505
```

### Mengubah Nilai Item Dictionary
`dict` memiliki sifata *mutable* artinya nilainya dapat diubah-ubah. Untuk mengubah nilai tersebut dengan syntax berikut ini : 
```python
nama_dict['kunci'] = 'Nilai_baru'
```

berikut ini contohnya kita mengubah nilai pada item dictionary `dict` diatas.
```python
# Mengubah nilai item dictionary dict dengan key
data['status'] = False

# Cek hasil perubahan
print(data['status'])

# Mengubah nilai item dictionary dengan .update
data.update({"sosmed" : {"twitter" : "@adammaulachaila"}})

# cek hasil perubahan
print(data['sosmed']['twitter'])
```

outputnya : 
```
False
@adammaulachaila
```

### Menghapus Nilai Item Dictionary
Untuk menghapus nilai item pada dictionary dapat menggunakan dua cara yaitu dengan perintah `del` dan dengan method `pop()`. 

Method `pop()` adalah method yang memiliki fungsi untuk mengeluarkan item dari dictionary, sementara fungsi `del` lebih pada menghapus sebuah variabel dari memori, berikut contohnya : 
```python
# Menghapus menggunakan perintah del
del data['status']

# cek hasil penghapusan data 
print(data)

# Menghapus item menggunkan method pop()
data.pop("sosmed")

# cek hasil penghapusan data 
print(data)
```

outputnya : 
```
{'nama': 'Adam Bachtiar Maulachela', 'NIDN': 62708078505, 'Prodi': 'Pendidikan Teknologi Informasi', 'mat_kul': ['Algoritma dan Pemrograman', 'Struktur Data', 'PBO'], 'sosmed': {'twitter': '@adammaulachaila'}}
{'nama': 'Adam Bachtiar Maulachela', 'NIDN': 62708078505, 'Prodi': 'Pendidikan Teknologi Informasi', 'mat_kul': ['Algoritma dan Pemrograman', 'Struktur Data', 'PBO']}
```

Jika kita ingin menghapus seluruh dictionary kita dapat menggunakan method `.clear()` : 
```python
data.clear()
```

### Menambahkan item pada dictionary
Untuk menambahkan isi ke dictionary, dapat menggunakan method `update()`, dimana parameternya berupa dictionary. Method ini juga dapat berfungsi sebagai pengubah nilai dictionary apabila kunci yang dimasukkan sudah ada di dalamnya. 

contohnya : 
```python
# membuat dictionary
mahasiswa = {
    "name" : "Adam Bachtiar Maulachela"
}

# menambahkan nim
mahasiswa.update({
    "nidn" : "0708078505"
})

# melihat hasilnya
print(mahasiswa)
```

outputnya : 
```
{'name': 'Adam Bachtiar Maulachela', 'nidn': '0708078505'}
```

### Looping Dictionary
Untuk mencetak semua isi dalam dictionary dapat digunakan mekanisme looping atau perulangan berikut contohnya : 
```python
# mencetak data pada dict secara berulang-ulang setiap key
for key in mahasiswa:
    print(key, mahasiswa[key])

# Atau:
for key, value in mahasiswa.items():
    print(f"{key}: {value}")
```
outputnya : 
```
name Adam Bachtiar Maulachela
nidn 0708078505
name: Adam Bachtiar Maulachela
nidn: 0708078505
```

### Latihan  Dictionary
Buatlah program yang : 
* Meminta user memasukkan data beberapa mahasiswa (NIM, nama, jurusan)
* Menyimpan data menggunakan dictionary (NIM sebagai key)
* Memungkinkan pencarian data berdasarkan NIM
* Menampilkan seluruh isi dictionary dalam format rapi

Pertama kita perlu memperhatikan struktur data seperti ini 
```
data_mahasiswa = {
    "NIM001": {"nama": "Rina", "jurusan": "TI"},
    "NIM002": {"nama": "Budi", "jurusan": "SI"}
}
```

dictionary utama adalah `data_mahasiswa` untuk menyimpan semua data mahasiswa, NIM berfungsi sebagai `key`, dan `value` berisi `nama` dan `jurusan`. 

Selanjutnya kita akan insialisasi dictionary kosong dan meminta user menginputkan jumlah mahasiswa yang akan didata, berikut kodenya : 
```python 
data_mahasiswa = {}
jumlah = int(input("Jumlah mahasiswa: "))
```

Selanjutnya kita input data setiap mahasiswa yang terdiri dari nim, nama, dasin jurusan, secara berulang sampai dengan seluruh jumlah mahasiswa yang diinputkan user semua terisi. berikut kodenya : 
```python
for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nim = input("NIM: ")
    nama = input("Nama: ")
    jurusan = input("Jurusan: ")
    data_mahasiswa[nim] = {
        "nama": nama,
        "jurusan": jurusan
    }
```

kode diatas akan melakukan perulangan sebanyak jumlah mahasiswa, dimana untuk setiap mahasiswa minta user untuk input `nim`, `nama`, dan `jurusan`. Kemudian setelah diinputkan simpan data ke dalam dictionary `data_mahasiswa[nim]` menggunakan nested dictionary. 

contoh hasil penyimpanannya : 
```
data_mahasiswa["22001"] = {"nama": "Rina", "jurusan": "TI"}
```
Selanjutnya kita membuat fitur pencarian data berdasarkan NIM, berikut kodenya : 
```python
print("\nCari data mahasiswa")
cari = input("Masukkan NIM: ")
if cari in data_mahasiswa:
    mhs = data_mahasiswa[cari]
    print(f"Nama: {mhs['nama']}, Jurusan: {mhs['jurusan']}")
else:
    print("Mahasiswa tidak ditemukan.")
```
program akan menerima input `nim` dari user, kemudian menggunakan pengkondisian `if` untuk mengecek apakah nim yang diinputkan ada dalam dictionary. Jika ditemukan, tampilkan `nama` dan `jurusan`, jika tidak ditemukan, tampilkan pesan `Mahasiswa tidak ditemukan`. 

Selanjutnya kita akan menampilkan seluruh data mahasiswa, berikut kodenya : 
```python
print("\nDaftar Seluruh Mahasiswa:")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} → {info['nama']} ({info['jurusan']})")
```
melakukan looping atau perulangan dictionary menggunkan method `.items()` untuk mengakses pasangan `nim` dan `info`, dan menampilkannya seperti ini : 
```
NIM: 22001 → Rina (TI)
```
berikut hasilnya jika program dijalankan :
```
Jumlah mahasiswa: 2

Mahasiswa ke-1:
NIM: 22001
Nama: Rina
Jurusan: TI

Mahasiswa ke-2:
NIM: 22002
Nama: Budi
Jurusan: SI

Masukkan NIM: 22001

Nama: Rina, Jurusan: TI

Daftar Seluruh Mahasiswa:
NIM: 22001 → Rina (TI)
NIM: 22002 → Budi (SI)
```