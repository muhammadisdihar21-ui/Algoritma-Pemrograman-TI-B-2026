import math #import library math

#membuat fungsi hitung_jarak
def hitung_jarak(x1, y1, x2, y2): 
    jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) #math.sqrt berfungsi sebagai akar dari (x2 - x1)**2 + (y2 - y1)**2 yang hasilnya dimasukkan kedalam variabel jarak
    return jarak #mengembalikan nilai jarak