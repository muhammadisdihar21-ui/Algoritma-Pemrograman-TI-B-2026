#program function hitung luas dan keliling persegi

def hitung_luas(sisi): #fungsi menghitung luas persegi
    return sisi * sisi 

def hitung_keliling(sisi): #fungsi menghitung keliling persegi
    return 4 * sisi

sisi_persegi = 5

luas = hitung_luas(sisi_persegi) #memanggil fungsi ke dalam variabel luas
keliling = hitung_keliling(sisi_persegi) #memanggil fungsi ke dalam variabel keliling

#mencetak 
print("Sisi persegi:", sisi_persegi)
print("Luas persegi:", luas)
print("Keliling persegi:", keliling)

#contoh pemanggilan ulang
for i in range(1, 4): #perulangan for dengan i sebagai pemicu aksi dari range 1-4, tetapi 4 tidak termasuk
    print("Sisi:", i)
    print("Luas:", hitung_luas(i))