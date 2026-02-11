# ==============================
# A. INHERITANCE (Pewarisan)
# ==============================

class Produk: #class induk
    def __init__(self, nama_produk, harga):
        #atribut class induk
        self.nama_produk = nama_produk
        self.harga = harga

    def info_produk(self): #method class induk
        return f"{self.nama_produk} seharga {self.harga}"


class ProdukElektronik(Produk): #class turunan dari class induk
    def __init__(self, nama_produk, harga, garansi):
        #mengambil atribut dari class induk
        super().__init__(nama_produk, harga)
        #atribut class turunan 
        self.garansi = garansi

    def info_produk(self): #method class turunan
        return f"{self.nama_produk} seharga {self.harga} dengan garansi {self.garansi} tahun"


class ProdukMakanan(Produk): #class turunan dari class induk
    def __init__(self, nama_produk, harga, tanggal_kadaluarsa):
        #mengambil atribut dari class induk
        super().__init__(nama_produk, harga)
        #atribut class turunan 
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def info_produk(self): #method class turunan 
        return f"{self.nama_produk} seharga {self.harga} kadaluarsa {self.tanggal_kadaluarsa}"


# ==============================
# B. POLYMORPHISM
# ==============================

class Notifikasi: #class induk
    def kirim(self): #method class induk
        return "Mengirim notifikasi umum"


class Email(Notifikasi): #class turunan 
    def kirim(self): #method class turunan dengan nama yang sama
        return "Mengirim notifikasi melalui Email"


class SMS(Notifikasi): #class turunan 
    def kirim(self): #method class turunan dengan nama yang sama 
        return "Mengirim notifikasi melalui SMS"


# ==============================
# C. ENCAPSULATION
# ==============================

class Mahasiswa: #class induk
    def __init__(self):
        self.__nilai = 0  #menggunakan atribut private

    def set_nilai(self, nilai): #method untuk mengubah nilai dari atribut private
        if 0 <= nilai <= 100: 
            self.__nilai = nilai
            return "Nilai berhasil disimpan"
        else:
            return "Nilai tidak valid"

    def get_nilai(self): #method untuk menampilkan nilai atribut private setelah diubah set nilai
        return self.__nilai