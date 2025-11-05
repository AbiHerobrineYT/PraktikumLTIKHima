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

#Calculator

def tambah(a, b):
    hasil = a + b
    return hasil

def kurang(a, b):
    hasil = a - b
    return hasil

def perkalian(a, b):
    hasil = a * b
    return hasil

def pembagian(a, b):
    if b != 0:
        hasil = a / b
        return hasil
    else:
        return "Error pembagian dengan nol"

def modulus(a, b):
    hasil = a % b
    return hasil

def pangkat(a, b):
    hasil = a ** b
    return hasil
    
def bagibulat(a, b):
    hasil = a // b
    return hasil

def Persegi(s):
    hasil = s * s
    return hasil

def PersegiPanjang(a, b):
    hasil = a * b
    return hasil

if login_sederhana():
    history = [] 
    last_result = None

    while True:
        pilihan = input('1.tambah, 2.kurang, 3.perkalian, 4.pembagian, 5.modulus, 6.pangkat, 7. bagi bulat  8.luas persegi, 9.Luas persegi panjang\nPilih angka: ')

        if pilihan in ["1","2","3","4","5","6","7","8","9"]:
            if last_result is not None:
                pakai = input(f"Mau pakai hasil sebelumnya ({last_result}) sebagai angka pertama? (ya/tidak): ").lower()
            else:
                pakai = "tidak"

            if pakai == "ya":
                x = last_result
            else:
                x = int(input("Angka Pertama: "))
            y = int(input("Angka Kedua: "))

        if pilihan == "1":
            hasil = tambah(x, y)
            print("Hasil:", hasil)
            history.append(f"{x} + {y} = {hasil}")

        elif pilihan == "2":
            hasil = kurang(x, y)
            print("Hasil:", hasil)
            history.append(f"{x} - {y} = {hasil}")

        elif pilihan == "3":
            hasil = perkalian(x, y)
            print("Hasil:", hasil)
            history.append(f"{x} * {y} = {hasil}")

        elif pilihan == "4":
            hasil = pembagian(x, y)
            print("Hasil:", hasil)
            history.append(f"{x} / {y} = {hasil}")

        elif pilihan == "5":
            hasil = modulus(x, y)
            print("Hasil:", hasil)
            history.append(f"{x} % {y} = {hasil}")

        elif pilihan == "6":
            hasil = pangkat(x, y)
            print("Hasil:", hasil)
            history.append(f"{x} ^ {y} = {hasil}")
        
        elif pilihan == "7":
            hasil = bagibulat(x, y)
            print("Hasil:", hasil)
            history.append(f"{x} // {y} = {hasil}")
            
        elif pilihan == "8":
            s = float(input("Masukkan panjang sisi persegi: "))
            hasil = Persegi(s)
            print("Hasil:", hasil)
            history.append(f"Luas Persegi ({s}) = {hasil}")
            
        elif pilihan == "9":
            p = float(input("Masukkan panjang: "))
            l = float(input("Masukkan lebar: "))
            hasil = PersegiPanjang(p, l)
            print("Hasil:", hasil)
            history.append(f"Luas Persegi Panjang ({p}x{l}) = {hasil}")
      
        else:
            print('error')
            continue
        
        last_result = hasil  # update hasil terakhir

        lanjut = input('Apakah mau lanjut?:')
        if lanjut.lower() != "ya":
            print("\n=== Program selesai. Riwayat perhitungan: ===")
            for h in history:
                print(h)
            break