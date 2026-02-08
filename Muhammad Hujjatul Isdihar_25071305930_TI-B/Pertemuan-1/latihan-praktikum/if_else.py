#PYTHON IF 
a = 330
b = 200
if b < a:
  print("a lebih besar dari b") #jika kondisi sesuai maka aksi akan di jalankan

angka = 15
if angka > 0:
  print("angka positif") #jika kondisi sesuai maka aksi akan di jalankan

umur = 20
if umur >= 18:
  #aksi akan dijalankan ketiganya ketika kondisi terpenuhi
  print("Kamu sudah bisa membuat KTP")
  print("Kamu sudah bisa mendaftar kuliah")
  print("Kamu sudah bisa membuat SIM")

is_logged_in = True
if is_logged_in:
  print("Selamat datang kembali!") #aksi ini akan dijalankan karena kondisi dari variabel yang digunakan adalah True

is_logged_in = False
if is_logged_in:
  print("Selamat datang kembali!") #aksi ini tidak akan dijalankan karena kondisi dari variabel yang digunakan adalah False

#PYTHON ELIF    
a = 33
b = 33
if b > a:
  print("b lebih besar dari a") #aksi ini akan dijalankan ketika kondisi terpenuhi, jika tidak lanjut ke kondisi kedua
elif a == b:
  print("a sama dengan b") #aksi ini akan dijalankan ketika kondisi terpenuhi, jika tidak maka program selesai

score = 75

if score >= 90:
  print("Nilai: A") #nilai A jika score lebih dari sama dengan 90
elif score >= 80:
  print("Nilai: B") #nilai B jika score lebih dari sama dengan 80 tapi kurang dari sama dengan 90
elif score >= 70:
  print("Nilai: C") #nilai C jika score lebih dari sama dengan 70 tapi kurang dari sama dengan 80
elif score >= 60:
  print("Nilai: D") #nilai D jika score lebih dari sama dengan 60 tapi kurang dari sama dengan 70

age = 25
if age < 13:
  print("You are a child") #dijalankan jika umur kurang dari 13
elif age < 20:
  print("You are a teenager") #dijalankan jika umur kurang dari 20 tapi lebih dari 12
elif age < 65:
  print("You are an adult") #dijalankan jika umur kurang dari 65 tapi umur lebih dari 19
elif age >= 65:
  print("You are a senior") #dijalankan jika umur lebih dari sama dengan 65

#aksi akan dijalankan sesuai dengan kondisi dan nilai variabel yang ada
day = 3
if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

#PYTHON ELSE
a = 200
b = 33
if b > a:
  print("b lebih besar dari a") #dijalankan jika b lebih besar dari a
elif a == b:
  print("a dan b sama") #dijalankan jika nilai a dan b sama
else:
  print("a lebih besar dari b") #jika kondisi 1 dan 2 tidak terpenuhi maka otomatis menjalankan aksi ini

#contoh lainnya
a = 200
b = 33
if b > a:
  print("b lebih besar dari a")
else:
  print("b tidak lebih besar dari a")

#contoh dengan perhitungan modulus
number = 7
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#contoh lain menentukan kategori suhu
temperature = 22
if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

#contoh lain untuk memvalidasi input pengguna
username = "Isdihar"
if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

#SHORTHAND IF
a = 5
b = 2
if a > b: print("a is greater than b") #contoh penggunaan if dalam satu baris

a = 2
b = 330
print("A") if a > b else print("B") #cetak A jika a lebih besar dari b, jika tidak cetak B

a = 10
b = 20
bigger = a if a > b else b #bigger adalah a jika a memang lebih besar dari b, jika tidak bigger adalah b
print("Bigger is", bigger) 

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") #cetak A jika a lebih besar dari b, jika tidak cetak sama dengan jika a sama dengan b, jika tidak juga cetak B

x = 15
y = 20
max_value = x if x > y else y #max_value adalah x jika x lebih dari y, jika tidak max_value adalah y
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest" #display_name adalah username jika username diisi, jika tidak display_name adalah guest
print("Welcome,", display_name)


