#program hitung mundur sebelum ujian

detik = 10

print("Hitung mundur dimulai")

while detik > 0: #kondisi
    #aksi
    print("Sisa waktu:", detik, "detik")
    detik -= 1  # dikurang supaya loop berhenti

print("Waktu habis!")

# contoh while kedua
angka = 1
total = 0

while angka <= 5: #kondisi
    #aksi
    total += angka
    print("Menambah", angka, "ke total")
    angka += 1

print("Total akhir:", total)