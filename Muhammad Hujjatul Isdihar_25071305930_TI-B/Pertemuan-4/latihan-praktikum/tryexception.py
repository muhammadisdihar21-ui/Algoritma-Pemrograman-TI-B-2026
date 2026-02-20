"""if 5 > 3
    print("Benar")

print(10 / 0)

try:
    x = 10 / 0
except:
    print("Terjadi sebuah error")


try:
    angka = int("abc")
except ValueError:
    print("Input tersebut bukanlah angka")

try:
    x = int(input("Masukkan angka: "))
    print(10/x)
except ValueError:
    print("Harus memasukkan angka")
except ZeroDivisionError:
    print("Angka tidak boleh nol")


try:
    x = int(input("Masukkan angka: "))
except:
    print("Error")
else:
    print("Tidak ada error")

try:
    print(10/0)
except:
    print("Error")
finally:
    print("Selesai")


umur = -5
if umur < 0:
    raise ValueError("Umur tidak boleh negatif")


class UmurError(Exception):
    pass

umur = -1
if umur < 0:
    raise UmurError("Umur salah")


try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Terjadi kesalahan input") from e


with open("file.txt") as f:
    data = f.read()
"""

try:
    1/0
except Exception as e:
    e.add_note("Terjadi saat proses pembagian")
    raise