# fungsi untuk pertambahan
def tambah(x, y):
    return x + y

# fungsi untuk pengurangan
def kurang(x, y):
    return x - y

# fungsi untuk perkalian
def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y

print("pilih operasi yang akan dikerjakan:")
print("1. pertambahan")
print("2. pengurangan")
print("3. Perkalian")
print("4. Pembagian")


while True:
    pilih = input("Masukan operasi yang diinginkan (1/2/3/4): ")

    if pilih in ('1','2','3','4'):
        try:
            num1 = float(input("masukan angka pertama: "))
            num2 = float(input("masukan angka kedua: "))
        except ValueError:
            print("angka masukan salah")
            continue

    if pilih == '1':
        print(num1, '+', num2, '=', tambah(num1,num2))
    elif pilih == '2':
        print(num1, '-', num2, '=', kurang(num1,num2))
    elif pilih == '3':
        print(num1, '*', num2, '=', kali(num1,num2))
    elif pilih == '4':
        print(num1, ':', num2, '=', bagi(num1,num2))

    ulang = input("apakah mau memasukan angka baru (ya/tidak): ")
    if ulang == "tidak":
        break
else:
    print("error")
