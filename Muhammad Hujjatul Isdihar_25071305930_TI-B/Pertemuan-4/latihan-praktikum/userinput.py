
print("Masukkan nama anda: ")
nama = input()
print(f"Halo {nama}")


nama = input("Masukkan nama anda: ")
print(f"Hai {nama}")


nama = input("Masukkan nama anda: ")
print(f"Halo {nama}")
fav1 = input("Apa makanan kesukaanmu? ")
fav2 = input("Apa warna kesukaanmu? ")
fav3 = input("Apa angka kesukaanmu? ")
print(f"Apakah kamu menyukai {fav2}, {fav1}, dan {fav3} ?")


import math

x = input("Masukkan angka: ")

#mengubah tipedata x dari string menjadi float
y = math.sqrt(float(x)) 

print(f"Akar kuadrat dari {x} adalah {y}")


y = True
while y == True:
  x = input("Masukkan angka: ")
  try:
    x = float(x);
    y = False
  except:
    print("Input salah, silahkan coba lagi.")

print("Terimakasih")


umur = int(input("Masukkan umur: "))

try:
    umur = int(input("Umur: "))
except ValueError:
    print("Harus angka")