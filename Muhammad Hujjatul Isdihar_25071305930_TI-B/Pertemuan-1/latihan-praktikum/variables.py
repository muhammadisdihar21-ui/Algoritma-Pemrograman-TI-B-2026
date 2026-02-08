#PYTHON VARIABLES
x = "Isdihar"
y = 19
print(x)
print(y)

x = 4       #x dengan tipe number
x = "Aku" #x yang awalnya number berubah menjadi string
print(x)

x = str(3)    #x bertipe string menjadi '3'
y = int(3)    #y bertipe number menjadi 3
z = float(3)  #z bertipe float menjadi 3.0

x = 20
y = "Isdihar"
print(type(x)) #berfungsi menentukan type data dari variabel x
print(type(y)) #berfungsi menentukan type data dari variabel y

a = 4
A = "Sally"
#variabel a dengan A tidaklah sama, keduanya merupakan variabel yang berbeda karena perbedaan huruf kapital dan huruf kecil

#VARIABLES NAMES
nama = "Isdihar"
nama_saya = "Isdihar"
_nama_saya = "Isdihar"
namaSaya = "Isdihar"
NAMASAYA = "Isdihar"
namasaya2 = "Isdihar"

'''
2nama = "Isdihar" #nama variabel tidak boleh diawali angka
nama-saya = "Isdihar" #nama variabel tidak boleh menggunakan simbol strip
nama saya = "Isdihar" #nama variabel tidak boleh ada spasi
'''

myVariableName = "Isdihar" #nama variabel dengan Camel Case dimana hanya diawal kata pertama yang hurufnya kecil
MyVariableName = "Isdihar" #nama variabel dengan Pascal Case dimana setiap awal kata berhuruf kapital
my_variable_name = "Isdihar" #nama variabel dengan Snake Case dimana setiap kata diberi pembatas dengan simbol underscore

#ASSIGN MULTIPLE VALUES
x, y, z = "Merah", "Kuning", "Hijau" #nama variabel juga bisa dibuat dalam satu baris yang nilainya sesuai dengan urutan nama variabelnya
print(x)
print(y)
print(z)

x = y = z = "Merah" #beberapa variabel juga bisa memiliki nilai yang sama
print(x)
print(y)
print(z)

warna = ["Merah", "Kuning", "Hijau"] #kita juga bisa memindahkan nilai-nilai dalam array list ke dalam beberapa variabel
x, y, z = warna
print(x)
print(y)
print(z)

#OUTPUT VARIABLES
x = "Python terbaik" 
print(x)

x = "Nama"
y = "aku"
z = "Muhammad Hujjatul Isdihar"
print(x, y, z) #kita juga bisa menampilkan nilai dari beberapa variabel dengan satu fungsi print() dan dipisahkan dengan koma

x = "Nama "
y = "aku "
z = "Muhammad Hujjatul Isdihar"
print(x + y + z) #selain menggunakan koma, juga bisa menggunakan operator penjumlahan, tetapi tidak memberikan spasi secara otomatis dari penggabungan nilai variabelnya

x = 5
y = 10
print(x + y)  
x = 10
y = 1
print(x - y)
x = 5
y = 10
print(x * y)
x = 50
y = 10
print(x / y)
#di atas adalah penggunaan operator aritmatika sebagai pengoperasian nilai bertipe data yang sama dari beberapa variabel

x = "Isdihar"
y = 19
z = "Tahun"
print(x, y, z) #dibanding menggunakan operator penjumlahan, cara terbaik adalah menggabungkan nilai variabel dengan koma 

#GLOBAL VARIABLES
x = "Isdihar" #contoh variabel global yang dimana bisa diakses dari luar maupun dari dalam fungsi
y = "19 tahun"

def fungsi(): #membuat fungsi
  print("Namaku", x, y)

fungsi() #memanggil fungsi

x = "Mahasiswa Teknik Informatika" #variabel global

def fungsi(): #membuat fungsi
  x = "Isdihar" #variabel lokal yang hanya bisa diakses di dalam fungsi tersebut
  y = "19 tahun"
  print("Namaku", x, y)

fungsi() #memanggil fungsi

print("Aku " + x) #mencetak hasil dari variabel global karena berada diluar dari fungsi diatasnya

def fungsiku(): #membuat fungsi
  global x #syntax global berfungsi membuat variabel x yang ada di dalam sebuah fungsi menjadi variabel global yang dapat diakses dari luar fungsi
  x = "luar biasa"

fungsiku() #memanggil fungsi

print("Python sangat " + x) #memanggil nilai variabel x yang ada di dalam sebuah fungsi

x = "terbaik" #nilai awal variabel x

def fungsiku(): #membuat fungsi
  global x #menjadikan variabel x sebagai variabel global
  x = "luar biasa" #mengubah nilai variabel x yang awalnya terbaik menjadi luar biasa

fungsiku()

print("Python sangat " + x)


