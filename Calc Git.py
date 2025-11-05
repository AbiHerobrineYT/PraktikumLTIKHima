#Login

def login_sederhana(): 
    username_benar = "Kelompok 2"
    password_benar = "Cake"

    print("Login Cuyy")
    input_username=input("Masukkan Username anda:")
    input_password=input("Masukkan Password anda:")

    if input_username == username_benar and input_password == password_benar:
        print(f"\nLogin berhasil! Selamat datang, {username_benar}!")
        return True
    else:
        print("\nUsername atau password salah.")
    
    print("\nPercobaan login habis. Akses ditolak.")
    return False