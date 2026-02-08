#fungsi menghitung rata-rata nilai
def rata_rata(nilai):
    if len(nilai) == 0: #len mendefinisikan banyaknya data 
        return "Data kosong"

    total = sum(nilai) #sum berfungsi menjumlahkan semua nilai
    rata = total / len(nilai)
    return rata #mengembalikan nilai rata-rata

data_nilai = [80, 75, 90, 60, 85] #sebuah list
hasil = rata_rata(data_nilai) #memanggil fungsi rata_rata
print("Rata-rata nilai adalah:", hasil) #mencetak rata-rata