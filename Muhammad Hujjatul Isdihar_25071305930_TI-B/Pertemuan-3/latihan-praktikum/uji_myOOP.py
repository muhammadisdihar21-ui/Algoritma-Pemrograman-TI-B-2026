from myOOP import * #mengambil semua class dari file myOOP.py

# ==============================
# MENGUJI INHERITANCE
# ==============================

#membuat objek dari class Produkelektronik
tv = ProdukElektronik("TV", "3.000.000", 2) 
#membuat objek dari class ProdukMakanan
roti = ProdukMakanan("Roti", "15.000", "12-12-2026")
print()
print(tv.info_produk())
print(roti.info_produk())
print()

# ==============================
# MENGUJI POLYMORPHISM
# ==============================

#membuat objek Email dan SMS
notif1 = Email()
notif2 = SMS()

print(notif1.kirim())
print(notif2.kirim())
print()

# ==============================
# MENGUJI ENCAPSULATION
# ==============================

#membuat objek Mahasiswa
mhs = Mahasiswa()

print(mhs.set_nilai(90)) #nilai valid karena berada di rentang 0-100
print("Nilai Isdihar adalah:", mhs.get_nilai())

print(mhs.set_nilai(160)) #nilai tidak valid karena diluar rentang 0-100
print()