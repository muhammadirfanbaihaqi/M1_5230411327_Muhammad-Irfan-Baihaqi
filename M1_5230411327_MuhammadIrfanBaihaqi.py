import math

def tampilMenuAwal() :
    print("\n========== Selamat Datang ===========")
    print("1. HITUNG VOLUME")
    print("2. HITUNG LUAS PERMUKAAN")           
    print("3. Keluar\n")

def tampilPilihBangun() :
    print("1. BOLA")
    print("2. Kerucut")
    print("3. Tabung")
    print("4. KEMBALI KE MENU UTAMA")

def menuAwal() :
    while True:
        tampilMenuAwal()
        pilih = input("PILIH MENU: ")
        if pilih == "1" :
            hitungVolume()
        elif pilih == "2" :
            hitungLuasPermukaan()
        elif pilih == "3" :
            print("ANDA KELUAR DARI PROGRAM")
            return True
        else:
            print("PILIHAN ANDA SALAH")
            while True:
                koreksi = input("APAKAH INGIN INPUT ULANG? (y/n) : ")
                if koreksi.lower() == "y":
                    break
                elif koreksi.lower() == "n":
                    print("ANDA KELUAR DARI PROGRAM")
                    return True
                else:
                    print("PILIHAN ANDA SALAH")

def hitungVolume() :
    while True:
        tampilPilihBangun()
        pilih = input("Masukkan pilihan bangun yang akan dihitung: ")
        if pilih == "1":
            volumeBola()
        elif pilih == "2":
            volumeKerucut()
        elif pilih == "3":
            volumeTabung()
        elif pilih == "4":
            print("=======KEMBALI KE MENU UTAMA=======")
            return True
        else:
            print("INPUTAN ANDA SALAH")

def hitungLuasPermukaan() :
    while True:
        tampilPilihBangun()
        pilih = input("Masukkan pilihan bangun yang akan dihitung: ")
        if pilih == "1":
            luasPermukaanBola()
        elif pilih == "2":
            luasPermukaanKerucut()
        elif pilih == "3":
            luasPermukaanTabung()
        elif pilih == "4":
            print("=======KEMBALI KE MENU UTAMA=======")
            return True
        else:
            print("INPUTAN ANDA SALAH")

def luasPermukaanBola():
    phi = math.pi
    while True:
        rStr = input("Masukkan jari-jari: ") #INPUT AWAL BERUPA STRING, KARENA SETELAH INI AKAN DICEK MENGGUNAKAN isdigit . isdigit adalah String method .
        # isdigit adalah string method untuk memeriksa apakah isi string adalah angka atau bukan
        cek = rStr.isdigit() #UNTUK MEMERIKSA APAKAH ANGKA ATAU BUKAN.
        if cek == True:
            r = float(rStr) #MENGUBAH DARI STRING MENJADI Angka(float)
            hitung = 4 * phi * r ** 2
            print(f"Luas Permukaan Bola dengan jari-jari {r} adalah {hitung:.3f}")
            print("=====KEMBALI KE MENU HITUNG LUAS PERMUKAAN======")
            return True #KEMBALI KE MENU LUAS PERMUKAAN
        else:
            print("JARI-JARI YANG ANDA MASUKAN SALAH")

def volumeBola():
    phi = math.pi
    while True:
        rStr = input("Masukkan jari-jari: ") 
        cek = rStr.isdigit() #UNTUK MEMERIKSA APAKAH ANGKA ATAU BUKAN.
        if cek == True:
            r = float(rStr) #MENGUBAH MENJADI Angka
            hitung = 4/3 * phi * r ** 3
            print(f"Volume Bola dengan jari-jari {r} adalah {hitung:.3f}")
            print("=======KEMBALI KE MENU HITUNG VOLUME========")
            return True #KEMBALI KE MENU HITUNG VOLUME
        else:
            print("JARI-JARI DAN TINGGI HARUS BERUPA ANGKA")

def volumeTabung():
    phi = math.pi
    while True:
        rStr = input("Masukkan Jari-jari: ")
        tStr = input("Masukkan Tinggi Tabung: ")
        cek1 = rStr.isdigit()
        cek2 = tStr.isdigit()
        if (cek1 == True and cek2 == True):
            r = float(rStr)
            t = float(tStr)
            hitung = phi * r ** 2 * t
            print(f"Volume tabung dengan jari-jari {r} dan tinggi {t} adalah {hitung:.3f}")
            print("KEMBALI KE MENU HITUNG VOLUME")
            return True
        else:
            print("JARI-JARI DAN TINGGI HARUS BERUPA ANGKA")

def luasPermukaanTabung() :
    phi = math.pi
    while True:
        rStr = input("Masukkan Jari-jari : ")
        tStr = input("Masukkan Tinggi Tabung : ")
        cek1 = rStr.isdigit()
        cek2 = tStr.isdigit()
        if (cek1 == True and cek2 == True):
            r = float(rStr)
            t = float(tStr)
            hitung = 2 * phi * r * t + 2 * phi * r ** 2
            print(f"Luas permukaan tabung dengan jari-jari {r} dan tinggi {t} adalah {hitung:.3f}")
            print("=====KEMBALI KE MENU HITUNG LUAS PERMUKAAN======")
            return True
        else:
            print("JARI-JARI DAN TINGGI HARUS BERUPA ANGKA")

def luasPermukaanKerucut() :
    phi = math.pi
    while True:
        rStr = input("Masukkan jari-jari : ")
        tStr = input("Masukkan tinggi kerucut : ")
        cek1 = rStr.isdigit()
        cek2 = tStr.isdigit()
        if (cek1 == True and cek2 == True):
            r = float(rStr)
            t = float(tStr)
            s = math.sqrt(r ** 2 + t ** 2) #S ADALAH GARIS PELUKIS KERUCUT. S = AKARKUADRAT DARI (r**2 + t**2)
            hitung = phi * r * s + phi * r ** 2
            print(f"luas permukaan kerucut dengan tinggi {t} , jari-jari {r}, dan garis pelukis {s:.3f} adalah {hitung:.3f}")
            print("======KEMBALI KE MENU HITUNG LUAS PERMUKAAN======")
            return True
        else:
            print("JARI-JARI DAN TINGGI HARUS BERUPA ANGKA")

def volumeKerucut() :
    phi = math.pi
    while True:
        rStr = input("Masukkan jari-jari : ")
        tStr = input("Masukkan tinggi kerucut : ")
        cek1 = rStr.isdigit()
        cek2 = tStr.isdigit()
        if (cek1 == True and cek2 == True):
            r = float(rStr)
            t = float(tStr)
            hitung = 1 / 3 * phi * r ** 2 * t
            print(f"volume kerucut dengan jari-jari {r} dan tinggi {t} adalah {hitung:.3f}")
            print("=======KEMBALI KE MENU HITUNG VOLUME========")
            return True
        else:
            print("JARI-JARI DAN TINGGI HARUS BERUPA ANGKA")

# SETIAP PRINT HASIL HITUNG DIFORMAT MENJADI 3 ANGKA DI BELAKANG KOMA AGAR LEBIH MUDAH DIBACA .
menuAwal()


            



