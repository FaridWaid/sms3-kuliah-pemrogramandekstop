x = "ya"
while x=="ya":
    print("1. Persegi /n 2. Persegi panjang /n 3. Jajar genjang")
    choice=int(input("Masukkan nomer pilihan: "))
    if choice == 1:
        print("Luas Persegi")
        s = int(input("Masukkan nilai s(sisi): "))
        luas = s * s
        print("Luas Persegi tersebut = ",luas)
        print("")
        print("Keliling Persegi")
        s = int(input("Masukkan nilai s(sisi): "))
        keliling = s*4
        print("Keliling Persegi tersebut = ",keliling)
    elif choice == 2:
        print("Luas Persegi panjang")
        p = int(input("Masukkan nilai p(panjang): "))
        l = int(input("Masukkan nilai l(lebar): "))
        luas = p * l
        print("Luas Persegi panjang tersebut = ",luas)
        print("")
        print("Keliling Persegi panjang")
        p = int(input("Masukkan nilai p(panjang): "))
        l = int(input("Masukkan nilai l(lebar): "))
        keliling = (p + l)*2
        print("Keliling Persegi panjang tersebut = ",keliling)
    else:
        print("Luas jajar genjang")
        a = int(input("Masukkan nilai a(alas): "))
        t = int(input("Masukkan nilai t(tinggi): "))
        luas = a * t
        print("Luas Jajar genjang tersebut = ",luas)
        print("")
        print("Keliling Jajar genjang")
        ab = int(input("Masukkan nilai AB: "))
        bc = int(input("Masukkan nilai BC: "))
        cd = int(input("Masukkan nilai CD: "))
        da = int(input("Masukkan nilai DA: "))
        keliling = ab+bc+cd+da
        print("Keliling Jajar genjang tersebut = ",keliling)
    x = str(input("Apakah ingin menghitung lagi? (ya/tidak)"))
