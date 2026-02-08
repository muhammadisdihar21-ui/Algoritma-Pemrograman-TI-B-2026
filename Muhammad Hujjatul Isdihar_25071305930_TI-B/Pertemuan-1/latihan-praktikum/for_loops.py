# program mengolah nilai mahasiswa

nilai = [70, 80, 65, 90, 85] #list nilai
total = 0

print("Daftar nilai:")

for n in nilai: #perulangan for dimana nilai diambil satu persatu dimasukkan ke dalam variabel n
    print(n)
    total += n #total = total + n

rata_rata = total / len(nilai) #menghitung rata-rata dengan membagi antara total dengan banyaknya nilai dalam list

print("Total nilai:", total)
print("Rata-rata:", rata_rata)

# cek kelulusan
for n in nilai: #perulangan for dimana setiap nilai dalam list di cek secara bergantian apakah lebih besar dari 75 atau tidak
    if n >= 75:
        print(n, "lulus") #jika nilai lebih besar sama dengan 75
    else:
        print(n, "tidak lulus") #jika nilai lebih kecil dari 75