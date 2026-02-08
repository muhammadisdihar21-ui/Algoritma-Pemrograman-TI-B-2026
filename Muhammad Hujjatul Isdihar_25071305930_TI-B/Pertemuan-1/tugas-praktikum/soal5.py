#membuat fungsi hitung
def hitung(a, b):
    penjumlahan = a + b
    pengurangan = a - b
    return penjumlahan, pengurangan

#memanggil fungsi hitung
hasil_jumlah, hasil_kurang = hitung(5, 3)


print('Penjumlahan =', hasil_jumlah)
print('Pengurangan =', hasil_kurang)