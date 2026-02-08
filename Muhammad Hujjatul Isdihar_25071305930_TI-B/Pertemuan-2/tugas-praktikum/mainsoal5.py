from modulesoal5 import hitung_jarak #memanggil fungsi dari file modulesoal5 yang bernama hitung_jarak 

#nilai x1, y1, x2, y2 di input dari user dengan tipe data float
x1 = float(input("Masukkan x1: "))
y1 = float(input("Masukkan y1: "))
x2 = float(input("Masukkan x2: "))
y2 = float(input("Masukkan y2: "))

hasil = hitung_jarak(x1, y1, x2, y2) #memanggil fungsi hitung_jarak ke dalam variabel hasil
print("Jarak antar dua titik adalah:", hasil) #mencetak hasil