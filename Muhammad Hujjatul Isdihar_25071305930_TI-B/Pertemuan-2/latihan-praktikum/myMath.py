def penambahan(a, b):
    tambah = a + b
    return tambah

def pengurangan(a, b):
    kurang = a - b
    return kurang

def perkalian(a, b):
    kali = a * b
    return kali

def pembagian(a, b):
    if b == 0:
        print("Error")
    else:
        bagi = a / b
        return bagi

def modulus(a, b):
    mod = a % b
    return mod

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
