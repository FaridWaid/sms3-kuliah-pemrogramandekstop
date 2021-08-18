def Makanan(i):
    total1=0
    if nomor==1:
        total1=total1+porsi1*12000
        print ("----- Nasi Goreng 12000 -----")
        print ("Hasilnya = ", total1)
        jenis1=("Nasi Goreng")
    elif nomor==2:
        total1=total1+porsi1*10000
        print ("----- Soto 10000 -----")
        print ("Hasilnya = ", total1)
        jenis1=("Soto")
    elif nomor==3:
        total1=total1+porsi1*9000
        print ("----- Mie Ayam 9000 -----")
        print ("Hasilnya = ", total1)
        jenis1=("Mie Ayam")
    else:
        ("Masukan Pilihan yang Benar!")
    return total1

def Minuman(i):
    total2=0
    if nomor==1:
        total2=total2+(porsi2*3000)
        print ("----- Es Teh 3000 -----")
        print ("Hasilnya = ", total2)
        jenis2=("Es Teh")
    if nomor==2:
        total2=total2+(porsi2*4000)
        print ("----- Es Jeruk 4000 -----")
        print ("Hasilnya = ", total2)
        jenis2=("Es Jeruk")
    if nomor==3:
        total2=total2+(porsi2*3000)
        print ("----- Es Kopi 3000 -----")
        print ("Hasilnya = ", total2)
        jenis2=("Es Kopi")
    else:
        ("Masukan Pilihan yang Benar!")
    return total2

#Makanan
print ("Menu Makanan")
print("1. Nasi Goreng")
print("2. Soto")
print("3. Mie Ayam")
nomor=int(input("Masukan Pilihan: "))
porsi1= int(input("Berapa Porsi: "))
menu1=Makanan(nomor)

#Minuman
print("\nMenu Minuman")
print("1. Es teh")
print("2. Es jeruk")
print("3. Es kopi")
nomor=int(input("Masukan Pilihan: "))
porsi2= int(input("Berapa Gelas: "))
menu2=Minuman(nomor)

#Total Tagihan
uang=int(input("\nUang Tunai: Rp."))
totalsemua=menu1+menu2    
print("\n=========================")
print("======= S T R U K =======")
print("=========================")
print ("=== Tagihan   :Rp.",totalsemua)
print ("=== Uang      :Rp.",uang)
akhir=int(uang-totalsemua)
print ("=== Kembalian :Rp.",akhir)
print("=========================")
print("=========================")