#PYTHON OPERATORS
print(10 + 5)
sum1 = 100 + 50 #menjumlahkan 2 angka
sum2 = sum1 + 250 #menjumlahkan variabel dengan angka
sum3 = sum2 + sum2 #menjumlahkan variabel dengan variabel

#ARITHMETIC OPERATORS
x = 200
y = 20

print(x + y) #penjumlahan (addition)
print(x - y) #pengurangan (subtraction)
print(x * y) #perkalian (multiplication)
print(x / y) #pembagian (division)
print(x % y) #sisa pembagian (modulus)
print(x ** y) #pangkat (exponentiation)
print(x // y) #pembulatan ke bawah (floor division)

x = 16
y = 7

print(x / y) #pembagian yang selalu menghasilkan nilai float

x = 16
y = 7

print(x // y) #pembagian yang selalu menghasilkan nilai int atau bilangan bulat

#ASSIGNMENT OPERATORS
x = 5

x += 3     #x = x + 3
print(x)   #8

x -= 2     #x = x - 2
print(x)   #6

x *= 2     #x = x * 2
print(x)   #12

x /= 3     #x = x / 3
print(x)   #4.0

x %= 3     #sisa bagi
print(x)   #1

x //= 2    #floor division
print(x)   #0

x **= 3    #pangkat
print(x)   #0

x = 5      #biner: 0101

x &= 3     #0101 & 0011 = 0001
print(x)   #1

x |= 3     #0001 | 0011 = 0011
print(x)   #3

x ^= 1     #0011 ^ 0001 = 0010
print(x)   #2

x = 4      #biner: 0100

x >>= 1    #geser kanan
print(x)   #2

x <<= 2    #geser kiri
print(x)   #8

#walrus operator
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#COMPARISON OPERATORS
x = 10
y = 8

print(x == y) #contoh equal
print(x != y) #contoh not equal
print(x > y) #contoh lebih besar
print(x < y) #contoh lebih kecil
print(x >= y) #contoh lebih besar sama dengan
print(x <= y) #contoh lebih kecil sama dengan

x = 8
print(2 < x < 10) #x lebih besar dari 2 dan x lebih kecil dari 10
print(3 < x and x < 20) #x lebih besar dari 3 dan x lebih kecil dari 20

#LOGICAL OPERATORS
x = 7
print(x > 0 and x < 10) #operator and, x lebih besar dari 0 dan x lebih kecil dari 10, hasilnya True

x = 7
print(x < 5 or x > 10) #operator or, x lebih kecil dari 5 atau x lebih besar dari 10, hasilnya False

x = 7
print(not(x > 3 and x < 10)) #operator not, x lebih besar dari 3 dan x lebih kecil dari 10, hasilnya di reverse/di balik, hasilnya True tapi karena operator not berubah menjadi False

#IDENTITY OPERATORS
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #True
print(x is y) #False
print(x == y) #True

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y) #True karena objeknya berbeda 

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y) #memeriksa apakah nilai kedua variabel sama
print(x is y) #memeriksa apakah kedua variabel menunjuk ke objek yang sama di memori

#MEMBERSHIP OPERATORS
#memeriksa apakah banana ada di dalam daftar list
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
#memeriksa apakah pineapple benar tidak ada di dalam daftar list
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

text = "Hello World"
print("H" in text) #apakah H ada di dalam variabel text
print("hello" in text) #apakah hello ada di dalam variabel text
print("z" not in text) #apakah z benar tidak ada di dalam variabel text

#BITWISE OPERATORS
print(6 & 3) #operator & membandingkan setiap bit dan menetapkannya menjadi 1 jika keduanya bernilai 1, jika tidak, nilainya ditetapkan menjadi 0

print(6 | 3) #operator | membandingkan setiap bit dan menetapkannya menjadi 1 jika salah satu atau kedua bit bernilai 1, jika tidak, nilainya ditetapkan menjadi 0

print(6 ^ 3) #operator ^ membandingkan setiap bit dan menetapkannya menjadi 1 jika hanya satu yang bernilai 1, jika tidak (jika keduanya bernilai 1 atau keduanya bernilai 0) maka nilainya ditetapkan menjadi 0

#OPERATOR PRECEDENCE
print((6 + 3) - (6 + 3)) #tanda kurung memiliki prioritas tertinggi, artinya ekspresi di dalam tanda kurung harus dievaluasi terlebih dahulu
print(100 + 5 * 3) #perkalian * memiliki prioritas lebih tinggi daripada penjumlahan +, dan oleh karena itu perkalian dievaluasi sebelum penjumlahan
print(5 + 4 - 7 + 3) #penjumlahan + dan pengurangan - memiliki prioritas yang sama, oleh karena itu kita mengevaluasi ekspresi dari kiri ke kanan