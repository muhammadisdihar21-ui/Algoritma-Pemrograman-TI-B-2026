#membuat custom exception untuk nilai negatif
class NilaiError(Exception):
    pass  

while True:  #loop while agar input diulang terus sampai data valid
    try:
        nilai = input("Masukkan nilai ujian: ")  #meminta input user bertipe string
        nilai = float(nilai)  #mencoba mengubah input menjadi angka bertipe float

        if nilai < 0:  #mengecek apakah nilai negatif
            raise NilaiError("Nilai tidak boleh negatif")  
            #jika nilai negatif, paksa python memunculkan error buatan sendiri

        break  #keluar dari loop while jika tidak ada error sama sekali

    except ValueError:  #berfungsi jika input bukanlah angka dan akan menampilkan pesan errornya
        print("Error: input harus berupa angka")

    except NilaiError as e:  #menangkap error buatan sendiri ketika angka yang dimasukkan adalah negatif
        print("Error:", e)

    finally:
        print("Percobaan input selesai\n")
        #bagian ini selalu dijalankan apapun hasilnya


#program utama menentukan kategori nilai
if nilai >= 90 and nilai <= 100:
    grade = "A"
elif nilai >= 80 and nilai < 90:
    grade = "B"
elif nilai >= 70 and nilai < 80:
    grade = "C"
elif nilai >= 60 and nilai < 70:
    grade = "D"
elif nilai >= 0 and nilai < 60:
    grade = "E"
else:
    print("Nilai yang dimasukkan tidak dalam rentang 0-100")
    nilai = ("Error")

#mencetak hasil akhirzS
print("Nilai:", nilai)
print("Grade:", grade)


