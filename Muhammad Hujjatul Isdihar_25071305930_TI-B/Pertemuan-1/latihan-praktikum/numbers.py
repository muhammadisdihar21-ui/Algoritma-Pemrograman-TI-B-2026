a = 7    #tipe data int
b = 7.7  #tipe data float
c = 7j   #tipe data complex

#mengecek tipe data yang digunakan nilai variabelnya
print(type(a))
print(type(b))
print(type(c))

#tipe data int
d = 5
e = 8129389437373439436
f = -311328281

print(type(d))
print(type(e))
print(type(f))

#tipe data float
g = 1.1000
h = 1.0191
i = -35777.59
j = 35e3
k = 12E4
l = -87.7e100

print(type(g))
print(type(h))
print(type(i))

print(type(j))
print(type(k))
print(type(l))

#tipe data complex
m = 3+5j
n = 5j
o = -5j

print(type(m))
print(type(n))
print(type(o))

p = 1    #tipe data int
q = 2.8  #tipe data float
r = 1j   #tipe data complex

#mengubah tipe data variabel p yang awalnya int menjadi float ke dalam variabel yang baru yaitu s
s = float(p)

#mengubah tipe data variabel q yang awalnya float menjadi int ke dalam variabel yang baru yaitu t
t = int(q)

#mengubah tipe data variabel p yang awalnya int menjadi complex ke dalam variabel yang baru yaitu u
u = complex(p)

#untuk tipe data complex tidak bisa diubah ke tipe data yang lain
print(s)
print(t)
print(u)

print(type(s))
print(type(t))
print(type(u))

import random #merupakan modul bawaan python

print(random.randrange(5, 30)) #berfungsi untuk mencetak sebuah angka random dari komputer pada range yang telah ditentukan 5-30