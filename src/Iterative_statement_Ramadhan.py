# Iterative Statement

# perulangan menggunakan for loop
for perulangan in range(25):
    print("perulangan ke-", perulangan)

for i in range(25):
    print("Perulangan ke", i)

# perulangan menggunakan while loop
# i = 0
# while i < 5:
#   print("Perulangan ke-", i)
#   i+= 1

# Kontrol dalam Perulangan
# 1. break
for perulangan in range(50):
    if perulangan == 25:
        break
    print(perulangan)

# 2. continue
for perulangan in range(20):
    if perulangan == 17:
        continue
    print(perulangan)

# 3. else pada Loop
for i in range(5):
    print(i)
else:
    print("Perulangan selesai")

# nested Loop (perulangan bersarang)
for i in range(9):
    for j in range(9):
        print(i, j)

# pola bintang
for i in range(9):
    for j in range(i+1):
        print("*", end="")
    print()

# aplikasi iterasi dalam algoritma
# 1. menghitung jumlah total
angka = [50, 75, 35, 40]
total = 0
for nilai in angka:
    total += nilai

print("Total:", total)

# 2. menghitung faktorial
n = 9
faktorial = 1

for i in range(1, n+1):
    faktorial *= i

print("Faktorial:", faktorial)

# 3. validasi input dengan while
nilai = -1
while nilai < 0:
    nilai = int(input("Masukkan angka positif: "))

print("Input diterima")