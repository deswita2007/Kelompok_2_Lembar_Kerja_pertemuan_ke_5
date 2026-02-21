#Library Statement

#Library requests
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)

#Library math
import math
print(math.sqrt(48))
print(math.pi)

#Library Random
import random
angka = random.randint(1, 100)
print("Angka acak:", angka)

#Library datetime
from datetime import datetime
sekarang = datetime.now()
print("Waktu sekarang:", sekarang)

#Menggunakan library random dan if
usia = random.randint(1, 100)
print("Usia:", usia)

if usia < 13:
    print("Kategori: Anak-anak")
elif usia < 18:
    print("Kategori: Remaja")
else:
    print("Kategori: Dewasa")

    