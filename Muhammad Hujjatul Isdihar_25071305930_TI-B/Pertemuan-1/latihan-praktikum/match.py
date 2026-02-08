#program untuk cek jenis kendaraan dan biayanya

kendaraan = input("Masukkan jenis kendaraan(motor/mobil/truk): ") #user memasukkan jenis kendaraannya dan disimpan dalam sebuah variabel
kendaraan = kendaraan.lower() #supaya user bisa menginput huruf besar dan kecil dengan bebas
biaya = 0

print("Jenis kendaraan:", kendaraan)

match kendaraan:
    #jika user memasukkan jenis kendaraan "motor"
    case "motor":
        biaya = 2000
        print("Ini motor")
        print("Parkirnya murah") 
    #jika user memasukkan jenis kendaraan "mobil"
    case "mobil":
        biaya = 5000
        print("Ini mobil")
        print("Parkirnya agak mahal")
    #jika user memasukkan jenis kendaraan "truk"
    case "truk":
        biaya = 10000
        print("Ini truk")
        print("Parkirnya paling mahal")
    #jika user memasukkan jenis kendaraan selain motor, mobil, truk
    case _:
        biaya = 0
        print("Jenis kendaraan tidak dikenal/anomali")

print("Biaya parkir:", biaya)

#tambahan
if biaya > 0:
    print("Silakan bayar di loket")
else:
    print("Tidak perlu bayar")