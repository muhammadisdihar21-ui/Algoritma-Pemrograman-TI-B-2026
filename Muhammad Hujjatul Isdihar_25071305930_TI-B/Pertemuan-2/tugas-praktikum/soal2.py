#fungsi menentukan bilangan prima
def bilangan_prima(n):
    hasil = [] #sebuah list kosong

    for i in range(2, n + 1): #perulangan for dari 2 sampai n
        prima = True 
        for j in range(2, i): #perulangan for didalam perulangan for dari 2 sampai i
            if i % j == 0: #jika i modulus j sama dengan nol artinya i bukan bilangan prima, jika tidak sama dengan nol maka akan lanjut ke pengulangan kedua sampai seterusnya
                prima = False
                break
        if prima: #setelah selesai melalui pengulangan j maka status prima masih sama dengan True
            hasil.append(i) #kemudian menambahkan nilai i ke dalam list hasil dan mulai pengulangan seterusnya sampai ke n

    return hasil #mengembalikan nilai hasil

print("Bilangan prima sampai 50 adalah:")
print(bilangan_prima(50)) #memanggil fungsi bilangan_prima