#variabel untuk menyimpan total jumlah angka yang muncul
jumlah = 0
tes = 10
#perulangan for dari 1 sampai 10
for i in range(1, 11):
    print(i) #selalu menampilkan angka selama kondisi perulangan True
    jumlah += i #menambahkan angka ke dalam total jumlah 

#menampilkan hasil jumlah angka
print('Jumlah =', jumlah)
