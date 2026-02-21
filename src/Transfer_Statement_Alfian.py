print("TRANSFER STATEMENT DALAM PROSES LOGIN SEDERHANA")
def login():
    kesempatan = 3
    password_benar = "1234"
    percobaan = 0
    
    while kesempatan > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        # pass jika username kosong
        if username == "":
            print("Username tidak boleh kosong")
            pass
        
        # continue jika password terlalu pendek
        elif len(password) < 4:
            print("Password minimal 4 karakter")
            percobaan += 1
            sisa = kesempatan - percobaan
            print(f"Kesempatan anda tersisa {sisa}")
           
            if percobaan == kesempatan:
                print("Akun diblokir")
                break # jika jumlah percobaan sama dengan jumlah kesempatan
    
            continue
        
        # jika password benar
        elif password == password_benar :
            print(f"Login berhasil! Selamat datang {username}")
            return   # return keluar dari fungsi
        
        else:
            percobaan += 1
            sisa = kesempatan - percobaan
            print(f"Username atau password salah, Kesempatan anda tersisa {sisa}")       
             
        # break jika kesempatan habis
        if percobaan == kesempatan:
            print("Akun diblokir")
            break

login()
