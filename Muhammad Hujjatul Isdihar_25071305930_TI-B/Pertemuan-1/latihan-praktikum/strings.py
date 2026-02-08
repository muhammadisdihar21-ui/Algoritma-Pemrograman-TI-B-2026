#PYTHON STRINGS
print("Halo") #dengan tanda kutip ganda
print('Halo') #dengan tanda kutip tunggal

print("Hidup Teknik")
#bisa mmemasukan tanda kutip di dalam string asal tidak sama dengan tanda kutip diluarnya
print("kalian bisa memanggilku 'Isdihar'")
print('kalian bisa memanggilku "Isdihar"')

#contoh penggunaannya di dalam sebuah variabel
a = "Halo dunia"
print(a)

#contoh string berbentuk sebuah paragraf lebih dari satu baris dengan tanda kutip ganda
a = """Namaku Muhammad Hujjatul Isdihar,
Umur ku 19 tahun, Aku mahasiswa Universitas Riau,
fakultas Teknik, Program Studi S1 Teknik Informatika"""
print(a)

#contoh string berbentuk sebuah paragraf lebih dari satu baris dengan tanda kutip tunggal
a = '''Namaku Muhammad Hujjatul Isdihar,
Umur ku 19 tahun, Aku mahasiswa Universitas Riau,
fakultas Teknik, Program Studi S1 Teknik Informatika'''
print(a)

#string bisa dipanggil dengan array/list
a = "Aku kaya"
print(a[1])

#perulangan melalui string
for x in "semangat":
  print(x)

#len berfungsi untuk menghitung panjang string
a = "Muhammad Hujjatul Isdihar"
print(len(a))

#berfungsi untuk memeriksa apakah ada kata Teknik di dalam string tersebut, dengan output True jika iya atau False jika tidak
x = "Aku mahasiswa Teknik Informatika!"
print("Teknik" in x)
x = "Aku mahasiswa Teknik Informatika!"
print("teknik" in x) #huruf kapital dan lainnya harus diperhatikan 
x = "Aku mahasiswa Teknik Informatika!"
print("Hebat" in x)

#hal ini juga bisa di kombinasikan dengan if
x = "Aku mahasiswa Teknik Informatika"
if "Informatika" in x: #jika tidak maka tidak ada output yang dihasilkan
  print("Ya, kata 'Informatika' ada pada string tersebut.") 

#not in berfungsi sebagai kebalikan dari in, jika tidak ada maka hasilnya true, jika ada hasilnya False 
x = "Aku mahasiswa Teknik Informatika"
print("isdihar" not in x)

#hal ini juga bisa di kombinasikan dengan if
x = "Aku mahasiswa Teknik Informatika"
if "Selamat" not in x:
  print("Tidak, kata 'Selamat' tidak ada pada string tersebut.")

#SLICING STRINGS
b = "Haloo duniaaa!"
print(b[6:9]) #mengambil karakter sebuah string dari indeks 6 sampai 9, tetapi untuk batas akhir "9" tidak termasuk, alias 6,7,8 saja

b = "Aku kaya!"
print(b[:5]) #mengambil karakter sebuah string dari indeks 0 sampai 5, tetapi indeks 5 tidak termasuk, alias 0,1,2,3,4 saja

b = "Aku kaya!"
print(b[4:]) #mengambil karakter sebuah string dari indeks 4 sampai akhir

b = "aku kaya!"
print(b[-5:-2]) #indeks minus berfungsi untuk mengakses karakter string dari belakang ke depan

#MODIFY STRINGS
a = "Halo Dunia!"
print(a.upper()) #berfungsi mengubah string menjadi huruf besar semua

a = "Halo Dunia!"
print(a.lower()) #berfungsi mengubah string menjadi huruf kecil semua

a = " Halo Dunia! "
print(a.strip()) #berfungsi untuk menghilangkan spasi dari awal atau akhir

a = "Halo Dunia!"
print(a.replace("H", "G")) #berfungsi untuk mengganti sebuah karakter dengan karakter lain yang ditentukan pada string

a = "Halo Dunia!"
print(a.split(" ")) #berfungsi untuk memisahkan kata pertama dengan kata kedua pada sebuah string dengan menentukan apa pembatasnya

#CONCATENATE STRINGS
#menggabungkan dua buah string dari dua variabel yang berbeda menjadi sebuah variabel yang baru
a = "Aku"
b = "Kaya"
c = a + b
print(c) 

#untuk menambahkan spasi ditengah-tengahnya 
a = "Aku"
b = "Kaya"
c = a + " " + b
print(c) 

#FORMAT STRINGS
#menggabungkan string dan angka ke dalam sebuah variabel dengan f-string, syntax f dan kurung kurawal {}
umur = 19
x = f"Namaku Isdihar, Aku {umur}"
print(x)

price = 10
x = f"Harga nasi goreng adalah {price} rupiah"
print(x)

price = 10
x = f"Harga nasi goreng adalah {price:.3f} rupiah" #.3f berfungsi untuk menambahkan 3 angka dibelakang koma
print(x)

x = f"Harga nasi goreng adalah {5 * 2} ribu rupiah" #bisa juga dengan menggunakan operasi matematika
print(x)

#ESCAPE CHARACTERS
#karakter escape berfungsi untuk menggunakan tanda kutip ganda di dalam string yang di kelilingi tanda kutip ganda juga
x = "Aku adalah mahasiswa \"Teknik\" Informatika."
print(x)
#single quote \'
x = "Aku adalah mahasiswa \'Teknik\' Informatika."
print(x)
#backslash \\
x = "Aku adalah mahasiswa \\Teknik\\ Informatika."
print(x)
#new line \n
x = "Aku adalah mahasiswa \nTeknik\n Informatika."
print(x)
#carriage return \r
x = "Aku adalah mahasiswa \rTeknik\r Informatika."
print(x)
#tab \t
x = "Aku adalah mahasiswa \tTeknik\t Informatika."
print(x)
#backspace \b
x = "Aku adalah mahasiswa \bTeknik\b Informatika."
print(x)
#form feed \f
x = "Aku adalah mahasiswa \fTeknik\f Informatika."
print(x)

#STRING METHODS
#berfungsi mengubah huruf awal menjadi huruf kapital
txt = "selamat datang di python."
x = txt.capitalize()
print (x)
#berfungsi mengubah semua huruf menjadi huruf kecil
txt = "Selamat datang di Python!"
x = txt.casefold()
print(x)
#berfungsi untuk memposisikan string di tengah
txt = "bola"
x = txt.center(20)
print(x)
txt = "bola"
x = txt.center(20, "O")
print(x)
#untuk menghitung berapa kali kata Aku muncul di dalam string
txt = "Aku adalah Isdihar, Aku mahasiswa Universitas Riau, Aku anak TI-B"
x = txt.count("Aku")
print(x)
#untuk memisahkan setiap kata dalam string
txt = "selamat datang wahai pemula"
x = txt.split()
print(x)
#mengubah semua huruf menjadi huruf kecil
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
#mengubah semua huruf menjadi huruf besar/kapital
txt = "Hello my friends"
x = txt.upper()
print(x)
#menghapus spasi di awal dan di akhir string
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
#mengganti sebuah kata pada string dengan kata lain yang sudah ditentukan
txt = "I like bananas"
x = txt.replace("bananas", "melon")
print(x)
#berfungsi mengecek di bagian mana kata welcome dalam string tersebut
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
