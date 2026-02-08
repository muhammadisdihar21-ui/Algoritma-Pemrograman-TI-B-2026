#fungsi menghitung jumlah digit
def jumlah_digit(n):
    if n == 0: #jika n sama dengan nol maka akan mengembalikan nilai 0
        return 0
    else: #jika n tidak sama dengan nol
        return (n % 10) + jumlah_digit(n // 10) #memanggil fungsi didalam dirinya sendiri

#nilai angka di input dari user dengan tipe data integer
angka = int(input("Masukkan angka: "))
hasil = jumlah_digit(angka) #memanggil fungsi jumlah_digit ke dalam variabel hasil

print("Hasil penjumlahan digit:", hasil) #mencetak hasil