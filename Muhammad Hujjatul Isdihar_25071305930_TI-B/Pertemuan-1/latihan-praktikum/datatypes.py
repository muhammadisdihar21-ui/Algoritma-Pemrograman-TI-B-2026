tipe1 = '1' #variabel dengan nilai bertipe data string
tipe2 = 1 #variabel dengan nilai bertipe data int/number
tipe3 = 1.5 #variabel dengan nilai bertipe data float
tipe4 = True #variabel dengan nilai bertipe data boolean
tipe5 = [1,3,4,5] #variabel dengan nilai bertipe data list
tipe6 = ['Isdihar',2,3] #variabel dengan nilai bertipe data list
tipe7 = (1,2,3) #variabel dengan nilai bertipe data tuple
tipe8 = { #variabel dengan nilai bertipe data dict
    'nama': 'Isdihar',
    'kelas': 'TI-B',
    'nim': '25071305930',
    'Mahasiswa Aktif' : True
}
tipe9 = 2j #variabel dengan nilai bertipe data complex
tipe10 = range(7) #variabel dengan nilai bertipe data range
tipe11 = {"Merah", "Kuning", "Hijau"} #variabel dengan nilai bertipe data set
tipe12 = frozenset({"Merah", "Kuning", "Hijau"}) #variabel dengan nilai bertipe data frozenset
tipe13 = b"Hai" #variabel dengan nilai bertipe data bytes
tipe14 = bytearray(5) #variabel dengan nilai bertipe data bytearray
tipe15 = memoryview(bytes(5)) #variabel dengan nilai bertipe data memoryview
tipe16 = None #variabel dengan nilai bertipe data none type

#mengecek tipe data apa yang digunakan dari variabel variabel diatas
print(type(tipe1)) 
print(type(tipe2))
print(type(tipe3))
print(type(tipe4))
print(type(tipe5))
print(type(tipe6))
print(type(tipe7))
print(type(tipe8))
print(tipe8['kelas'])
print(type(tipe9)) 
print(type(tipe10))
print(type(tipe11))
print(type(tipe12))
print(type(tipe13))
print(type(tipe14))
print(type(tipe15))
print(type(tipe16))

#kita juga bisa langsung menetapkan tipe data apa yang akan digunakan pada nilai variabel tersebut
x = str("Ini adalah string")
y = int(10)	
z = float(20.7)
a = list(("Harimau", "Singa", "Kucing"))	
b = tuple(("Ayam", "Bebek", "Angsa"))

print(type(x))