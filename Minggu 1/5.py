woi = "xxx"
lala = "12345"
print("Validasi username dan password anda")
coba = 4
for x in range(1,coba):
    a =input("Masukkan username: ")
    b =input("Masukkan password anda: ")
    if a == woi and b == lala :
        print("Anda berhasil masuk")
        break
    else:
        print("Maaf username dan password anda salah")
