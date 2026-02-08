#fungsi menghitung pangkat
def pangkat_rekursif(a, b):
    if b == 0: #jika b sama dengan nol maka akan mengembalikan nilai 1
        return 1
    else: #jika b tidak sama dengan nol 
        return a * pangkat_rekursif(a, b - 1) #memanggil fungsi didalam dirinya sendiri

#nilai angka dan pangkat di input dari user dengan tipe data integer
angka = int(input("Masukkan angka (a): "))
pangkat = int(input("Masukkan pangkat (b): "))

hasil = pangkat_rekursif(angka, pangkat) #memanggil fungsi pangkat_rekursif ke dalam variabel hasil
print("Hasilnya adalah:", hasil) #mencetak hasil