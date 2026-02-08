#membandingkan 2 angka yang memiliki hasil True atau False
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 212
b = 50
#sebuah pemilihan untuk mengecek apakah a atau b yang lebih besar
if b > a:
  print("b lebih besar dari a")
else:
  print("b lebih kecil dari a")

#semua True jika nilai stringnya tidak kosong, dan angkanya bukan 0
print(bool("Hai"))
print(bool(15))

x = "Hai"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#ketika output False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class kelas():
  def __len__(self):
    return 0

myobj = kelas()
print(bool(myobj))

#fungsi yang mengembalikan nilai True
def myFunction() :
  return True

print(myFunction())

#contoh penggunaan fungsi dengan if
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#untuk memeriksa apakah sebuah nilai variabel bertipe data int atau tidak
x = 200
print(isinstance(x, int))
