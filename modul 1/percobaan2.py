dm = {}
for _ in range(int(input("Jumlah mahasiswa: "))):
    nim = input("\nNIM: ")
    dm[nim] = {
        "n": input("Nama: "),
        "j": input("Jurusan: "),
        "a": input("Alamat: "),
        "m": [(input(f"  Matkul {i+1}: "), float(input("  Nilai: ")))
              for i in range(int(input("Jumlah matkul: ")))]
    }

print("\n=== Data Mahasiswa ===")
for nim, d in dm.items():
    print(f"\nNIM: {nim}\nNama: {d['n']}\nJurusan: {d['j']}\nAlamat: {d['a']}\nNilai:")
    [print(f"  {m} = {n}") for m, n in d["m"]]
    print(f"Rata-rata: {sum(n for _, n in d['m']) / len(d['m']):.2f}")