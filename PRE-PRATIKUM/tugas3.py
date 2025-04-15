def fibonacci_banyak_elemen(n):
    fib = [1, 2]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    print("Output:", ",".join(map(str, fib[:n])))

# Contoh penggunaan
jumlah = int(input("Masukkan jumlah deret: "))
fibonacci_banyak_elemen(jumlah)