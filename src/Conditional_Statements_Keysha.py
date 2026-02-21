#Types of Conditional Statements
#example 1
penjualan = 320

if penjualan >= 500:
    print("Target: Sangat Terlampaui")
elif penjualan >= 400:
    print("Target: Terlampaui")
elif penjualan >= 300:
    print("Target: Tercapai")
elif penjualan >= 200:
    print("Target: Hampir Tercapai")
elif penjualan >= 100:
    print("Target: Kurang")
else:
    print("Target: Tidak Tercapai")

#Syntax of the if statement
number = 7
if number > 5:
    #Calculate square
    print(number * number)
print('Next lines of code')

#If – else statement
pin = input("Masukkan PIN: ")

if pin == "1302":
    print("PIN benar, transaksi diproses")
else:
    print("PIN salah, coba lagi")

#Syntax of the if-elif-else statement:
def pilih_menu(pilihan):
    if pilihan == 1:
        print("Nasi Goreng")
    elif pilihan == 2:
        print("Mie Ayam")
    elif pilihan == 3:
        print("Bakso")
    else:
        print("Menu tidak tersedia")

pilih_menu(1)
pilih_menu(2)
pilih_menu(3)
pilih_menu(4)

#Menggunakan Input dari Pengguna
susu = int(input("Jumlah susu di kulkas: "))

if susu > 1:
    print("Stok aman")
elif susu == 1:
    print("Tinggal satu, segera beli")
else:
    print("Susu habis, harus beli")

#Menggunakan if Bersarang (Nested If)
umur = int(input("Masukkan umur: "))

if umur >= 18:
    print("Sudah dewasa")
    if umur >= 60:
        print("Termasuk lansia")
    else:
        print("Bukan lansia")
elif umur == 0:
    print("Baru lahir")
else:
    print("Masih anak-anak")

#Menggunakan Operator Logika dalam if
umur_seseorang = int(input("Masukkan umur anda: "))

if umur_seseorang >= 0 and umur_seseorang< 18:
    print("Masih anak anak")
elif umur_seseorang >= 18 and umur_seseorang < 60:
    print("Sudah dewasa dan bukan lansia")
elif umur_seseorang >= 60 and umur_seseorang <= 100:
    print("Sudah dewasa dan lansia")
else:
    print("Usia sangat lanjut")

#Menggunakan Ternary Operator (if dalam satu baris)
level = int(input("Masukkan level pemain: "))
status = "Pro Player" if level >= 50 else "Player Biasa"
print(f"Status: {status}")

#Variabel yang Bisa Digunakan dalam if, elif
#Boolean (bool)
terhubung_internet = True

if terhubung_internet:
    print("Perangkat terhubung ke internet")

#Angka (int, float)
skor = 120

if skor >= 100:
    print("Menang")
elif skor < 100:
    print("Kalah")

#String (str)
email = "andikeysha@email.com"

if email:
    print("Email telah diisi")

#List, Tuple, Set, Dictionary (list, tuple, set, dict)
keranjang = []

if keranjang:
    print("Keranjang memiliki barang")
else:
    print("Keranjang kosong")

#NoneType (None)
kode_verifikasi = None

if kode_verifikasi is None:
    print("Kode verifikasi belum dibuat")